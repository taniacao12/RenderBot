class Door:
    def __init__ (self, y0, y1, x0, x1, id, frontDoor):
        self.y0 = y0 # minRox
        self.y1 = y1 # maxRow
        self.x0 = x0 # minCol
        self.x1 = x1 # maxCol
        self.id = id
        self.frontDoor = frontDoor
        self.rooms = []
    
    def getID (self):
        return self.id

    def isFrontDoor (self):
        return self.frontDoor

    def getBounds (self):
        return self.y0, self.y1, self.x0, self.x1
    
    def getLength (self):
        return self.y1 - self.y0
    
    def getWidth (self):
        return self.x1 - self.x0
    
    def getCentroid (self):
        return (self.y0 + self.y1) / 2, (self.x0 + self.x1) / 2
    
    def getRooms (self):
        return self.rooms
    
    def addRoom (self, room):
        self.rooms.append(room)