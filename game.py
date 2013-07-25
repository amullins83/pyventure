from pymongo import MongoClient
from sys import path
path.append('.')

import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

from pyventureClasses import *


from pyventureClasses.commands import *


class Pyventure(object):
    def __init__(self):
        self.initializePlayer()
        self.initializeCommands()
        self.initializeRooms()
        self.initializeMap()
        self.currentRoom = 0
        self.showIntroduction()
        self.command = ""
        if __name__ == "__main__":
            self.main()

    def main(self):
        while(self.player.hp > 0 and self.numItems() > 0 and self.command != "quit"):
            self.rooms[self.currentRoom].describe()
            print self.map.showExits(self.currentRoom)
            self.getCommand()
            clear()

        if self.command == "quit":
            print "Though you are reknowned throughout the realms as a brave soul, you bravely run away."
        elif self.player.hp <= 0:
            print "You have tragically succombed to an inevitable violent end. Alas! Alack!"
        elif self.numItems() == 0:
            print "You have acquired every item in the game. Look at you, you little hoarder! You win!"
        else:
            print "For unknown reasons, the game has decided to end now. Maybe it was tired?"
        print "The end."

    def initializePlayer(self):
        self.player = Player()

    def initializeRooms(self):
        self.rooms = [Foyer(self), LivingRoom(self), DiningRoom(self), Bedroom(self)]

    def initializeMap(self):
        neighbors = MongoClient(os.environ["MONGOLAB_URI"], int(os.environ["MONGOLAB_PORT"])).pyventure.maps.find_one({"name": "alpha"})["neighbors"]
        self.map = Mapventure()
        self.map.add(len(neighbors))

        for i in range(len(neighbors)):
            for direction in neighbors[i]:
                self.map.connect(i, neighbors[i][direction], direction)

        # self.map.connect(0, 1, "south")
        # self.map.connect(0, 2, "west")
        # self.map.connect(1, 3, "east")
        # self.map.connect(1, 0, "north")
        # self.map.connect(2, 0, "east")
        # self.map.connect(3, 1, "west")

    def initializeCommands(self):
        self.commands = {
            "move": Move(self),
            "look": Look(self),
            "get":  Get(self),
            "use":  Use(self),
            "drop": Drop(self),
            "quit": Quit(self)
        }

    def numItems(self):
        num = 0
        for room in self.rooms:
            num += len(room.items)
        return num

    def showIntroduction(self):
        print "Pyventure = Win!"
        print "There are a total of", self.numItems(), "items to collect in this house."
        print "Gotta get 'em all!\n"

    def changeRoom(self):
        self.currentRoom = self.map.next(self.currentRoom, self.direction)

    def getCommand(self):
        self.command = details("\nWhat would you like to do?: ", self.commands)
        self.commands[self.command].do()

if __name__ == "__main__":
    p = Pyventure()
