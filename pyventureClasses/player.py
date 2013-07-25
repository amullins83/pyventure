from random import randint


class Player(object):
    def capacityFactor(self):
        return 5

    def __init__(self):
        self.level = 1
        self.gp = 0
        self.hp = self.maxHP = 100
        self.mp = self.maxMP = 50
        self.xp = 0
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
