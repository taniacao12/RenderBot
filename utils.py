import numpy as np
from skimage import measure, feature, segmentation
from scipy import stats, ndimage

from door import Door
from room import Room

oppositeDir = {
    'I': 'O', 'O': 'I', 'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E',
    'NE': 'SW', 'NW': 'SE', 'SE': 'NW', 'SW': 'NE'
}

programs = {
    13: 0, 14: 1, 15: 2, 16: 3, 17: 4, 2: 5, 3: 6, 4: 7, 1: 8,
    5: 9, 6: 10, 7: 11, 8: 12, 0: 13, 9: 14, 10: 15, 11: 16, 12: 17
}

def getMask (array, criteria) -> np.array:
    mask = array == criteria
    region = measure.regionprops(mask.astype(int))[0]
    return np.array(region.bbox)

def getChannels (image) -> np.array:
    """
    gets the plan's mask from all 4 image channel
    """
    c0 = image[..., 0] # boundary
    c1 = image[..., 1] # program
    c2 = image[..., 2] # instance
    c3 = image[..., 3] # inside
    y0, x0, y1, x1 = getMask(c0, 127)
    return c0[y0:y1, x0:x1], c1[y0:y1, x0:x1], c2[y0:y1, x0:x1], c3[y0:y1, x0:x1]

def getFrontDoor (boundary, instance, rooms) -> Door:
    """
    gets the front door's mask
    """
    y0, x0, y1, x1 = getMask(boundary, 255)
    door = Door(y0, y1, x0, x1, 0, True)
    id = nbrs(instance, door)
    room = [room for room in rooms if room.getID() == id[0]][0]
    door.addRoom(room)
    return door

def getInteriorDoors (program) -> list:
    """
    gets the interior door's masks
    return: list of interior doors
    """
    mask = (program == 17).astype(np.uint8)
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

def collides (bbox1, bbox2, th = 0) -> bool:
    """
    determines whether or not two boxes collide with each other
    :param bbox1: bounds of box 1 (y0, y1, x0, x1)
    :param bbox2: bounds of box 2 (y0, y1, x0, x1)
    :param th: optional margin to add to the boxes (default 0)
    :return: True/False depending if boxes collide
    """
    return not(
        (bbox1[0] - th > bbox2[1]) or
        (bbox1[1] + th < bbox2[0]) or
        (bbox1[2] - th > bbox2[3]) or
        (bbox1[3] + th < bbox2[2])
    )

def pointBoxRelation (coor, box) -> str:
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

def doorRoomRelation (door, box) -> str:
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

def nbrs (instance, door):
    y0, y1, x0, x1 = door.getBounds()
    values = set()
    if door.getLength() > door.getWidth():
        for y in range(y0, y1):
            values.add(instance[y][x0 - 1])
            values.add(instance[y][x1 + 1])
    else:
        for x in range(x0, x1):
            values.add(instance[y0 - 1][x])
            values.add(instance[y1 + 1][x])
    return [value for value in values if value != 0]

def getRooms (program, instance, doors) -> list:
    """
    gets the rooms' masks and attributes
    return: list of rooms
    """
    rooms = []
    regions = measure.regionprops(instance)
    for region in regions:
        value = stats.mode(program[region.coords[:, 0],
                                region.coords[:, 1]],
                                axis=None,
                                keepdims=True)[0][0]
        id = stats.mode(instance[region.coords[:, 0],
                                region.coords[:, 1]],
                                axis=None,
                                keepdims=True)[0][0]
        y0, x0, y1, x1 = np.array(region.bbox)
        rooms.append(Room(y0, y1, x0, x1, id, programs[value]))
    
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
        id = nbrs(instance, door)
        room1 = [room for room in rooms if room.getID() == id[0]][0]
        room2 = [room for room in rooms if room.getID() == id[1]][0]
        room1.addDoor(door, doorRoomRelation(door, room2), room2)
        room2.addDoor(door, doorRoomRelation(door, room1), room1)
        door.addRoom(room1)
        door.addRoom(room2)
    return rooms

            