description = {
    0:  ["External Area", "External"],
    1:  ["Exterior Wall", "Exterior Wall"],
    2:  ["Front Door",    "Front Door"],
    3:  ["Interior Wall", "Interior Wall"],
    4:  ["Interior Door", "Interior Door"],
    5:  ["Kitchen",       "Function Area"],
    6:  ["Bathroom",      "Function Area"],
    7:  ["Dining Room",   "Function Area"],
    8:  ["Master Room",   "Bedroom"],
    9:  ["Child Room",    "Bedroom"],
    10: ["Study Room",    "Bedroom"],
    11: ["Second Room",   "Bedroom"], #?????????????
    12: ["Guest Room",    "Bedroom"],
    13: ["Living Room",   "Public Area"],
    14: ["Balcony",       "Public Area"],
    15: ["Entrance",      "Public Area"], #????????????
    16: ["Storage",       "Public Area"],    
    17: ["Wall-in",       "Public Area"], #?????????????
}

class Room:
    def __init__ (self, y0, y1, x0, x1, id, program):
        self.y0 = y0 # minRow
        self.y1 = y1 # maxRow
        self.x0 = x0 # minCol
        self.x1 = x1 # maxCol
        self.id = id
        self.program = program
        self.relations = {}
        self.doors = {}

    def getID (self):
        return self.id

    def getProgram (self):
        return self.program

    def getCategory (self):
        return description[self.program][0]
        
    def getType (self):
        return description[self.program][1]
    
    def getBounds (self):
        return self.y0, self.y1, self.x0, self.x1
    
    def getLength (self):
        return self.y1 - self.y0
    
    def getWidth (self):
        return self.x1 - self.x0
    
    def getArea (self):
        return self.getLength() * self.getWidth()
    
    def getCentroid (self):
        return (self.y0 + self.y1) / 2, (self.x0 + self.x1) / 2
    
    def getRelations (self):
        return self.relations
    
    def addRelation (self, relation, room):
        if relation in self.relations:
            self.relations[relation].append(room)
        else: self.relations[relation] = [room]
    
    def getDoors (self):
        return self.doors

    def addDoor (self, door, relation, room):
        self.doors[door] = (relation, room)
 
    def __str__(self):
        return self.id