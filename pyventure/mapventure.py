class Neighbor(object):
    def __init__(self, id, directionList=["north", "south", "east", "west"]):
        self.id = id
        self.directionList = directionList
        self.neighbor = {}
        for direction in directionList:
            self.neighbor[direction] = -1

    def connect(self, direction, newId):
        self.neighbor[direction] = newId


class Mapventure(object):
    def __init__(self, directionList=["north", "south", "east", "west"]):
        self.directionList = directionList
        self.neighbors = []

    def add(self, num=1):
        for i in range(num):
            self.neighbors.append(Neighbor(len(self.neighbors), self.directionList))

    def connect(self, id1, id2, direction):
        if self.isValidId(id1) and self.isValidId(id2):
            self.neighbors[id1].connect(direction, id2)

    def next(self, id, direction):
        if direction in self.directionList:
            return self.neighbors[id].neighbor[direction]
        else:
            return -1

    def isValidId(self, id):
        return id >= 0 and id < len(self.neighbors)
