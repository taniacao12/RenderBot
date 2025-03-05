import os, time

from utils.file_utils import *
from utils.data_utils import getPlans, getInfo

def run (name, imagePath) -> None:
    imagePath = directory + '/' + imagePath
    print("Reading {}".format(imagePath))
    height, width, program = readImage(imagePath)
    orientations, boundary = getPlans(height, width, program)
    _, info = getInfo(height, width, program, orientations, boundary)
    
    print("Printing output files [{}]...".format(name))
    printImage(name, height, width, program)
    # printPlan(1, "program.txt", program)
    # printPlan(2, "orientations.txt", orientations)
    # printPlan(3, "boundary.txt", boundary)
    # printJSON('JSON/{}'.format(name), info)
    printJSON('JSON/{}'.format(name), info, 'Rhino', imagePath, width, height)

if __name__ == '__main__':
    start = time.time()

    directory = 'references/RPLAN'
    files = sorted(os.listdir(directory), key = natural_sort_key)
    command = input("Enter your command: ").strip().lower()
    while command != "all" and not command.isdigit():
        command = input("Enter your command: ").strip().lower()
    if command == "all":
        start = 285
        end = 500
        fileBatch = files[start:end + 1]
        for i in range(len(fileBatch)):
            run(i + start, fileBatch[i])
    elif command.isdigit():
        run(int(command), files[int(command)])

    end = time.time()
    print("Runtime: {}".format(end - start))