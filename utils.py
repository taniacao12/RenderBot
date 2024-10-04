import numpy as np
from skimage import measure, feature, segmentation
from scipy import stats, ndimage

from door import Door
from room import Room

color = {
    (245, 245, 245): 0,  # external area
    ( 50,  50,  50): 1,  # exterior wall
    (100, 100, 100): 2,  # front door
    (150, 150, 150): 3,  # interior wall
    (200, 200, 200): 4,  # interior door
    (255,  69,  69): 5,  # kitchen
    (255, 165,   0): 6,  # bathroom
    (255, 255,   0): 7,  # dining room
    (  0,   0, 128): 8,  # master room
    ( 65, 105, 225): 9,  # child room
    (  0,   0, 205): 10, # study room
    (135, 206, 235): 11, # second room
    (173, 216, 230): 12, # guest room
    (  0, 128,   0): 13, # living room
    (  0, 128, 128): 14, # balcony
    (128,   0, 128): 15, # entrance
    (255, 182, 193): 16, # storage
    (139,  69,  19): 17  # wall-in
}

oppositeDir = {
    'I': 'O', 'O': 'I', 'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E',
    'NE': 'SW', 'NW': 'SE', 'SE': 'NW', 'SW': 'NE'
}

def getMask (array: np.array, criteria: int) -> np.array:
    mask = array == criteria
    region = measure.regionprops(mask.astype(int))[0]
    return np.array(region.bbox)

def getData (image: np.array) -> tuple[np.array, np.array]:
    """
    dets the plan's image channgels
    """
    colors = image[..., :3]
    program = np.array([[color[tuple(col)] for col in row] for row in colors], dtype=np.uint8)
    rooms  = np.array([[255 - col for col in row] for row in image[..., 3]], dtype=np.uint8)
    return program, rooms

def getFrontDoor (c0: np.array, c1: np.array, rooms: list[Room]) -> Door:
    """
    gets the front door's mask
    """
    y0, x0, y1, x1 = getMask(c0, 2)
    door = Door(y0, y1, x0, x1, 0, True)
    id = nbrs(c1, door)
    room = [room for room in rooms if room.getID() == id[0]][0]
    door.addRoom(room)
    return door

def getInteriorDoors (c0: np.array) -> list[Door]:
    """
    gets the interior door's masks
    return: list of interior Door objects
    """
    mask = (c0 == 4).astype(np.uint8)
    distance = ndimage.morphology.distance_transform_cdt(mask)
    local_maxi = (distance > 1).astype(np.uint8)
    corner_measurement = feature.corner_harris(local_maxi)
    local_maxi[corner_measurement > 0] = 0
    markers = measure.label(local_maxi)
    labels = segmentation.watershed(-distance, markers, mask=mask, connectivity=8)
    regions = measure.regionprops(labels)

    interiorDoors = []
    for region in regions:
        y0, x0, y1, x1 = np.array(region.bbox)
        door = Door(y0, y1, x0, x1, len(interiorDoors) + 1, False)
        interiorDoors.append(door)
    return interiorDoors

def collides (bbox1: tuple[int, int, int, int], bbox2: tuple[int, int, int, int], th: int = 0) -> bool:
    """
    determine if two bounding boxes collide
    :param bbox1: bounds of box 1 (y0, y1, x0, x1)
    :param bbox2: bounds of box 2 (y0, y1, x0, x1)
    :param th: optional margin to add to the boxes (default 0)
    :return: True if boxes collide, False otherwise
    """
    return not(
        (bbox1[0] - th > bbox2[1]) or
        (bbox1[1] + th < bbox2[0]) or
        (bbox1[2] - th > bbox2[3]) or
        (bbox1[3] + th < bbox2[2])
    )

def pointBoxRelation (coor: tuple[int, int], box: tuple[int, int, int, int]) -> str:
    """
    finds the relation of the coor to the box
     NW  N  NE
        ---
     W | I | E
        ---
     SW  S  SE
     O for surrounding
    """
    y, x = coor
    y0, y1, x0, x1 = box
    if (x < x0 and y <= y0) or (x == x0 and y == y0):
        return 'NW'
    elif x0 <= x < x1 and y <= y0:
        return 'N'
    elif (x1 <= x and y < y0) or (x == x1 and y == y0):
        return 'NE'
    elif x <= x0 and y0 < y <= y1:
        return 'W'
    elif x0 < x < x1 and y0 < y < y1:
        return 'I'
    elif x1 <= x and y0 <= y < y1:
        return 'E'
    elif (x <= x0 and y1 < y) or (x == x0 and y == y1):
        return 'SW'
    elif x0 < x <= x1 and y1 <= y:
        return 'S'
    elif (x1 < x and y1 <= y) or (x == x1 and y == y1):
        return 'SE'
    else: return None

def doorRoomRelation (door: Door, box: Room) -> str:
    """
    finds the relation of the door to the box
        NW N NE
        -------
     WN|       | EN
     W |       | E
     WS|       | ES
        -------
        SW S SE
    """
    y0, y1, x0, x1 = box.getBounds()
    yc, xc = box.getCentroid()
    y, x = door.getCentroid()
    if x == xc and y < yc: return 'N'
    elif x == xc and y > yc: return 'S'
    elif y == yc and x < xc: return 'W'
    elif y == yc and x > xc: return 'E'
    elif x0 < x < xc:
        if y < yc: return 'NW'
        else: return 'SW'
    elif xc < x < x1:
        if y < yc: return 'NE'
        else: return 'SE'
    elif y0 < y < yc:
        if x < xc: return 'WN'
        else: return 'EN'
    elif yc < y < y1:
        if x < xc: return 'WS'
        else: return 'ES'
    else: return None

def nbrs (c1: np.array, door: Door) -> list[int]:
    y0, y1, x0, x1 = door.getBounds()
    values = set()
    if door.getLength() > door.getWidth():
        for y in range(y0, y1):
            values.add(c1[y][x0 - 1])
            values.add(c1[y][x1 + 1])
    else:
        for x in range(x0, x1):
            values.add(c1[y0 - 1][x])
            values.add(c1[y1 + 1][x])
    return [int(value) for value in values if value != 0]

def getRooms (c0: np.array, c1: np.array, doors: list[Door]) -> list[Room]:
    """
    gets the rooms' masks and attributes
    return: list of rooms
    """
    rooms = []
    regions = measure.regionprops(c1)
    for region in regions:
        value = stats.mode(c0[region.coords[:, 0],
                                region.coords[:, 1]],
                                axis=None,
                                keepdims=True)[0][0]
        id = stats.mode(c1[region.coords[:, 0],
                                region.coords[:, 1]],
                                axis=None,
                                keepdims=True)[0][0]
        y0, x0, y1, x1 = np.array(region.bbox)
        rooms.append(Room(y0, y1, x0, x1, id, value))
    
    # find relations between rooms
    for u in range(len(rooms)):
        for v in range(u + 1, len(rooms)):
            # check if two rooms are connected
            if not collides(rooms[u].getBounds(), rooms[v].getBounds(), 9):
                continue # rooms are not connected
            # if they are, check the spatial relation between them
            uy0, uy1, ux0, ux1 = rooms[u].getBounds()
            vy0, vy1, vx0, vx1 = rooms[v].getBounds()
            if ux0 < vx0 and ux1 > vx1 and uy0 < vy0 and uy1 > vy1:
                relation = 'O' # room u surrounds room v
            elif ux0 >= vx0 and ux1 <= vx1 and uy0 >= vy0 and uy1 <= vy1:
                relation = 'I' # room u is inside room v
            else: relation = pointBoxRelation(rooms[u].getCentroid(), rooms[v].getBounds())
            rooms[u].addRelation(oppositeDir[relation], rooms[v])
            rooms[v].addRelation(relation, rooms[u])

    # find relations between doors and rooms
    for door in doors:
        id = nbrs(c1, door)
        room1 = [room for room in rooms if room.getID() == id[0]][0]
        room2 = [room for room in rooms if room.getID() == id[1]][0]
        room1.addDoor(door, doorRoomRelation(door, room2), room2)
        room2.addDoor(door, doorRoomRelation(door, room1), room1)
        door.addRoom(room1)
        door.addRoom(room2)
    return rooms

            