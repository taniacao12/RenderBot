import numpy as np

from legend import nbr
from utils.file_utils import printPlan

def getX (program: np.array, row: int, col: int):
    '''
    find width of continuous wall
    '''
    count = 1
    for c in range(col + 1, len(program[row])):
        if program[row][c] in [1, 2, 3, 4]: count += 1
        else: break
    for c in range(col - 1, -1, -1):
        if program[row][c] in [1, 2, 3, 4]: count += 1
        else: break
    return count

def getY (program: np.array, row: int, col: int):
    '''
    find length of continuous wall
    '''
    count = 1
    for r in range(row + 1, len(program)):
        if program[r][col] in [1, 2, 3, 4]: count += 1
        else: break
    for r in range(row - 1, -1, -1):
        if program[r][col] in [1, 2, 3, 4]: count += 1
        else: break
    return count

def getPlans (rows: int, cols: int, program: np.array):
    '''
    create a new set of plans where p1 denotes orientations and p2 displays boundaries:
    '''
    p1 = np.zeros((rows, cols), dtype = np.uint8)
    p2 = np.zeros((rows, cols), dtype = np.uint8)
    for row in range(rows):
        for col in range(cols):
            if program[row][col] in [1, 2, 3, 4]:
                x = getX(program, row, col)
                y = getY(program, row, col)
                if x > y: p1[row][col] = 1 
                elif x < y: p1[row][col] = 2
                else: p1[row][col] = 3
                if program[row][col] % 2: p2[row][col] = 1
                else: p2[row][col] = 2
            elif program[row][col] >= 5: p2[row][col] = 3
    # printPlan(2, "plan.txt", p1)

    # convert all interconnecting parts of p1 into corners
    row = 0
    while row < rows:
        col = 0
        while col < cols:
            if col > 1 and p1[row][col] == 2 and p1[row][col - 1] in [1, 3]:
                p1[row][col] = 3
                while col < cols - 1 and p1[row][col + 1] == 2:
                    p1[row][col + 1] = 3
                    col += 1
            elif col < cols - 1 and p1[row][col] == 2 and p1[row][col + 1] in [1, 3]:
                p1[row][col] = 3
                c = col - 1
                while c > -1 and p1[row][c] == 2:
                    p1[row][c] = 3
                    c -= 1
            elif row > 1 and p1[row][col] == 1 and p1[row - 1][col] in [2, 3]:
                p1[row][col] = 3
                r = row
                while r < rows - 1 and p1[r + 1][col] == 1:
                    p1[r + 1][col] = 3
                    r += 1
            elif row < rows - 1 and p1[row][col] == 1 and p1[row + 1][col] in [2, 3]:
                p1[row][col] = 3
                r = row - 1
                while r > -1 and p1[r][col] == 1:
                    p1[r][col] = 3
                    r -= 1
            col += 1
        row += 1
    return p1, p2

def getNextOptions (grid: np.array, row: int, col: int, num: int):
    '''
    return list of all possible moves
    '''
    ret = []
    if row + nbr['N'][0] >= 0 and grid[row + nbr['N'][0]][col + nbr['N'][1]] == num:
        ret.append('N')
    if col + nbr['E'][1] < len(grid[row]) and grid[row + nbr['E'][0]][col + nbr['E'][1]] == num:
        ret.append('E')
    if row + nbr['S'][0] < len(grid) and grid[row + nbr['S'][0]][col + nbr['S'][1]] == num:
        ret.append('S')
    if col + nbr['W'][1] >= 0 and grid[row + nbr['W'][0]][col + nbr['W'][1]] == num:
        ret.append('W')
    return ret

def getBorderNext (grid: np.array, row: int, col: int, dir: str, num: int):
    '''
    get next move such that you move through the outline of the shape until
    there are no more moves to make
    '''
    options = getNextOptions(grid, row, col, num)
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

def getSnakeNext (grid: np.array, row: int, col: int, dir: str, num: int, temp: list):
    '''
    get next move such that you move through all coordinates outlining and
    within the shape until there are no more moves to make
    '''
    options = getNextOptions(grid, row, col, num)
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

def getShape (grid: np.array, row: int, col: int):
    '''
    get coordinates of corners in shape that starts with the given coordinate
    '''
    # get coordinates
    num = grid[row][col]
    shape, dir = [[row, col]], 'E'
    row, col, dir, turn = getBorderNext(grid, row, col, dir, num)
    while [row, col] != shape[0] and grid[row, col] == num:
        r, c, d, turn = getBorderNext(grid, row, col, dir, num)
        if turn: shape.append([row, col])
        row, col, dir = r, c, d
    if [row, col] == shape[0]: shape.append([row, col])

    # remove shape from grid
    row, col, dir, temp = shape[0][0], shape[0][1], 'E', []
    while grid[row][col] == num:
        grid[row][col] = 0
        # if row > 87 and col > 37:
        #     printPlan(4, "test.txt", grid)
        #     time.sleep(.2)
        row, col, dir, temp = getSnakeNext(grid, row, col, dir, num, temp)
        if dir == 'Done':
            if temp: row, col, dir = temp[0][0], temp[0][1], 'E'
            else: break
        if [row, col] in temp: temp.remove([row, col])
    return grid, shape, num

def getComponent (info: dict, name: str, rows: int, cols: int, grid: np.array, p3: np.array):
    '''
    find and add shape information to info based on component type
    '''
    for row in range(rows):
        for col in range(cols):
            if grid[row][col]:
                grid, shape, orientation = getShape(grid, row, col) # get shape coordinates
                if name == 'Rooms': location = 2
                else: location = p3[row][col]
                # print(orientation in info[location][name], location, name, orientation, shape)
                if orientation in info[location][name]: info[location][name][orientation].append(shape)
                else: info[location][name][int(orientation)] = [shape]
    return info

def getInfo (rows: int, cols: int, p1: np.array, p2: np.array, p3: np.array):
    '''
    find and return wall, door, and room information
    '''
    info = {
        1: {'Walls': {}, 'Doors': {}},
        2: {'Walls': {}, 'Doors': {}, 'Rooms': {}}
    }
    doors = np.zeros((rows, cols), dtype = np.uint8)
    rooms = np.zeros((rows, cols), dtype = np.uint8)
    for row in range(rows):
        for col in range(cols):
            if p1[row][col] in [3, 4] and p2[row][col] != 3:
                doors[row][col] = p2[row][col]
            if p3[row][col] == 3: rooms[row][col] = p1[row][col]
    getComponent(info, 'Walls', rows, cols, np.copy(p2), p3)
    getComponent(info, 'Doors', rows, cols, doors, p3)
    getComponent(info, 'Rooms', rows, cols, rooms, p3)
    return info

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