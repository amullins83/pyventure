from random import randint


class Player(object):
    def __init__(self):
        self.initializeInventory()
        self.level = 1
        self.gp = 0
        self.hp = self.maxHP = 100
        self.mp = self.maxMP = 50
        self.rollCharacterSheet()

    def initializeInventory(self):
        self.inventory = {}

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

    def D6(self, number):
        value = 0
        for i in range(number):
            value += randint(1, 6)
        return value

    def addToInventory(self, item):
        if item.name in self.inventory.keys():
            self.inventory[item.name]["count"] += 1
        else:
            self.inventory[item.name] = {"item": item, "count": 1}


class Item(object):
    def __init__(self, name, lookText="It's not much to look at."):
        self.name = name

    def look(self):
        print self.lookText


class Room(object):
    def __init__(self, name, exitDirections, items=[], lookText="Nothing to see here..."):
        self.name = name
        self.exitDirections = exitDirections
        self.items = items
        self.options = ["look", "move", "get", "use", "quit"]
        self.neighbor = {"north": -1, "south": -1, "east": -1, "west": -1}
        self.searched = False
        self.lookText = lookText

    def describe(self, text):
        print "You are in the", self.name
        print text
        print "Exits:"
        for direction in self.exitDirections:
            print "\t", direction

    def look(self):
        print self.lookText

        if len(self.items) > 0:
            print "While looking around, you spot the following item(s):"
            for item in self.items:
                print item.name

        self.searched = True

    def takeItem(self, itemName):
        for item in self.items:
            if item.name == itemName:
                self.items.remove(item)
                return item


class Foyer(Room):
    """The initial room"""
    def __init__(self):
        super(Foyer, self).__init__("Foyer", ["south", "west"])
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
    def __init__(self):
        super(LivingRoom, self).__init__("Living Room", ["north", "east"], [Item("Coffee table book")], "There is a book on the coffee table.")
        self.text = """
            You have entered a living room shabbily furnished with a television, a well-worn couch, and a coffee table.
        """
        self.neighbor["north"] = 0
        self.neighbor["east"] = 3

    def describe(self):
        super(LivingRoom, self).describe(self.text)


class DiningRoom(Room):
    def __init__(self):
        super(DiningRoom, self).__init__("Dining Room", ["east"], [Item("Plate", "It's a dinner plate with a faint marinara sauce stain.")], "There is a plate on the dining room table. It looks clean enough, but that's only in comparison to the table itself.")
        self.text = """
            You have entered a dining room. At least, you assume so because the vast majority of the limited floorspace is consumed by
            a single rectangular table that as caked with dust as it is completely lacking in style or character."
        """
        self.neighbor["east"] = 0

    def describe(self):
        super(DiningRoom, self).describe(self.text)


class Bedroom(Room):
    def __init__(self):
        super(Bedroom, self).__init__("Bedroom", ["west"], [Item("Excalibur", "It's apparently a legendary sword from Arthurian legend, but the jury's still out on that one.")], "The hilt of a magnificent legendary sword is inexplicably protruding from the center of the mattress. Wait, what?!")
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
        if __name__ == "__main__":
            self.main()

    def main(self):
        while(self.player.hp > 0):
            self.rooms[self.currentRoom].describe()
            self.getCommand()

    def initializePlayer(self):
        self.player = Player()

    def initializeRooms(self):
        self.rooms = [Foyer(), LivingRoom(), DiningRoom(), Bedroom()]

    def initializeCommands(self):
        self.validCommands = ["move", "look", "get", "use", "quit"]

    def showIntroduction(self):
        print "Pyventure = Win!"

    def getCommand(self):
        self.command = ""
        while self.command not in self.validCommands:

            print "Your choices:"
            for option in self.rooms[self.currentRoom].options:
                print "\t", option

            self.command = raw_input("What would you like to do?: ")
        getattr(self, self.command)()

    def move(self):
        self.direction = ""
        while self.direction not in self.rooms[self.currentRoom].exitDirections:

            print "Your choices:"
            for direction in self.rooms[self.currentRoom].exitDirections:
                print "\t", direction

            self.direction = raw_input("Which direction would you like to go?: ")
        self.changeRoom()

    def changeRoom(self):
        self.currentRoom = self.rooms[self.currentRoom].neighbor[self.direction]

    def look(self):
        self.rooms[self.currentRoom].look()

    def get(self):
        room = self.rooms[self.currentRoom]
        if room.searched and len(room.items) > 0:
            getItem = ""
            itemNames = []
            for item in room.items:
                itemNames.append(item.name)
            while getItem not in itemNames:
                print "Your choices:"
                for itemName in itemNames:
                    print "\t", itemName

                getItem = raw_input("Which thing would you like to get? ")
            self.player.addToInventory(room.takeItem(getItem))

    def use(self):
        pass

    def quit(self):
        self.player.hp = 0


if __name__ == "__main__":
    p = Pyventure()
