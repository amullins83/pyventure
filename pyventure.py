import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


from random import randint
from collections import defaultdict


class Player(object):
    def capacityFactor(self):
        return 5

    def __init__(self):
        self.level = 1
        self.gp = 0
        self.hp = self.maxHP = 100
        self.mp = self.maxMP = 50
        self.rollCharacterSheet()
        self.initializeInventory()

    def initializeInventory(self):
        self.inventory = {}
        self.remainingCapacity = self.capacity()

    def rollCharacterSheet(self):
        self.constitution = self.D6(3)
        self.dexterity = self.D6(3)
        self.charisma = self.D6(3)
        self.intelligence = self.D6(3)
        self.strength = self.D6(3)
        self.wisdom = self.D6(3)
        self.setHP()
        self.setMP()
        self.setAttack()
        self.setDefense()

    def setHP(self):
        self.maxHP += self.constitution
        self.hp = self.maxHP

    def setMP(self):
        self.maxMP += self.wisdom
        self.mp = self.maxMP

    def setAttack(self):
        self.attack = self.strength

    def setDefense(self):
        self.defense = self.dexterity

    def capacity(self):
        return self.capacityFactor() * self.strength

    def D6(self, number):
        value = 0
        for i in range(number):
            value += randint(1, 6)
        return value

    def addToInventory(self, item):
        if item.size <= self.remainingCapacity:
            if item.name in self.inventory.keys():
                self.inventory[item.name]["count"] += 1
            else:
                self.inventory[item.name] = {"item": item, "count": 1}
            self.remainingCapacity -= item.size
        else:
            print "You can't carry that."
            if len(self.inventory):
                print "Try dropping something."

    def isInInventory(self, itemName):
        return itemName in self.inventory.keys() and self.inventory[itemName]["count"]

    def use(self, itemName):
        if self.isInInventory(itemName):
            print "You use the " + itemName
            self.inventory[itemName]["item"].use()

    def drop(self, itemName):
        if self.isInInventory(itemName):
            print "You drop the " + itemName
            self.inventory[itemName]["count"] -= 1
            item = self.inventory[itemName]["item"]
            if self.inventory[itemName]["count"] == 0:
                del self.inventory[itemName]
            return item


class Item(object):
    def __init__(self, name, roomText="", lookText="It's not much to look at.", size=1, isConsumed=False):
        self.name = name
        self.roomText = roomText
        self.size = size
        self.isConsumed = isConsumed
        self.used = False

    def look(self):
        print self.lookText

    def use(self):
        self.used = True


class Excalibur(Item):
    def __init__(self):
        super(Excalibur, self).__init__("Excalibur", "The hilt of a magnificent legendary sword is inexplicably protruding from the center of the mattress. Wait, what?!", "It's apparently a legendary sword from Arthurian legend, but the jury's still out on that one.")


def emptyfunction():
    pass


class UseHash(defaultdict):
    def __init__(self):
        self.setdefault(dict)


class Room(object):
    def replaceText(self, find, replacement):
        self.text = self.text.replace(find, replacement)

    def __init__(self, name, exitDirections, game, items=[], lookText="Nothing to see here...\n", useHash=UseHash()):
        self.name = name
        self.game = game
        self.exitDirections = exitDirections
        self.items = items
        self.options = game.validCommands
        self.neighbor = {"north": -1, "south": -1, "east": -1, "west": -1}
        self.searched = False
        self.lookText = lookText
        self.useHash = useHash

    def describe(self, text):
        print "\nYou are in the", self.name, "\n"
        print text
        print "\nExits:"
        for direction in self.exitDirections:
            print "\t", direction

    def look(self):
        print self.lookText

        if len(self.items) > 0:
            for item in self.items:
                print item.roomText

            print "\nWhile looking around, you spot the following item(s):"
            for item in self.items:
                print "\t", item.name

        self.searched = True

    def takeItem(self, itemName):
        for item in self.items:
            if item.name == itemName:
                self.items.remove(item)
                return item

    def use(self, itemName):
        if itemName in self.useHash:
            print self.useHash[itemName]["text"]
            self.useHash[itemName]["action"]()
        else:
            print "Nothing happens."


class Foyer(Room):
    """The initial room"""

    def __init__(self, game):
        useHash = UseHash()
        useHash["Excalibur"] = {
            "text": "You slice the coatrack in half!",
            "action": lambda: self.replaceText("a\n            coatrack and ", "")
        }
        super(Foyer, self).__init__("Foyer", ["south", "west"], game, useHash=useHash)
        self.text = """
            You are standing in an entryway with a
            coatrack and a dirty linoleum floor. The walls were
            painted in the 1980's, as evidenced by their putrid
            yellow hue and general dinginess. You get the haunting
            sense that maybe you've been here before, like maybe
            it was your childhood home in a past life, but one
            where you were a child in the 80's.

        """
        self.neighbor["south"] = 1
        self.neighbor["west"] = 2

    def describe(self):
        super(Foyer, self).describe(self.text)


class LivingRoom(Room):
    def __init__(self, game):
        super(LivingRoom, self).__init__("Living Room", ["north", "east"], game, [Item("book", "there is a book on the coffee table", "a giant photo book filled with images of the great pyramids in Egypt. The title: 'Triangular Things I Totally Saw Once'. Author: Justin Bieber.")], "")
        self.text = """
            You have entered a living room shabbily furnished with a television, a well-worn couch, and a coffee table.
        """
        self.neighbor["north"] = 0
        self.neighbor["east"] = 3

    def describe(self):
        super(LivingRoom, self).describe(self.text)


class DiningRoom(Room):
    def __init__(self, game):
        super(DiningRoom, self).__init__("Dining Room", ["east"], game, [Item("Plate", "There is a plate on the dining room table. It looks clean enough, but that's only in comparison to the table itself.", "It's a dinner plate with a faint marinara sauce stain.")], "")
        self.text = """
            You have entered a dining room. At least, you assume so because the vast majority of the limited floorspace is consumed by
            a single rectangular table that as caked with dust as it is completely lacking in style or character."
        """
        self.neighbor["east"] = 0

    def describe(self):
        super(DiningRoom, self).describe(self.text)


class Bedroom(Room):
    def returnSword(self):
        self.game.drop("Excalibur")

    def __init__(self, game):
        useHash = UseHash()
        useHash["Excalibur"] = {
            "text": "You twirl the sword around and wind up getting it stuck back in the bedsheets.",
            "action": self.returnSword
        }
        super(Bedroom, self).__init__("Bedroom", ["west"], game, [Excalibur()], "", useHash)
        self.text = """
            You have entered what must be the single largest pile of dirty t-shirts and random, useless stuff you have ever seen.
            You almost fail to notice the fact that there appears to be a roughly bed-shaped object on the opposite corner of the room
            from the entrance. Crossing the room to take a better look at it would probably be a waste of time, not unlike this game.
        """
        self.neighbor["west"] = 1

    def describe(self):
        super(Bedroom, self).describe(self.text)


class Pyventure(object):
    def __init__(self):
        self.initializePlayer()
        self.initializeCommands()
        self.initializeRooms()
        self.currentRoom = 0
        self.showIntroduction()
        self.command = ""
        if __name__ == "__main__":
            self.main()

    def main(self):
        while(self.player.hp > 0 and self.numItems() > 0 and self.command != "quit"):
            self.rooms[self.currentRoom].describe()
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
        self.direction = self.details("\nWhich direction would you like to go?: ", self.rooms[self.currentRoom].exitDirections)
        self.changeRoom()

    def changeRoom(self):
        self.currentRoom = self.rooms[self.currentRoom].neighbor[self.direction]

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
