from enum import Enum


class Actions(Enum):
    '''Actions that a player can take'''
    CHECK = 1,
    CALL = 2,
    RAISE = 3,
    FOLD = 4