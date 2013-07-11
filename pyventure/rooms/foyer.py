from pyventure.useHash import UseHash
from pyventure.room import Room


class Foyer(Room):
    """The initial room"""

    def __init__(self, game):
        useHash = UseHash()
        useHash["Excalibur"] = {
            "text": "You slice the coatrack in half!",
            "action": lambda: self.replaceText("a\n            coatrack and ", "")
        }
        super(Foyer, self).__init__("Foyer", game, useHash=useHash)
        self.text = """
            You are standing in an entryway with a
            coatrack and a dirty linoleum floor. The walls were
            painted in the 1980's, as evidenced by their putrid
            yellow hue and general dinginess. You get the haunting
            sense that maybe you've been here before, like maybe
            it was your childhood home in a past life, but one
            where you were a child in the 80's.

        """

    def describe(self):
        super(Foyer, self).describe(self.text)
