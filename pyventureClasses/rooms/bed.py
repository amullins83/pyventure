from . import Room
from ..items import *
from ..useHash import UseHash


class Bedroom(Room):
    def returnSword(self):
        self.game.drop("Excalibur")

    def __init__(self, game):
        useHash = UseHash()
        useHash["Excalibur"] = {
            "text": "You twirl the sword around and wind up getting it stuck back in the bedsheets.",
            "action": self.returnSword
        }
        super(Bedroom, self).__init__("Bedroom", game, [Excalibur()], "", useHash)
        self.text = """
            You have entered what must be the single largest pile of dirty t-shirts and random, useless stuff you have ever seen.
            You almost fail to notice the fact that there appears to be a roughly bed-shaped object on the opposite corner of the room
            from the entrance. Crossing the room to take a better look at it would probably be a waste of time, not unlike this game.
        """

    def describe(self):
        super(Bedroom, self).describe(self.text)
