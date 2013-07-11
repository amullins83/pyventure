from . import Room
from ..useHash import UseHash
from ..items import Item


class LivingRoom(Room):
    def __init__(self, game):
        super(LivingRoom, self).__init__("Living Room", game, [Item("book", "there is a book on the coffee table", "a giant photo book filled with images of the great pyramids in Egypt. The title: 'Triangular Things I Totally Saw Once'. Author: Justin Bieber.")], "")
        self.text = """
            You have entered a living room shabbily furnished with a television, a well-worn couch, and a coffee table.
        """

    def describe(self):
        super(LivingRoom, self).describe(self.text)
