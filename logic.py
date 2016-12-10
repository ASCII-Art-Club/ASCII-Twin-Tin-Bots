from abc import ABCMeta


class Order(metaclass=ABCMeta):
    """All orders inherit from this order."""

    @staticmethod
    def execute(bot):
        raise NotImplementedError()


class Bot(object):
    """
    Attribute API:
    bot_team - access team of bot
    orders - access orders in bot
    """

    def __init__(self, initial_order: Order):
        self.orders = initial_order
        ...


class GameState(object):
    """
    Put helper functions to not pollute the namespace.
    Because globals are bad.
    Directly modify properties.
    """
    bots = []

    def __init__(self):
        pass
