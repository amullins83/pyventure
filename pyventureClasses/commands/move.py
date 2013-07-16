from . import Command


class move(Command):
    """docstring for move"""
    def __init__(self, game):
        self.checkList = {
            "what": lambda: True
        }
        super(move, self).__init__("move", game, self.doFunction, self.checkList)
