from . import Room
from ..useHash import UseHash
from ..items import Item


class DiningRoom(Room):
    def __init__(self, game):
        super(DiningRoom, self).__init__("Dining Room", game, [Item("Plate", "There is a plate on the dining room table. It looks clean enough, but that's only in comparison to the table itself.", "It's a dinner plate with a faint marinara sauce stain.")], "")
        self.text = """
            You have entered a dining room. At least, you assume so because the vast majority of the limited floorspace is consumed by
            a single rectangular table that as caked with dust as it is completely lacking in style or character."
        """

    def describe(self):
        super(DiningRoom, self).describe(self.text)
