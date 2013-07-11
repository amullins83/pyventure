from sys import path
path.append('items')


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

#import all items in items directory
from items.excalibur import Excalibur
