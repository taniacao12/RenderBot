import numpy as np

from legend import nbr, program_desc
from utils.file_utils import printPlan, printJSON

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
    orientations = np.zeros((rows, cols), dtype = 'U10')
    boundary = np.zeros((rows, cols), dtype = 'U10')
    for row in range(rows):
        for col in range(cols):
            if program[row][col] in [1, 2, 3, 4]:
                x = getX(program, row, col)
                y = getY(program, row, col)
                if x > y: orientations[row][col] = 'Horizontal'
                elif x < y: orientations[row][col] = 'Vertical'
                else: orientations[row][col] = 'Corner'
                if program[row][col] % 2: boundary[row][col] = 'External'
                else: boundary[row][col] = 'Internal'
            elif program[row][col] >= 5: boundary[row][col] = 'Rooms'
    # printPlan(2, "test.txt", orientations)

    # convert all interconnecting parts into corners
    for row in range(rows):
        for col in range(cols):
            if col > 1 and orientations[row][col] == 'Vertical' and orientations[row][col - 1] in ['Horizontal', 'Corner']:
                orientations[row][col] = 'Corner'
                while col < cols - 1 and orientations[row][col + 1] == 'Vertical':
                    orientations[row][col + 1] = 'Corner'
                    col += 1
            elif col < cols - 1 and orientations[row][col] == 'Vertical' and orientations[row][col + 1] in ['Horizontal', 'Corner']:
                orientations[row][col] = 'Corner'
                c = col - 1
                while c > -1 and orientations[row][c] == 'Vertical':
                    orientations[row][c] = 'Corner'
                    c -= 1
            elif row > 1 and orientations[row][col] == 'Horizontal' and orientations[row - 1][col] in ['Vertical', 'Corner']:
                orientations[row][col] = 'Corner'
                r = row
                while r < rows - 1 and orientations[r + 1][col] == 'Horizontal':
                    orientations[r + 1][col] = 'Corner'
                    r += 1
            elif row < rows - 1 and orientations[row][col] == 'Horizontal' and orientations[row + 1][col] in ['Vertical', 'Corner']:
                orientations[row][col] = 'Corner'
                r = row - 1
                while r > -1 and orientations[r][col] == 'Horizontal':
                    orientations[r][col] = 'Corner'
                    r -= 1
    return orientations, boundary

def getNextOptions (grid: np.array, row: int, col: int, criteria):
    '''
    return list of all possible moves
    '''
    ret = []
    if row + nbr['N'][0] >= 0 and grid[row + nbr['N'][0]][col + nbr['N'][1]] == criteria:
        ret.append('N')
    if col + nbr['E'][1] < len(grid[row]) and grid[row + nbr['E'][0]][col + nbr['E'][1]] == criteria:
        ret.append('E')
    if row + nbr['S'][0] < len(grid) and grid[row + nbr['S'][0]][col + nbr['S'][1]] == criteria:
        ret.append('S')
    if col + nbr['W'][1] >= 0 and grid[row + nbr['W'][0]][col + nbr['W'][1]] == criteria:
        ret.append('W')
    return ret

def getBorderNext (grid: np.array, row: int, col: int, dir: str, options: list):
    '''
    get next move such that you move through the outline of the shape until
    there are no more moves to make
    '''
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

def getSnakeNext (grid: np.array, row: int, col: int, dir: str, options: list, temp: list):
    '''
    get next move such that you move through all coordinates outlining and
    within the shape until there are no more moves to make
    '''
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

def getShape (grid: np.array, plan: np.array, info: dict, loc: str, name: str, row: int, col: int):
    '''
    get coordinates of corners in shape that starts with the given coordinate
    '''
    # get coordinates
    category = grid[row][col]
    coors, dir = [[row, col]], 'E'
    row, col, dir, turn = getBorderNext(grid, row, col, dir, getNextOptions(grid, row, col, category))
    while [row, col] != coors[0] and grid[row, col] == category:
        r, c, d, turn = getBorderNext(grid, row, col, dir, getNextOptions(grid, row, col, category))
        if turn: coors.append([row, col])
        row, col, dir = r, c, d
    if [row, col] == coors[0]: coors.append([row, col])

    # add shape to components
    if loc not in info: info[loc] = {name: {}}
    if name not in info[loc]: info[loc][name] = {}
    if name == 'Rooms':
        programID = program_desc[int(category)][0]
        program = program_desc[int(category)][1]
        if program not in info[loc][name]:
            id = '{}{}{}01'.format(loc[0], name[0], programID)
            info[loc][name][program] = {id: {'Coordinates': coors}}
        else:
            count = len(info[loc][name][program]) + 1
            id = '{}{}{}{:02}'.format(loc[0], name[0], programID, count)
            info[loc][name][program][id] = {'Coordinates': coors}
    elif category not in info[loc][name]:
        id = '{}{}{}01'.format(loc[0], name[0], category[0])
        info[loc][name][category] = {id: {'Coordinates': coors}}
    else:
        count = len(info[loc][name][category]) + 1
        id = '{}{}{}{:02}'.format(loc[0], name[0], category[0], count)
        info[loc][name][category][id] = {'Coordinates': coors}

    # remove shape from grid and add to plan
    row, col, dir, temp = coors[0][0], coors[0][1], 'E', []
    while grid[row][col] == category:
        grid[row][col] = ''
        plan[row][col] = id
        # if row > 87 and col > 37:
        #     printPlan(4, "test.txt", grid)
        #     time.sleep(.2)
        row, col, dir, temp = getSnakeNext(grid, row, col, dir, getNextOptions(grid, row, col, category), temp)
        if dir == 'Done':
            if temp: row, col, dir = temp[0][0], temp[0][1], 'E'
            else: break
        if [row, col] in temp: temp.remove([row, col])
    return grid, plan, info

def getComponent (plan: np.array, info: dict, name: str, rows: int, cols: int, grid: np.array, p3: np.array):
    '''
    find and add shape information to info based on component type
    '''
    for row in range(rows):
        for col in range(cols):
            if grid[row][col]:
                loc = p3[row][col]
                if loc == 'Rooms': loc = 'Internal'
                grid, plan, info = getShape(grid, plan, info, loc, name, row, col)
                # printJSON('0', info)
    return plan, info

def getComponents (rows: int, cols: int, p1: np.array, p2: np.array, p3: np.array):
    '''
    find and return wall, door, and room information
    '''
    plan = np.zeros((rows, cols), dtype = 'U6')
    doors = np.zeros((rows, cols), dtype = 'U10')
    rooms = np.zeros((rows, cols), dtype = 'U2')
    for row in range(rows):
        for col in range(cols):
            if p1[row][col] in [3, 4] and p2[row][col] != 'Corner':
                doors[row][col] = p2[row][col]
            if p3[row][col] == 'Rooms':
                rooms[row][col] = p1[row][col]
    # printPlan(2, "test.txt", doors)
    # printPlan(1, "test.txt", rooms)

    plan, info = getComponent(plan, {}, 'Walls', rows, cols, np.copy(p2), p3)
    plan, info = getComponent(plan, info, 'Doors', rows, cols, doors, p3)
    plan, info = getComponent(plan, info, 'Rooms', rows, cols, rooms, p3)
    return plan, info

def addRoomRelations (info: dict, roomID: str, nameID: str, dir: str):
    '''
    find and add room relations to info
    '''
    # find room
    for loc in info:
        if loc[0] == roomID[0]:
            for name in info[loc]:
                if name[0] == roomID[1]:
                    for category in info[loc][name]:
                        if category[0] == roomID[2]:
                            for id in info[loc][name][category]:
                                if id == roomID:
                                    room = info[loc][name][category][id]
                                    break
    # add compenent to room relations
    if nameID[1] == 'D': relationName = 'Door Relations'
    elif nameID[1] == 'W': relationName = 'Wall Relations'
    if relationName not in room: room[relationName] = {dir: []}
    if dir not in room[relationName]: room[relationName][dir] = []
    room[relationName][dir].append(nameID)
    return info

def getRelations (info: dict, rows: int, cols: int, plan: np.array):
    '''
    add information on connections between components
    '''
    for loc in info:
        for name in ['Walls', 'Doors']:
            for category in info[loc][name]:
                if category != 'Corner':
                    for nameID in info[loc][name][category]:
                        shape = info[loc][name][category][nameID]
                        coors = shape['Coordinates']
                        shape['Room Relations'] = {}
                        if category == 'Horizontal':
                            mid = int((coors[1][1] + coors[0][1]) // 2)
                            if coors[0][0] > 1 and plan[coors[0][0] - 1][mid]:
                                roomID = plan[coors[0][0] - 1][mid]
                                shape['Room Relations']['N'] = roomID
                                info = addRoomRelations(info, roomID, nameID, 'S')
                            if coors[2][0] < rows - 1 and plan[coors[2][0] + 1][mid]:
                                roomID = plan[coors[2][0] + 1][mid]
                                shape['Room Relations']['S'] = roomID
                                info = addRoomRelations(info, roomID, nameID, 'N')
                        elif category == 'Vertical':
                            mid = int((coors[2][0] + coors[1][0]) // 2)
                            if coors[0][1] > 1 and plan[mid][coors[0][1] - 1]:
                                roomID = plan[mid][coors[0][1] - 1]
                                shape['Room Relations']['W'] = roomID
                                info = addRoomRelations(info, roomID, nameID, 'E')
                            if coors[1][1] < cols - 1 and plan[mid][coors[1][1] + 1]:
                                roomID = plan[mid][coors[1][1] + 1]
                                shape['Room Relations']['E'] = roomID
                                info = addRoomRelations(info, roomID, nameID, 'W')
    return info

def getInfo (rows: int, cols: int, p1: np.array, p2: np.array, p3: np.array):
    '''
    find and return information on floor plan
    '''
    plan, info = getComponents(rows, cols, p1, p2, p3)
    return getRelations(info, rows, cols, plan)