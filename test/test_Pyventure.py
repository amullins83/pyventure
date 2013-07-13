from sys import path
path.append("..")

from game import Pyventure
from pyventureClasses import *


class TestClass:
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
