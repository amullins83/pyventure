__all__ = ["Room", "Foyer", "LivingRoom", "DiningRoom", "Bedroom"]


from ..useHash import UseHash


class Room(object):
    def replaceText(self, find, replacement):
        self.text = self.text.replace(find, replacement)

    def __init__(self, name, game, items=[], lookText="Nothing to see here...\n", useHash=UseHash()):
        self.name = name
        self.game = game
        self.items = items
        self.options = game.validCommands
        self.searched = False
        self.lookText = lookText
        self.useHash = useHash

    def describe(self, text):
        print "\nYou are in the", self.name, "\n"
        print text

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

from foyer import Foyer
from bed import Bedroom
from living import LivingRoom
from dining import DiningRoom
