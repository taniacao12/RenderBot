# scaleFactor = 1 / 4 # 4 pixels is equivalent to 1 foot
scaleFactor = 3 # 1 pixel is equivalent to 3 inches

nbr = {
    'N': (-1,  0),
    'S': ( 1,  0),
    'W': ( 0, -1),
    'E': ( 0,  1),
}

checkDir = {
    'N': 'W',
    'S': 'E',
    'W': 'S',
    'E': 'N',
}

oppositeDir = {
     'I':  'O',  'O':  'I',
     'N':  'S',  'S':  'N',
     'E':  'W',  'W':  'E',
    'NE': 'SW', 'NW': 'SE',
    'SE': 'NW', 'SW': 'NE',
}

c0_code = {
    0:   0, # exterior area
    127: 1, # exterior wall
    255: 2, # egress door
}

c2_code = {
    0: 0, # exterior area
    # rooms are numbered 1 to N
}

c3_code = {
    0:   0, # exterior area
    255: 1, # interior area
}

program_code = {
    # boundary
    13:  0, # exterior area
    14:  1, # exterior wall
    16:  2, # interior wall
    15:  3, # exterior door
    17:  4, # interior door
    # common spaces (core)
    3:   5, # bathroom
    2:   6, # kitchen
    4:   7, # dining room
    0:   8, # living room
    10:  9, # entrance
    9:  10, # balcony
    # common spaces (additional)
    6:  11, # study room
    11: 12, # storage
    12: 13, # walk-in storage
    # bedrooms
    1:  14, # master room
    5:  15, # child room
    7:  16, # second room
    8:  17, # guest room   
}

color_code = {
    # boundary
    0:  [255, 255, 255], # exterior area
    1:  [ 68,  77,  58], # exterior wall
    2:  [ 68,  77,  58], # interior wall
    3:  [212, 180, 141], # exterior door
    4:  [212, 180, 141], # interior door
    # common spaces (core)
    5:  [235, 156, 151], # bathroom
    6:  [189,  85,  86], # kitchen
    7:  [214, 138, 112], # dining room
    8:  [240, 224, 156], # living room
    9:  [116, 202, 187], # entrance
    10: [123, 180, 163], # balcony
    # common spaces (additional)
    11: [ 91, 113,  74], # study room
    12: [137, 151, 124], # storage
    13: [190, 198, 182], # walk-in storage
    # bedrooms
    14: [ 61,  94, 137], # master room
    15: [ 96, 126, 173], # child room
    16: [153, 152, 194], # second room
    17: [ 76,  79, 110], # guest room
}

program_desc = {
    0:  ["External Area",   "Exterior"],
    1:  ["Exterior Wall",   "Wall"],
    3:  ["Interior Wall",   "Wall"],
    2:  ["Exterior Door",   "Door"],
    4:  ["Interior Door",   "Door"],
    5:  ["Bathroom",        "Common Area"],
    6:  ["Kitchen",         "Common Area"],
    7:  ["Dining Room",     "Common Area"],
    8:  ["Living Room",     "Common Area"],
    9:  ["Entrance",        "Common Area"],
    10: ["Balcony",         "Common Area"],
    11: ["Study Room",      "Office"],
    12: ["Storage",         "Storage"],    
    13: ["Walk-In Storage", "Storage"],
    14: ["Master Room",     "Bedroom"],
    15: ["Child Room",      "Bedroom"],
    16: ["Second Room",     "Bedroom"],
    17: ["Guest Room",      "Bedroom"],
}

location = {
    1: 'External',
    2: 'Internal'
}

orientation = {
    1: 'Horizontal',
    2: 'Vertical',
    3: 'Corner'
}