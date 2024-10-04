class Door:
    def __init__ (self, y0, y1, x0, x1, id, frontDoor):
        self.y0 = int(y0) # minRox
        self.y1 = int(y1) # maxRow
        self.x0 = int(x0) # minCol
        self.x1 = int(x1) # maxCol
        self.id = int(id)
        self.frontDoor = frontDoor
        self.rooms = []
    
    def getID (self) -> int:
        return self.id

    def isFrontDoor (self) -> bool:
        return self.frontDoor

    def getBounds (self) -> tuple[int, int, int, int]:
        return self.y0, self.y1, self.x0, self.x1
    
    def getLength (self) -> int:
        return self.y1 - self.y0
    
    def getWidth (self) -> int:
        return self.x1 - self.x0
    
    def getCentroid (self) -> tuple[float, float]:
        return (self.y0 + self.y1) / 2, (self.x0 + self.x1) / 2
    
    def getRooms (self) -> list:
        return self.rooms
    
    def addRoom (self, room) -> None:
        self.rooms.append(room)

    def __str__(self):
        return self.id
    
    def to_dict (self):
        centroid = self.getCentroid()
        rooms = []
        for room in self.rooms:
            rooms.append(room.getID())
        return {
            "isFrontDoor": self.frontDoor,
            "bounds": {
                'y0': self.y0,
                'y1': self.y1,
                'x0': self.x0,
                'x1': self.x1
            },
            "length": self.getLength(),
            "width": self.getWidth(),
            "centroid": {
                'y': centroid[0],
                'x': centroid[1]
            },
            "rooms": rooms
        }