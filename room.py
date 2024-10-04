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
        self.y0 = int(y0) # minRox
        self.y1 = int(y1) # maxRow
        self.x0 = int(x0) # minCol
        self.x1 = int(x1) # maxCol
        self.id = int(id)
        self.program = program
        self.relations = {}
        self.doors = {}

    def getID (self) -> int:
        return self.id

    def getProgram (self) -> int:
        return self.program

    def getCategory (self) -> str:
        return description[self.program][0]
        
    def getType (self) -> str:
        return description[self.program][1]
    
    def getBounds (self) -> tuple[int, int, int, int]:
        return self.y0, self.y1, self.x0, self.x1
    
    def getLength (self) -> int:
        return self.y1 - self.y0
    
    def getWidth (self) -> int:
        return self.x1 - self.x0
    
    def getArea (self) -> int:
        return self.getLength() * self.getWidth()
    
    def getCentroid (self) -> tuple[float, float]:
        return (self.y0 + self.y1) / 2, (self.x0 + self.x1) / 2
    
    def getRelations (self) -> dict[str, list['Room']]:
        return self.relations
    
    def addRelation (self, relation: str, room: 'Room') -> None:
        if relation in self.relations:
            self.relations[relation].append(room)
        else: self.relations[relation] = [room]
    
    def getDoors (self) -> dict:
        return self.doors

    def addDoor (self, door, relation: str, room: 'Room') -> None:
        self.doors[door] = (relation, room)
 
    def __str__(self):
        return self.id
    
    def to_dict (self):
        centroid = self.getCentroid()
        relations = {}
        for relation, r in self.relations.items():
            l = []
            for item in r:
                l.append(item.getID())
            relations[relation] = l
        doors = {}
        for door, info in self.doors.items():
            doors[door.getID()] = {
                'relation': info[0],
                'room': info[1].getID()
            }
        return {
            "type": self.getType(),
            "category": self.getCategory(),
            "bounds": {
                'y0': self.y0,
                'y1': self.y1,
                'x0': self.x0,
                'x1': self.x1
            },
            "length": self.getLength(),
            "width": self.getWidth(),
            "area": self.getArea(),
            "centroid": {
                'y': centroid[0],
                'x': centroid[1]
            },
            "relations": relations,
            "doors": doors
        }