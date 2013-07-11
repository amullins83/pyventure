__all__ = ['items', 'rooms', 'Item', 'Excalibur', 'Room', 'Foyer', 'LivingRoom', 'DiningRoom', 'Bedroom', 'UseHash', 'Mapventure', 'Player']

from sys import path
path += ['items', 'rooms']

#import all items in items directory
from items import *
from rooms import *
from mapventure import Mapventure
from useHash import UseHash
from player import Player
