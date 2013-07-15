from sys import path
path.append("..")

from game import Pyventure
from pyventureClasses import *


class TestPyventure:
    """Believe it or not, the goal of this class is to test the Pyventure class."""
    def setUp(self):
        self.game = Pyventure()

    def tearDown(self):
        self.game = 0

    def test_exists(self):
        assert self.game

    def test_containsFourRooms(self):
        assert len(self.game.rooms) >= 4

    def test_roomsInOrder(self):
        roomType = [Foyer, LivingRoom, DiningRoom, Bedroom]
        for room in range(len(self.game.rooms)):
            assert self.game.rooms[room].__class__ == roomType[room]

    def test_map(self):
        for connection in [(0, 1, "south"), (0, 2, "west"), (1, 0, "north"), (1, 3, "east"), (2, 0, "east")]:
            assert self.game.map.next(connection[0], connection[2]) == connection[1]
