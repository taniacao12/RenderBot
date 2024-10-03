import os, random
import imageio.v2 as imageio

import utils
from plan import Plan

def output(fileName, text):
    with open('output/' + fileName, 'w') as file:
        file.write(text)

def printChannel (type, fileName, channel):
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    text = ""
    for row in channel:
        for col in row:
            if type == 2:
                if col == 13: text += ' ' # external area
                elif col == 14: text += '.' # exterior wall
                elif col == 15: text += '*' # front door
                elif col == 16: text += '.' # interior walls
                elif col == 17: text += '~' # interior doors
                else: text += alpha[col - 1]
            else:
                if col == 0: text += ' ' # external area
                elif type == 1:
                    if col == 127: text += '.' # exterior wall
                    elif col == 255: text += '*' # front door
                    else: text += alpha[col - 1]
                elif type == 3: text += str(col) # rooms
                elif type == 4: text += '*' # interior area
        text += '\n'
    output(fileName, text)

def printChannels (c0, c1, c2):
    printChannel(1, 'boundary.txt', c0)
    printChannel(2, 'program.txt', c1)
    printChannel(3, 'instance.txt', c2)
    printChannel(4, 'inside.txt', c2)

def rplan ():
    # select file from dataset
    # choice = 1
    directory = 'data/RPLAN'
    files = os.listdir(directory)
    while True:
        choice = int(input("Select a file for simulation:\nPick a number from 1 to {} or 0 for random choice => ".format(len(files))).strip())
        if 0 <= choice <= len(files): break
    if choice == 0:
        imagePath = directory + '/' + random.choice(files)
    else: imagePath = directory + '/' + files[choice - 1]
    print("Reading {}".format(imagePath))

    # read image and gather its data
    image = imageio.imread(imagePath)
    # print(image.shape) # print out image metadata (size and number of channels)
    c0, c1, c2, c3 = utils.getChannels(image)
    # printChannels(c0, c1, c2, c3)

    interiorDoors = utils.getInteriorDoors(c1)
    rooms = utils.getRooms(c1, c2, interiorDoors)
    frontDoor = utils.getFrontDoor(c0, c2, rooms)
    plan = Plan(c1, frontDoor, interiorDoors, rooms)
    output('output.txt', plan.output())

if __name__ == '__main__':
    rplan()