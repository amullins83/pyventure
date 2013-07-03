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


class Room(object):
    def __init__(self, name, exitDirections, items):
        self.name = name
        self.exitDirections = exitDirections
        self.items = items
        self.options = ["look", "move", "get", "use"]
        self.neighbor = {"north": -1, "south": -1, "east": -1, "west": -1}

    def describe(self, text):
        print text

        print "You are in the", self.name
        print "Exits:"
        for direction in self.exitDirections:
            print "\t", direction


class Foyer(Room):
    """The initial room"""
    def __init__(self):
        super(Foyer, self).__init__("Foyer", ["south", "west"], [])
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
        super(LivingRoom, self).__init__("Living Room", ["north", "east"], ["Coffee table book"])
        self.text = """

        """
        self.neighbor["north"] = 0
        self.neighbor["east"] = 3

    def describe(self):
        super(LivingRoom, self).describe(self.text)


class DiningRoom(Room):
    def __init__(self):
        super(DiningRoom, self).__init__("Dining Room", ["east"], ["Plate"])
        self.text = """

        """
        self.neighbor["east"] = 0

    def describe(self):
        super(DiningRoom, self).describe(self.text)


class Bedroom(Room):
    def __init__(self):
        super(Bedroom, self).__init__("Bedroom", ["west"], ["Excalibur"])
        self.text = """

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
        self.validCommands = ["move", "look", "get", "use"]

    def showIntroduction(self):
        print "Pyventure = Win!"

    def getCommand(self):
        self.command = ""
        while self.command not in self.validCommands:

            print "Your choices:"
            for option in self.rooms[self.currentRoom].options:
                print "\t", option

            self.command = raw_input("What would you like to do?")
        getattr(self, self.command)()

    def move(self):
        self.direction = ""
        while self.direction not in self.rooms[self.currentRoom].exitDirections:

            print "Your choices:"
            for direction in self.rooms[self.currentRoom].exitDirections:
                print "\t", direction

            self.direction = raw_input("What would you like to do?")
        self.changeRoom()

    def changeRoom(self):
        self.currentRoom = self.rooms[self.currentRoom].neighbor[self.direction]

    def look(self):
        pass

    def get(self):
        pass

    def use(self):
        pass

p = Pyventure()
