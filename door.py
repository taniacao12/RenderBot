from legend import scale

class Door:
    def __init__ (self, id, type, orient, coords):
        self.id = id
        self.type = type # 1 for external, 2 for interior
        self.orientation = orient # 1 for horizontal, 2 for vertical
        self.coordinates = coords
        # self.centroid = ((self.y0 + self.y1 - 1) / 2, (self.x0 + self.x1 - 1) / 2)
        # self.dimensions = (0, 0)
        # self.length = (self.y1 - self.y0) * scale
        # self.width = (self.x1 - self.x0) * scale
        # self.area = region.area * scale ** 2
        # self.rooms = {}
    
    def getID (self) -> int:
        return self.id
    
    def getType (self) -> int:
        return self.type
    
    # def getLength (self) -> int:
    #     return self.length
    
    # def getWidth (self) -> int:
    #     return self.width
    
    # def getArea (self) -> int:
    #     return self.area
        
    # def getCentroid (self) -> tuple[float, float]:
    #     return self.centroid
    
    # def getRooms (self) -> list:
    #     return self.rooms
    
    # def addRoom (self, room) -> None:
    #     self.rooms.append(room)

    # def __str__(self):
    #     text =    "Door ID      {}".format(self.id)
    #     text += "\nBounds:      ({}, {}, {}, {})".format(self.y0, self.y1, self.x0, self.x1)
    #     text += "\nCentroid:    {}".format(self.centroid)
    #     text += "\nLength:      {} ft".format(self.length)
    #     text += "\nWidth:       {} ft".format(self.width)
    #     text += "\nArea:        {} ft^2".format(self.area)
    #     text += "\nOrientation: {}".format(self.orientation)
    #     text += "\nIs Egress:   {}".format(self.egress)
    #     text += "\nRooms:       {}".format(self.rooms)
    #     return text

    # def to_dict (self):
    #     ret = {
    #         "bounds": (self.y0, self.y1, self.x0, self.x1),
    #         "centroid": self.centroid,
    #         "length": self.length,
    #         "width": self.width,
    #         "area": self.area,
    #         "orientation": self.orientation,
    #         "isEgress": self.egress,
    #         "rooms": {},
    #     }
    #     if self.orientation == 'V':
    #         ret["rooms"]["W"] = int(self.rooms[0])
    #         ret["rooms"]["E"] = int(self.rooms[1])
    #     else:
    #         ret["rooms"]["N"] = int(self.rooms[0])
    #         ret["rooms"]["S"] = int(self.rooms[1])
    #     return ret