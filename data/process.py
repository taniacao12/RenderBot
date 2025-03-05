import os, time

from utils.file_utils import *

def getExternalWalls (data: dict):
    walls = data['Features']['Walls']
    ret = {}
    for i, each in enumerate(walls):
        if each[-2:] == 'EW':
            ret['W{:02}'.format(len(ret) + 1)] = walls[each]
    return ret

if __name__ == '__main__':
    start = time.time()

    directory = 'JSON'
    files = sorted(os.listdir(directory), key = natural_sort_key)

    walls = []
    groups = []
    for name in range(len(files)):
        data = readJSON(directory + '/' + files[name])
        externalWalls = getExternalWalls(data)
        if externalWalls in walls:
            groups[walls.index(externalWalls)].append(name)
        else:
            walls.append(externalWalls)
            groups.append([name])

    content = {}
    for each in groups:
        length = len(each)
        if length in content:
            content[length].append(each)
        else: content[length] = [each]
    printJSON('groups', content)

    end = time.time()
    print("Runtime: {}".format(end - start))