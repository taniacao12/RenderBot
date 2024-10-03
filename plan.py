class Plan:
    def __init__ (self, plan, frontDoor, interiorDoors, rooms):
        self.plan = plan
        self.frontDoor = frontDoor
        self.interiorDoors = interiorDoors
        self.rooms = rooms
        
    def output (self):
        ret = ""
        area = 0
        for room in self.rooms:
            ret += "\n========== Room {:<2} ==========\n".format(room.getID())
            ret += "Type: {}\n".format(room.getType())
            ret += "Category: {}\n".format(room.getCategory())
            ret += "Dimensions: {} by {} pixels\n".format(room.getLength(), room.getWidth())
            ret += "Area: {} square pixels\n".format(room.getArea())
            for relation, r in room.getRelations().items():
                ret += "{}:".format(relation)
                for item in r:
                    ret += " Room {}".format(item.getID())
                ret += "\n"
            for door, info in room.getDoors().items():
                ret += "Door {}: {} of room {}\n".format(door.getID(), info[0], info[1].getID())
            area += room.getArea()
        ret += "\n========== {} Doors ==========\n".format(len(self.interiorDoors) + 1)
        ret += "Front Door {}: Room {}\n".format(self.frontDoor.getID(), self.frontDoor.getRooms()[0].getID())
        for door in self.interiorDoors:
            ret += "Interior Door {}: Room {} and {}\n".format(door.getID(), door.getRooms()[0].getID(), door.getRooms()[1].getID())
        ret += "\n========== Overview ==========\n"
        ret += "Total Area: {}\n".format(area)
        return ret