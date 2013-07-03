import sys
sys.path = [".."] + sys.path
import unittest
from pyventure import Pyventure


class PyventureError(Exception):
    """A custom error class to test Pyventure"""
    def __init__(self, msg):
        super(PyventureError, self).__init__(msg)


class TestPyventure(unittest.TestCase):
    """Believe it or not, the goal of this class is to test the Pyventure class."""
    def __init__(self):
        super(TestPyventure, self).__init__()
        self.game = Pyventure()
        self.getTests()
        self.run()

    def run(self):
        for testFunction in self.tests:
            try:
                testFunction()
            except PyventureError, e:
                print "Error while testing Pyventure:", e.msg

    def getTests(self):
        self.tests = [self.exists, self.containsFourRooms]

    def exists(self):
        if not self.game:
            raise PyventureError("Pyventure does not exist")

    def containsFourRooms(self):
        if len(self.game.rooms) < 4:
            raise PyventureError("Pyventure has fewer than 4 rooms")
