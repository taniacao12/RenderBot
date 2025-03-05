# scaleFactor = 1 / 4 # 4 pixels is equivalent to 1 foot
scaleFactor = 3 # 1 pixel is equivalent to 3 inches

nbr = {
    'N': (-1,  0),
    'S': ( 1,  0),
    'W': ( 0, -1),
    'E': ( 0,  1),
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
    6:  11, # office
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
    11: [ 91, 113,  74], # office
    12: [137, 151, 124], # storage
    13: [190, 198, 182], # walk-in storage
    # bedrooms
    14: [ 61,  94, 137], # master room
    15: [ 96, 126, 173], # child room
    16: [153, 152, 194], # second room
    17: [ 76,  79, 110], # guest room
}

program_desc = {
    0:  ["EA", "External Area"],
    1:  ["EW", "Exterior Wall"],
    2:  ["ED", "Exterior Door"],
    3:  ["IW", "Interior Wall"],
    4:  ["ID", "Interior Door"],
    5:  ["BA", "Bathroom"],
    6:  ["KT", "Kitchen"],
    7:  ["DR", "Dining Room"],
    8:  ["LR", "Living Room"],
    9:  ["EN", "Entrance"],
    10: ["BL", "Balcony"],
    11: ["OF", "Office"],
    12: ["ST", "Storage"],    
    13: ["ST", "Storage"],
    14: ["BR", "Bedroom"],
    15: ["BR", "Bedroom"],
    16: ["BR", "Bedroom"],
    17: ["BR", "Bedroom"],
    # 13: ["WI", "Walk-In Storage"],
    # 14: ["MR", "Master Room"],
    # 15: ["CR", "Child Room"],
    # 16: ["SR", "Second Room"],
    # 17: ["GR", "Guest Room"],
}