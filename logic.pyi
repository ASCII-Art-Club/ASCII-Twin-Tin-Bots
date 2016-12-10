from abc import ABCMeta
from typing import List


class Order(metaclass=ABCMeta):
    pass


class Bot(object):
    orders = ...  # type: List[Order]


class GameState(object):
    """
    Put helper functions to not pollute the namespace.
    Because globals are bad.
    Directly modify properties.
    """

    bots = []  # type: List[Bot]

    def __init__(self):
        pass
