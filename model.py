from enum import Enum


class Model(object):
    def __init__(self):
        self.curr_slot = None



class Slot(object):
    def __init__(self, _button, _next, _prev=None, _alt=None, _access_alt=None, _qual=None, _peices=None):
        self.button = _button
        self.next = _next
        self.prev = _prev
        self.alt = _alt
        self.access_alt = _access_alt
        self.qual = _qual
        self.peices = _peices

    def make_next(self, next):
        self.next = next
        next.prev = self

class Qual(Enum):
    SAFE = 1
    HOME = 2
    G = 3
    B = 4
    R = 5
    Y = 6

class Player(Enum):
    BLUE = 1
    GREEN = 2
    RED = 3
    YELLOW = 4
