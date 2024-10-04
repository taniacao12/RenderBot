import os, re, random, json
import imageio.v2 as imageio

import utils
from plan import Plan

def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split('([0-9]+)', s)]

def output(fileName, text):
    with open('output/' + fileName, 'w') as file:
        file.write(text)

def printChannel (type, fileName, channel):
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    text = ""
    for row in channel:
        for col in row:
            if col == 0: text += ' ' # external area
            elif type == 1:
                if col == 1: text += '.' # exterior wall
                elif col == 2: text += '*' # front door
                elif col == 3: text += '.' # interior walls
                elif col == 4: text += '~' # interior doors
                else: text += alpha[col - 1]
            elif type == 2: text += str(col)
        text += '\n'
    output(fileName, text)

def printChannels (c0, c1):
    printChannel(1, 'program.txt', c0)
    printChannel(2, 'rooms.txt', c1)

def rplan ():
    while True:
        # select file from dataset
        directory = 'data/dataset'
        files = sorted(os.listdir(directory), key=natural_sort_key)
        while True:
            choice = int(input("Select a file for simulation:\nPick a number from 1 to {}, 0 for random choice, or -1 to exit program\n=> ".format(len(files))).strip())
            if -1 <= choice <= len(files): break
        if choice == -1: break
        elif choice == 0: imageName = random.choice(files)
        else: imageName = files[choice - 1]
        imagePath = directory + '/' + imageName
        print("Reading {}".format(imagePath))

        # read image and gather its data
        image = imageio.imread(imagePath)
        height, width, channels = image.shape
        # print(height, width, channels)
        c0, c1 = utils.getData(image)
        # printChannels(c0, c1)

        interiorDoors = utils.getInteriorDoors(c0)
        rooms = utils.getRooms(c0, c1, interiorDoors)
        frontDoor = utils.getFrontDoor(c0, c1, rooms)
        plan = Plan(imagePath, height, width, frontDoor, interiorDoors, rooms)

        output(imageName.split('.')[0] + '.txt', plan.output())
        with open('output/{}.json'.format(imageName.split('.')[0]), 'w') as file:
            json.dump(plan, file, default=lambda o: o.to_dict(), indent=4)

if __name__ == '__main__':
    rplan()