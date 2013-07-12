__all__ = ["Item", "Excalibur"]


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

from excalibur import Excalibur
