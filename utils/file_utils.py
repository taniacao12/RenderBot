"""
Functions for the following:
 - read image files
 - text sorting methods
 - creating and writing files
"""

import re, json
import numpy as np
import imageio.v2 as imageio
from skimage import measure

from legend import color_code, program_code, program_desc, scaleFactor

def natural_sort_key(s):
    """
    key to sort file names in natural format where '1' < '2' < '10' instead of '1' < '10' < '2'
    """
    return [int(text) if text.isdigit() else text.lower() for text in re.split('([0-9]+)', s)]

def readImage (imagePath: str):
    """
    read image, get its channels, and reformat them for clarity and consistency
    """
    image = imageio.imread(imagePath)
    c1 = image[..., 1] # program
    mask = (c1 != 13).astype(np.uint8)
    region = measure.regionprops(mask.astype(np.uint8))[0]
    y0, x0, y1, x1 = region.bbox
    c1 = np.array([[program_code[col] for col in row] for row in c1[y0:y1, x0:x1]], dtype = np.uint8)
    height, width = c1.shape
    return height, width, c1

def printImage (fileName: str, height: int, width: int, program: np.array):
    """
    format array into image array format and write into a png file with the given file name
    """
    coloredImage = np.zeros((height, width, 3), dtype = np.uint8)
    for y in range(height):
        for x in range(width):
            rgb = color_code[program[y, x]]
            coloredImage[y, x] = [rgb[0], rgb[1], rgb[2]]
    imageio.imwrite('data/dataset/{}.png'.format(fileName), coloredImage)

def output(fileName: str, text: str) -> None:
    """
    create file with given file name and write given text into it
    """
    with open('output/' + fileName, 'w') as file:
        file.write(text)

def printPlan (option: int, fileName: str, array: np.array) -> None:
    """
    convert array into formatted text and write it into a file with the given file name
    """
    #        0         1         2
    #         123456789 123456789 12345
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    text = ""
    for row in array:
        for col in row:
            if col == 0 or col == '': text += ' ' # external area
            elif option == 1: # program
                if col == 1: text += '.' # exterior wall
                elif col == 2: text += ',' # interior wall
                elif col == 3: text += '*' # exterior door
                elif col == 4: text += '~' # interior doors
                else: text += alpha[col - 5] # rooms
            elif option == 2: # orientation
                if col == 'Horizontal': text += '-' # horizontal
                elif col == 'Vertical': text += '|' # vertical
                elif col == 'Corner': text += '*' # corner
            elif option == 3: # boundary
                if col == 'External': text += '*' # exterior wall
                elif col == 'Internal': text += '.' # interior wall
                elif col == 'Rooms': text += '_' # interior rooms
            else: text += str(col) # test
        text += '\n'
    output(fileName, text)

def scaleFormat (shape: list):
    '''
    scale shape based on scale factor and format to [x, y] format
    '''
    temp = []
    for point in shape:
        newPoint = [coor * scaleFactor for coor in point]
        temp.append([newPoint[1], -newPoint[0]])
    return temp

def rhinoCoorFormat (coors: list):
    '''
    format shape coordinates to work with Rhino
    '''
    i, temp, hanging = 1, [coors[0]], False
    while i < len(coors) - 1:
        prev, curr, next, last = coors[i - 1], coors[i], coors[i + 1], temp[-1]
        if curr[0] == prev[0]:
            dist = curr[1] - prev[1]
            corner = (prev[1] < curr[1] and curr[0] > next[0]) \
                or (prev[1] > curr[1] and curr[0] < next[0])
            if hanging:
                temp.append([last[0], last[1] + dist])
                if not corner: hanging = False
            elif dist > 0: temp.append([last[0], last[1] + dist + 1])
            else: temp.append([last[0], last[1] + dist - 1])
            if prev[1] < curr[1] and curr[0] > next[0]: # EN corner
                temp[-1][1] -= 1
                hanging = True
            elif prev[1] > curr[1] and curr[0] < next[0]: # WS corner
                temp[-1][1] += 1
                hanging = True
        elif curr[1] == prev[1]:
            if i == 1:
                temp.append([last[0], last[1] + 1])
                last = temp[-1]
            dist = curr[0] - prev[0]
            if hanging:
                temp.append([last[0] + dist, last[1]])
                hanging = False
            elif dist > 0:
                temp.append([last[0] + dist + 1, last[1]])
            else: temp.append([last[0] + dist - 1, last[1]])
            if prev[0] < curr[0] and curr[1] < next[1]: # SE corner
                temp[-1][0] -= 1
                hanging = True
            elif prev[0] > curr[0] and curr[1] > next[1]: # NW corner
                temp[-1][0] += 1
                hanging = True

        if prev == next and curr[0] == next[0]: # horizontal line
            temp.append([curr[0] + 1, curr[1] + 1])
            temp.append([next[0] + 1, next[1]])
            i += 2
        elif prev == next and curr[1] == next[1]: # vertical line
            temp.append([curr[0] + 1, curr[1] + 1])
            temp.append([next[0], next[1] + 1])
            i += 2
        elif prev[0] == curr[0] and curr[0] == next[0]: # line right/left
            last = temp[-1]
            if i < len(coors) - 2 and next[0] == coors[i + 2][0]: # right and left
                temp.append([last[0] + 1, last[1]])
                temp.append([last[0] + 1, next[1]])
                temp.append(next)
                temp.append(coors[i + 2])
                hanging = True
                i += 1
            else: # right or left
                temp.append([last[0], last[1] - 1])
                temp.append(curr)
                hanging = True
            i += 1
        elif prev[1] == curr[1] and curr[1] == next[1]: # line up/down
            # add test case for up and down
            last = temp[-1]
            temp.append([last[0], last[1] - 1])
            if next != coors[-1]:
                temp.append(curr)
                hanging = True
                i += 1
        i += 1
    temp.append(temp[0])
    return scaleFormat(temp)

def rhinoFormat (info: dict):
    '''
    format info to work with Rhino
    '''
    for featureType in info:
        for id in info[featureType]:
            temp = info[featureType][id]
            temp['Coordinates'] = rhinoCoorFormat(temp['Coordinates'])
    return info

def printJSON (fileName: str, data: dict, option: str = None, imagePath: str = None) -> None:
    """
    export data as JSON file with the given file name
    """
    with open('output/JSON/{}.json'.format(fileName), 'w') as file:
        if option == 'Rhino':
            data = {
                'Image Path': imagePath,
                'Features': rhinoFormat(data)
            }
        json.dump(data, file, indent = 4)