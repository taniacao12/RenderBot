import numpy as np
from skimage import measure, feature, segmentation
from scipy import ndimage

from legend import nbr, oppositeDir
from utils.file_utils import printPlan
from door import Door
from room import Room
from window import Window

def getX (c1: np.array, row: int, col: int):
    count = 1
    for c in range(col + 1, len(c1[row])):
        if c1[row][c] in [1, 2, 3, 4]: count += 1
        else: break
    for c in range(col - 1, -1, -1):
        if c1[row][c] in [1, 2, 3, 4]: count += 1
        else: break
    return count

def getY (c1: np.array, row: int, col: int):
    count = 1
    for r in range(row + 1, len(c1)):
        if c1[r][col] in [1, 2, 3, 4]: count += 1
        else: break
    for r in range(row - 1, -1, -1):
        if c1[r][col] in [1, 2, 3, 4]: count += 1
        else: break
    return count

def getBoundary (rows: int, cols: int, c1: np.array):
    temp = np.zeros((rows, cols), dtype=np.uint8)
    for row in range(rows):
        for col in range(cols):
            if c1[row][col] in [1, 2, 3, 4]:
                x = getX(c1, row, col)
                y = getY(c1, row, col)
                if x > y: temp[row][col] = 1
                elif x < y: temp[row][col] = 2
                else: temp[row][col] = 3
    # printPlan(2, "walls.txt", temp)

    row = 0
    while row < rows:
        col = 0
        while col < cols:
            if col > 1 and temp[row][col] == 2 and temp[row][col - 1] in [1, 3]:
                temp[row][col] = 3
                while col < cols - 1 and temp[row][col + 1] == 2:
                    temp[row][col + 1] = 3
                    col += 1
            elif col < cols - 1 and temp[row][col] == 2 and temp[row][col + 1] in [1, 3]:
                temp[row][col] = 3
                c = col - 1
                while c > -1 and temp[row][c] == 2:
                    temp[row][c] = 3
                    c -= 1
            elif row > 1 and temp[row][col] == 1 and temp[row - 1][col] in [2, 3]:
                temp[row][col] = 3
                r = row
                while r < rows - 1 and temp[r + 1][col] == 1:
                    temp[r + 1][col] = 3
                    r += 1
            elif row < rows - 1 and temp[row][col] == 1 and temp[row + 1][col] in [2, 3]:
                temp[row][col] = 3
                r = row - 1
                while r > -1 and temp[r][col] == 1:
                    temp[r][col] = 3
                    r -= 1
            col += 1
        row += 1
    return temp

def getNextOptions (boundary: np.array, row: int, col: int, num: int):
    ret = []
    if row + nbr['N'][0] >= 0 and boundary[row + nbr['N'][0]][col + nbr['N'][1]] == num:
        ret.append('N')
    if col + nbr['E'][1] < len(boundary[row]) and boundary[row + nbr['E'][0]][col + nbr['E'][1]] == num:
        ret.append('E')
    if row + nbr['S'][0] < len(boundary) and boundary[row + nbr['S'][0]][col + nbr['S'][1]] == num:
        ret.append('S')
    if col + nbr['W'][1] >= 0 and boundary[row + nbr['W'][0]][col + nbr['W'][1]] == num:
        ret.append('W')
    return ret

def getBorderNext (boundary: np.array, row: int, col: int, dir: str, num: int):
    options = getNextOptions(boundary, row, col, num)
    N = [row + nbr['N'][0], col + nbr['N'][1]]
    S = [row + nbr['S'][0], col + nbr['S'][1]]
    E = [row + nbr['E'][0], col + nbr['E'][1]]
    W = [row + nbr['W'][0], col + nbr['W'][1]]
    if dir == 'E':
        if 'N' in options: return N[0], N[1], 'N', True
        elif 'E' in options: return E[0], E[1], 'E', False
        elif 'S' in options: return S[0], S[1], 'S', True
        return row, col, 'W', True
    elif dir == 'S':
        if 'E' in options: return E[0], E[1], 'E', True
        elif 'S' in options: return S[0], S[1], 'S', False
        elif 'W' in options: return W[0], W[1], 'W', True
        return row, col, 'N', True
    elif dir == 'W':
        if 'S' in options: return S[0], S[1], 'S', True
        elif 'W' in options: return W[0], W[1], 'W', False
        elif 'N' in options: return N[0], N[1], 'N', True
        return row, col, 'E', True
    elif dir == 'N':
        if 'W' in options: return W[0], W[1], 'W', True
        elif 'N' in options: return N[0], N[1], 'N', False
        elif 'E' in options: return E[0], E[1], 'E', True
        return row, col, 'S', True

def getSnakeNext (boundary: np.array, row: int, col: int, dir: str, num: int, temp: list):
    options = getNextOptions(boundary, row, col, num)
    if not options: return row, col, 'Done', temp
    N = [row + nbr['N'][0], col + nbr['N'][1]]
    S = [row + nbr['S'][0], col + nbr['S'][1]]
    E = [row + nbr['E'][0], col + nbr['E'][1]]
    W = [row + nbr['W'][0], col + nbr['W'][1]]
    retR, retC, retD = None, None, None
    if dir == 'E':
        if 'N' in options: retR, retC, retD = N[0], N[1], 'N'
        if 'E' in options:
            if not retD: retR, retC, retD = E[0], E[1], 'E'
            elif E not in temp: temp.append(E)
        if 'S' in options:
            if not retD: retR, retC, retD = S[0], S[1], 'S'
            elif S not in temp: temp.append(S)
        if 'W' in options:
            if not retD: retR, retC, retD = W[0], W[1], 'W'
            elif W not in temp: temp.append(W)
        return retR, retC, retD, temp
    elif dir == 'N':
        if 'N' in options: retR, retC, retD = N[0], N[1], 'N'
        if 'W' in options:
            if not retD: retR, retC, retD = W[0], W[1], 'W'
            elif W not in temp: temp.append(W)
        if 'E' in options:
            if not retD: retR, retC, retD = E[0], E[1], 'E'
            elif E not in temp: temp.append(E)
        return retR, retC, retD, temp
    elif dir == 'W':
        if 'N' in options: retR, retC, retD = N[0], N[1], 'N'
        if 'W' in options:
            if not retD: retR, retC, retD = W[0], W[1], 'W'
            elif W not in temp: temp.append(W)
        if 'S' in options:
            if not retD: retR, retC, retD = S[0], S[1], 'S'
            elif S not in temp: temp.append(S)
        return retR, retC, retD, temp
    elif dir == 'S':
        if 'W' in options: retR, retC, retD = W[0], W[1], 'W'
        if 'E' in options:
            if not retD: retR, retC, retD = E[0], E[1], 'E'
            elif E not in temp: temp.append(E)
        if 'S' in options:
            if not retD: retR, retC, retD = S[0], S[1], 'S'
            elif S not in temp: temp.append(S)
        return retR, retC, retD, temp

def getShape (boundary: np.array, row: int, col: int):
    # get points
    num = boundary[row][col]
    shape, dir = [[row, col]], 'E'
    row, col, dir, turn = getBorderNext(boundary, row, col, dir, num)
    while [row, col] != shape[0] and boundary[row, col] == num:
        r, c, d, turn = getBorderNext(boundary, row, col, dir, num)
        if turn: shape.append([row, col])
        row, col, dir = r, c, d
    if [row, col] == shape[0]: shape.append([row, col])

    # remove shape from boundary
    row, col, dir, temp = shape[0][0], shape[0][1], 'E', []
    while boundary[row][col] == num:
        boundary[row][col] = 0
        # if row > 87 and col > 37:
        #     printPlan(2, "testing.txt", boundary)
        #     time.sleep(.2)
        row, col, dir, temp = getSnakeNext(boundary, row, col, dir, num, temp)
        if dir == 'Done':
            if temp: row, col, dir = temp[0][0], temp[0][1], 'E'
            else: break
        if [row, col] in temp: temp.remove([row, col])

    if num == 4: shape.insert(0, 3)
    else: shape.insert(0, num)
    return boundary, shape

def getWalls (rows: int, cols: int, boundary: np.array):
    walls = []
    for row in range(rows):
        for col in range(cols):
            if boundary[row][col]:
                boundary, shape = getShape(boundary, row, col)
                # print(shape)
                walls.append(shape)
    return walls

def getDoors (rows: int, cols: int, c1: np.array, boundary: np.array):
    temp = np.zeros((rows, cols), dtype=np.uint8)
    for row in range(rows):
        for col in range(cols):
            if c1[row][col] in [3, 4] and boundary[row][col] != 3:
                temp[row][col] = c1[row][col] - 2

    doors = []
    for row in range(rows):
        for col in range(cols):
            if temp[row][col]:
                temp, shape = getShape(temp, row, col)
                shape.insert(1, boundary[row][col])
                doors.append(shape)
    return doors

def getRooms (rows: int, cols: int, c1: np.array, boundary: np.array):
    temp = np.zeros((rows, cols), dtype=np.uint8)
    for row in range(rows):
        for col in range(cols):
            if c1[row][col] and boundary[row][col] == 0:
                temp[row][col] = c1[row][col]
    # printPlan(1, "testing.txt", temp)

    rooms = []
    for row in range(rows):
        for col in range(cols):
            if temp[row][col]:
                temp, shape = getShape(temp, row, col)
                rooms.append(shape)
    return rooms

# def getRegion (array: np.array, criteria: int, type: bool) -> np.array:
#     if type: mask = array == criteria
#     else: mask = array != criteria
#     return measure.regionprops(mask.astype(np.uint8))[0]

# def getRegions (array: np.array, criteria: int, type: bool) -> list:
#     if type: mask = (array == criteria).astype(np.uint8)
#     else: mask = (array != criteria).astype(np.uint8)
#     distance = ndimage.morphology.distance_transform_cdt(mask)
#     local_maxi = (distance > 1).astype(np.uint8)
#     corner_measurement = feature.corner_harris(local_maxi)
#     local_maxi[corner_measurement > 0] = 0
#     markers = measure.label(local_maxi)
#     labels = segmentation.watershed(-distance, markers, mask=mask, connectivity=8)
#     regions = measure.regionprops(labels)
#     return regions

# def collides (bbox1: tuple[int, int, int, int], bbox2: tuple[int, int, int, int], th: int = 0) -> bool:
#     """
#     determine if two bounding boxes collide
#     :param bbox1: bounds of box 1 (y0, y1, x0, x1)
#     :param bbox2: bounds of box 2 (y0, y1, x0, x1)
#     :param th: optional margin to add to the boxes (default 0)
#     :return: True if boxes collide, False otherwise
#     """
#     return not(
#         (bbox1[0] - th > bbox2[1]) or
#         (bbox1[1] + th < bbox2[0]) or
#         (bbox1[2] - th > bbox2[3]) or
#         (bbox1[3] + th < bbox2[2])
#     )

# def pointBoxRelation (coor: tuple[int, int], box: tuple[int, int, int, int]) -> str:
#     """
#     finds the relation of the coor to the box
#      NW  N  NE
#         ---
#      W | I | E
#         ---
#      SW  S  SE
#      O for surrounding
#     """
#     y, x = coor
#     y0, y1, x0, x1 = box
#     if (x < x0 and y <= y0) or (x == x0 and y == y0): return 'NW'
#     elif x0 <= x < x1 and y <= y0: return 'N'
#     elif (x1 <= x and y < y0) or (x == x1 and y == y0): return 'NE'
#     elif x <= x0 and y0 < y <= y1: return 'W'
#     elif x0 < x < x1 and y0 < y < y1: return 'I'
#     elif x1 <= x and y0 <= y < y1: return 'E'
#     elif (x <= x0 and y1 < y) or (x == x0 and y == y1): return 'SW'
#     elif x0 < x <= x1 and y1 <= y: return 'S'
#     elif (x1 < x and y1 <= y) or (x == x1 and y == y1): return 'SE'
#     else: return None

def getOldRooms (c1: np.array, c2: np.array) -> dict[Room]:
    rooms = {}
    for region in measure.regionprops(c2):
        rooms[int(region.label)] = Room(region, c1)
    
    # find relations between rooms
    keys = list(rooms.keys())
    for a in range(len(keys)):
        for b in range(a + 1, len(keys)):
            # check if two rooms are connected
            A, B = keys[a], keys[b]
            if not collides(rooms[A].getBounds(), rooms[B].getBounds(), 9):
                continue # rooms are not connected
            # if they are, check the spatial relation between them
            ay0, ay1, ax0, ax1 = rooms[A].getBounds()
            by0, by1, bx0, bx1 = rooms[B].getBounds()
            if ax0 < bx0 and ax1 > bx1 and ay0 < by0 and ay1 > by1:
                relation = 'O' # room a surrounds room b
            elif ax0 >= bx0 and ax1 <= bx1 and ay0 >= by0 and ay1 <= by1:
                relation = 'I' # room a is inside room b
            else: relation = pointBoxRelation(rooms[A].getCentroid(), rooms[B].getBounds())
            rooms[A].addRelation(oppositeDir[relation], rooms[B])
            rooms[B].addRelation(relation, rooms[A])
    return rooms

# def roomRelation (door: Door, box: Room) -> str:
#     """
#     finds the relation of the door to the box
#         NW N NE
#         -------
#      WN|       | EN
#      W |       | E
#      WS|       | ES
#         -------
#         SW S SE
#     """
#     y0, y1, x0, x1 = box.getBounds()
#     yc, xc = box.getCentroid()
#     y, x = door.getCentroid()
#     if x == xc and y < yc: return 'N'
#     elif x == xc and y > yc: return 'S'
#     elif y == yc and x < xc: return 'W'
#     elif y == yc and x > xc: return 'E'
#     elif x0 < x < xc:
#         if y < yc: return 'NW'
#         else: return 'SW'
#     elif xc < x < x1:
#         if y < yc: return 'NE'
#         else: return 'SE'
#     elif y0 < y < yc:
#         if x < xc: return 'WN'
#         else: return 'EN'
#     elif yc < y < y1:
#         if x < xc: return 'WS'
#         else: return 'ES'
#     else: return None

# def getDoor (id: int, region: np.array, egress, c1: np.array, c2: np.array, rooms: dict[Room]) -> Door:
#     y0, x0, y1, x1 = np.array(region.bbox)
#     centerH = int((x0 + x1 - 1) / 2)
#     centerV = int((y0 + y1 - 1) / 2)
#     if egress: # fix
#         if c1[y0 - 1][centerH] > 5 or c1[y1 + 1][centerH] > 5:
#             orientation = 'H'
#             r1 = c2[y0 - 1][centerH]
#             r2 = c2[y1 + 1][centerH]
#         elif c1[centerV][x0 - 1] > 5 or c1[centerV][x1 + 1] > 5:
#             orientation = 'V'
#             r1 = c2[centerV][x0 - 1]
#             r2 = c2[centerV][x1 + 1]
#     elif c1[y0 - 1][centerH] > 5 and c1[y1 + 1][centerH] > 5:
#         orientation = 'H'
#         r1 = c2[y0 - 1][centerH]
#         r2 = c2[y1 + 1][centerH]
#     elif c1[centerV][x0 - 1] > 5 and c1[centerV][x1 + 1] > 5:
#         orientation = 'V'
#         r1 = c2[centerV][x0 - 1]
#         r2 = c2[centerV][x1 + 1]
#     else: return None
#     door = Door(id, region, orientation, egress)
#     if r1 != 0:
#         door.addRoom(r1)
#         if egress:
#             door.addRoom(0)
#             rooms[r1].addDoor(door, 'I', 0)
#     if r2 != 0:
#         if egress:
#             door.addRoom(0)
#             rooms[r2].addDoor(door, 'I', 0)
#         door.addRoom(r2)
#     if r1 != 0 and r2 != 0:
#         rooms[r1].addDoor(door, roomRelation(door, rooms[r2]), r2)
#         rooms[r2].addDoor(door, roomRelation(door, rooms[r1]), r1)
#     return door

# def getDoors (c1: np.array, c2: np.array, rooms: dict[Room]) -> dict[Door]:
#     doors = {}
#     # egress door
#     doors[len(doors) + 1] = getDoor(len(doors) + 1, getRegion(c1, 3, True), True, c1, c2, rooms)
#     # interior doors
#     for region in getRegions(c1, 5, True):
#         door = getDoor(len(doors) + 1, region, False, c1, c2, rooms)
#         if door: doors[len(doors) + 1] = door
#     return doors

# def getWindow (id: int, region: np.array, c1: np.array, c2: np.array, rooms: dict[Room]) -> Window:
#     y0, x0, y1, x1 = np.array(region.bbox)
#     centerH = int((x0 + x1 - 1) / 2)
#     centerV = int((y0 + y1 - 1) / 2)
#     if c1[y0 - 1][centerH] in range(1, 6) or c1[y1 + 1][centerH] in range(1, 6):
#         orientation = 'V'
#         r1 = c2[centerV][x0 - 1]
#         r2 = c2[centerV][x1 + 1]
#     else:
#         orientation = 'H'
#         r1 = c2[y0 - 1][centerH]
#         r2 = c2[y1 + 1][centerH]
#     window = Window(id, region, orientation)
#     if r1 != 0:
#         window.setRoom(r1)
#         rooms[r1].addWindow(roomRelation(window, rooms[r1]), window)
#     elif r2 != 0:
#         window.setRoom(r2)
#         rooms[r2].addWindow(roomRelation(window, rooms[r2]), window)
#     if window.room == None: return None
#     return window

# def getWindows (c1: np.array, c2: np.array, rooms: dict[Room]) -> dict[Door]:
    windows = {}
    passer = False
    for region in getRegions(c1, 2, True):
        window = getWindow(len(windows) + 1, region, c1, c2, rooms)
        if window: windows[len(windows) + 1] = window
    return windows