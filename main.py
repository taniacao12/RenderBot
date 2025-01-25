import os, time
import numpy as np

from utils.file_utils import *
from utils.data_utils import getBoundary, getWalls, getDoors, getRooms
from plan import Plan

def run (name, imagePath) -> None:
    imagePath = directory + '/' + imagePath
    print("Reading {}".format(imagePath))
    height, width, c1, c2 = readImage(imagePath)

    print("Printing output files [{}]...".format(name))
    printImage(name, height, width, c1, c2)
    printPlan(1, "program.txt", c1)
    # printPlan(2, "instance.txt", c2)

    boundary = getBoundary(height, width, c1)
    # printPlan(2, "walls.txt", boundary)
    printPlan(2, "boundary/{}.txt".format(name), boundary)

    walls = getWalls(height, width, np.copy(boundary))
    printShapes("walls/{}.txt".format(name), walls)

    doors = getDoors(height, width, c1, boundary)
    printShapes("doors/{}.txt".format(name), doors)

    rooms = getRooms(height, width, c1, boundary)
    printShapes("rooms/{}.txt".format(name), rooms)

    # plan = Plan(imagePath, height, width, walls, doors, rooms)
    # output('Text/{}.txt'.format(choice), plan.output())
    # printJSON(name, plan)
        
if __name__ == '__main__':
    start = time.time()

    directory = 'data/RPLAN'
    files = sorted(os.listdir(directory), key = natural_sort_key)
    command = input("Enter your command: ").strip().lower()
    while command != "all" and not command.isdigit():
        command = input("Enter your command: ").strip().lower()
    if command == "all":
        fileBatch = files[0:101]
        for i in range(len(fileBatch)):
            run(i, fileBatch[i])
    elif command.isdigit():
        run(int(command), files[int(command)])

    end = time.time()
    print("Runtime: {}".format(end - start))
