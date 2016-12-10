from abc import ABCMeta
from typing import List


class Order(metaclass=ABCMeta):
    pass


class Bot(object):
    orders = ...  # type: List[Order]


class GameState(object):
    bots = []  # type: List[Bot]
