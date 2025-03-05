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

def getNextOptions (grid: np.array, row: int, col: int, value):
    '''
    return list of all possible moves
    '''
    ret = []
    if row + nbr['N'][0] >= 0 and grid[row + nbr['N'][0]][col + nbr['N'][1]] == value:
        ret.append('N')
    if col + nbr['E'][1] < len(grid[row]) and grid[row + nbr['E'][0]][col + nbr['E'][1]] == value:
        ret.append('E')
    if row + nbr['S'][0] < len(grid) and grid[row + nbr['S'][0]][col + nbr['S'][1]] == value:
        ret.append('S')
    if col + nbr['W'][1] >= 0 and grid[row + nbr['W'][0]][col + nbr['W'][1]] == value:
        ret.append('W')
    return ret

def getBorderNext (row: int, col: int, dir: str, options: list):
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

def getSnakeNext (row: int, col: int, dir: str, options: list, storage: list):
    '''
    get next move such that you move through all coordinates outlining and
    within the shape until there are no more moves to make
    '''
    if not options: return row, col, 'Done', storage
    N = [row + nbr['N'][0], col + nbr['N'][1]]
    S = [row + nbr['S'][0], col + nbr['S'][1]]
    E = [row + nbr['E'][0], col + nbr['E'][1]]
    W = [row + nbr['W'][0], col + nbr['W'][1]]
    retR, retC, retD = None, None, None
    if dir == 'E':
        if 'N' in options: retR, retC, retD = N[0], N[1], 'N'
        if 'E' in options:
            if not retD: retR, retC, retD = E[0], E[1], 'E'
            elif E not in storage: storage.append(E)
        if 'S' in options:
            if not retD: retR, retC, retD = S[0], S[1], 'S'
            elif S not in storage: storage.append(S)
        if 'W' in options:
            if not retD: retR, retC, retD = W[0], W[1], 'W'
            elif W not in storage: storage.append(W)
        return retR, retC, retD, storage
    elif dir == 'N':
        if 'N' in options: retR, retC, retD = N[0], N[1], 'N'
        if 'W' in options:
            if not retD: retR, retC, retD = W[0], W[1], 'W'
            elif W not in storage: storage.append(W)
        if 'E' in options:
            if not retD: retR, retC, retD = E[0], E[1], 'E'
            elif E not in storage: storage.append(E)
        return retR, retC, retD, storage
    elif dir == 'W':
        if 'N' in options: retR, retC, retD = N[0], N[1], 'N'
        if 'W' in options:
            if not retD: retR, retC, retD = W[0], W[1], 'W'
            elif W not in storage: storage.append(W)
        if 'S' in options:
            if not retD: retR, retC, retD = S[0], S[1], 'S'
            elif S not in storage: storage.append(S)
        return retR, retC, retD, storage
    elif dir == 'S':
        if 'W' in options: retR, retC, retD = W[0], W[1], 'W'
        if 'E' in options:
            if not retD: retR, retC, retD = E[0], E[1], 'E'
            elif E not in storage: storage.append(E)
        if 'S' in options:
            if not retD: retR, retC, retD = S[0], S[1], 'S'
            elif S not in storage: storage.append(S)
        return retR, retC, retD, storage

def getCoors (plan: np.array, grid: np.array, row: int, col: int, id: str):
    '''
    get coordinates of feature, add it to plan, and remove it from grid
    '''
    value = grid[row][col]
    coors, dir = [[row, col]], 'E'
    row, col, dir, turn = getBorderNext(row, col, dir, getNextOptions(grid, row, col, value))
    while [row, col] != coors[0] and grid[row, col] == value:
        r, c, d, turn = getBorderNext(row, col, dir, getNextOptions(grid, row, col, value))
        if turn: coors.append([row, col])
        row, col, dir = r, c, d
    if [row, col] == coors[0]: coors.append([row, col])

    row, col, dir, storage = coors[0][0], coors[0][1], 'E', []
    while grid[row][col] == value:
        grid[row][col] = ''
        plan[row][col] = id
        # if row > 87 and col > 37:
        #     printPlan(4, "test.txt", grid)
        #     time.sleep(.2)
        row, col, dir, storage = getSnakeNext(row, col, dir, getNextOptions(grid, row, col, value), storage)
        if dir == 'Done':
            if storage: row, col, dir = storage[0][0], storage[0][1], 'E'
            else: break
        if [row, col] in storage: storage.remove([row, col])
    return plan, grid, coors

def getFeature (plan: np.array, info: dict, featureType: str, rows: int, cols: int, grid: np.array, p3: np.array):
    '''
    find and add shape information to info based on component type
    '''
    if featureType not in info: info[featureType] = {}
    for row in range(rows):
        for col in range(cols):
            value = grid[row][col]
            if value:
                count = len(info[featureType]) + 1
                if featureType == 'Rooms':
                    programID = program_desc[int(value)][0]
                    program = program_desc[int(value)][1]
                    id = '{}{:02}-{}'.format(featureType[0], count, programID)
                    plan, grid, coors = getCoors(plan, grid, row, col, id)
                    info[featureType][id] = {
                        'Program': program,
                        'Coordinates': coors
                    }
                else:
                    loc = p3[row][col]
                    if loc == 'External' and featureType == 'Walls': num = 1
                    elif loc == 'External' and featureType == 'Doors': num = 2
                    elif loc == 'Internal' and featureType == 'Walls': num = 3
                    elif loc == 'Internal' and featureType == 'Doors': num = 4
                    programID = program_desc[num][0]
                    program = program_desc[num][1]
                    id = '{}{:02}-{}'.format(featureType[0], count, programID)
                    plan, grid, coors = getCoors(plan, grid, row, col, id)
                    info[featureType][id] = {
                        'Program': program,
                        'Orientation': value,
                        'Coordinates': coors
                    }                    
                # printJSON('0', info)
    return plan, info

def getFeatures (rows: int, cols: int, p1: np.array, p2: np.array, p3: np.array):
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

    plan, info = getFeature(plan, {}, 'Walls', rows, cols, np.copy(p2), p3)
    plan, info = getFeature(plan, info, 'Doors', rows, cols, doors, p3)
    plan, info = getFeature(plan, info, 'Rooms', rows, cols, rooms, p3)
    return plan, info

def getNbrs (coors: list, plan: np.array, rows: int, cols: int, orientation: str):
    up = coors[0][0]
    down, left, right = None, None, None
    for coor in coors:
        if down == None or down < coor[0]: down = coor[0]
        if left == None or left > coor[1]: left = coor[1]
        if right == None or right < coor[1]: right = coor[1]
    midH = int((left + right) // 2)
    midV = int((up + down) // 2)
    if up == 0: up = ''
    else: up = plan[up - 1][midH]
    if down == rows - 1: down = ''
    else: down = plan[down + 1][midH]
    if left == 0: left = ''
    else: left = plan[midV][left - 1]
    if right == cols - 1: right = ''
    else: right = plan[midV][right + 1]
    return up, down, left, right

def addRoomRelations (info: dict, roomID: str, featureID: str, dir: str):
    '''
    find and add room relations to info
    '''
    # find room
    for id in info['Rooms']:
        if id == roomID:
            room = info['Rooms'][id]
            break
    # add compenent to room relations
    if featureID[0] == 'W': relationName = 'Wall Relations'
    elif featureID[0] == 'D': relationName = 'Door Relations'
    if relationName not in room: room[relationName] = {dir: []}
    if dir not in room[relationName]: room[relationName][dir] = []
    room[relationName][dir].append(featureID)
    return info

def getRelations (plan: np.array, info: dict, rows: int, cols: int):
    '''
    add information on connections between components
    '''
    for featureType in ['Walls', 'Doors']:
        for featureID in info[featureType]:
            orientation = info[featureType][featureID]['Orientation']
            if orientation != 'Corner':
                feature = info[featureType][featureID]
                coors = feature['Coordinates']
                feature['Room Relations'] = {}
                up, down, left, right = getNbrs(coors, plan, rows, cols, orientation)
                if orientation == 'Horizontal':
                    if left and left[0] == 'R' and right and right[0] == 'R':
                        if left != right: raise ValueError("error in line 291")
                        feature['Room Relations']['I'] = left
                        info = addRoomRelations(info, left, featureID, 'O')
                    elif left and left[0] == 'R':
                        feature['Room Relations']['W'] = left
                        info = addRoomRelations(info, left, featureID, 'E')
                    elif right and right[0] == 'R':
                        feature['Room Relations']['E'] = right
                        info = addRoomRelations(info, right, featureID, 'W')
                    else:
                        if up:
                            feature['Room Relations']['N'] = up
                            info = addRoomRelations(info, up, featureID, 'S')
                        if down:
                            feature['Room Relations']['S'] = down
                            info = addRoomRelations(info, down, featureID, 'N')
                elif orientation == 'Vertical':
                    if up and up[0] == 'R' and down and down[0] == 'R':
                        if up != down: raise ValueError("error in line 330")
                        feature['Room Relations']['I'] = up
                        info = addRoomRelations(info, up, featureID, 'O')
                    elif up and up[0] == 'R':
                        feature['Room Relations']['N'] = up
                        info = addRoomRelations(info, up, featureID, 'S')
                    elif down and down[0] == 'R':
                        feature['Room Relations']['S'] = down
                        info = addRoomRelations(info, down, featureID, 'N')
                    else:
                        if left:
                            feature['Room Relations']['W'] = left
                            info = addRoomRelations(info, left, featureID, 'E')
                        if right:
                            feature['Room Relations']['E'] = right
                            info = addRoomRelations(info, right, featureID, 'W')
    return plan, info

def getInfo (rows: int, cols: int, p1: np.array, p2: np.array, p3: np.array):
    '''
    find and return information on floor plan
    '''
    plan, info = getFeatures(rows, cols, p1, p2, p3)
    return getRelations(plan, info, rows, cols)