from sys import path
path.append("../pyventureClasses")

from mapventure import Mapventure
import re


class TestMapventure:
    def setUp(self):
        self.map = Mapventure()

    def tearDown(self):
        self.map = 0

    def add(self):
        self.map.add(4)

    def connect(self):
        self.map.connect(0, 1, "north")

    def test_add(self):
        self.map.add()
        assert len(self.map.neighbors) == 1
        self.map.add(3)
        assert len(self.map.neighbors) == 4

    def test_connect(self):
        self.add()
        self.connect()
        assert self.map.neighbors[0].neighbor["north"] == 1

    def test_next(self):
        self.add()
        self.connect()
        assert self.map.next(0, "north") == 1

    def test_isValidId(self):
        assert not self.map.isValidId(0)
        self.add()
        assert self.map.isValidId(3)
        assert not self.map.isValidId(4)

    def test_validDirections(self):
        self.add()
        assert self.map.validDirections(0) == []
        self.connect()
        assert self.map.validDirections(0) == ["north"]

    def test_showExits(self):
        self.add()
        self.connect()
        show = self.map.showExits(0)
        assert re.search("north", show).group(0) == "north"
