from abc import ABCMeta


# TODO: who calls what? See the GitHub Issue.

class Order(metaclass=ABCMeta):
    """All orders inherit from this order."""

    @staticmethod
    def execute(bot):
        raise NotImplementedError()


class SpecialOrder(Order, metaclass=ABCMeta):
    """All special orders inherit from this order."""

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


class PlayBoard(object):
    _grid = [[]]  # TODO: implement hexagonal grid; other devs can help

    def __init__(self):
        """Create an empty play board"""
        pass

    @classmethod
    def generate_random_board(cls):
        """
        Fill a playboard with random crystals and/or obstacles
        You can override this method in subclasses to create new game varieties.
        """
        # return cls(...)
        pass


class ProgrammingBoard(object):
    # TODO: How does the programming board work?
    pass


class Player(object):
    def __init__(self):
        self.owned_orders = []  # type: Order
        self.owned_bots = []  # type: Bot


class GameState(object):
    """
    Put helper functions to not pollute the namespace.
    Because globals are bad.
    Directly modify properties.
    """
    bots = []
    players = []

    def __init__(self):
        pass

    @property
    def num_players(self):
        return len(self.players)
