from sys import path
path.append('.')

import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

from pyventureClasses import *


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
            self.map.showExits(self.currentRoom)
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
        self.map = Mapventure()
        self.map.add(len(self.rooms))
        self.map.connect(0, 1, "south")
        self.map.connect(0, 2, "west")
        self.map.connect(1, 3, "east")
        self.map.connect(1, 0, "north")
        self.map.connect(2, 0, "east")
        self.map.connect(3, 1, "west")

    def initializeCommands(self):
        self.validCommands = ["move", "look", "get", "use", "drop", "quit"]

    def numItems(self):
        num = 0
        for room in self.rooms:
            num += len(room.items)
        return num

    def showIntroduction(self):
        print "Pyventure = Win!"
        print "There are a total of", self.numItems(), "items to collect in this house."
        print "Gotta get 'em all!\n"

    def wait_for_enter(self):
        raw_input("\n\nHit enter to continue")

    def details(self, prompt, validList):
        detail = ""
        while detail not in validList:
            print "\nYour choices:"
            for itemName in validList:
                print "\t", itemName
            detail = raw_input(prompt)
        return detail

    def getCommand(self):
        self.command = self.details("\nWhat would you like to do?: ", self.rooms[self.currentRoom].options)
        getattr(self, self.command)()

    def move(self):
        self.direction = self.details("\nWhich direction would you like to go?: ", self.map.validDirections(self.currentRoom))
        self.changeRoom()

    def changeRoom(self):
        self.currentRoom = self.map.next(self.currentRoom, self.direction)

    def look(self):
        self.rooms[self.currentRoom].look()
        self.wait_for_enter()

    def get(self):
        room = self.rooms[self.currentRoom]
        if room.searched and len(room.items) > 0:
            itemNames = []
            for item in room.items:
                itemNames.append(item.name)
            getItem = self.details("\nWhich thing would you like to get? ", itemNames)

            self.player.addToInventory(room.takeItem(getItem))
            print "\nYou got the", getItem, "!\n"
            self.wait_for_enter()

    def use(self):
        if len(self.player.inventory):
            item = self.details("\nWhich item do you want to use? ", self.player.inventory.keys() + ['nothing'])
            if item != "nothing":
                self.player.use(item)
                self.rooms[self.currentRoom].use(item)
            self.wait_for_enter()

    def drop(self, itemName=""):
        if itemName not in self.player.inventory.keys() and len(self.player.inventory):
            itemName = self.details("\nWhat would you like to drop? ", self.player.inventory.keys() + ['nothing'])
        if itemName != "nothing":
            item = self.player.drop(itemName)
            if item:
                self.rooms[self.currentRoom].items.append(item)

    def quit(self):
        pass


if __name__ == "__main__":
    p = Pyventure()
