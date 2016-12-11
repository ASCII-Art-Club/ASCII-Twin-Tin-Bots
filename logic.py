from abc import ABCMeta
from helper_classes import OrderList
from typing import List  # this is jus to help linters


# TODO: who calls what? See the GitHub Issue.

class Order(metaclass=ABCMeta):
    """All orders inherit from this order."""

    @classmethod
    def execute(cls, bot: Bot):
        raise NotImplementedError()


class SpecialOrder(Order, metaclass=ABCMeta):
    """All special orders inherit from this order."""


class Forward(Order):
    forward_constant = 1

    @classmethod
    def execute(cls, bot):
        bot.move_forward(cls.forward_constant)


class ForwardTwice(Forward):
    forward_constant = 2


class Rotate(Order):
    rotate_constant = 1

    @classmethod
    def execute(cls, bot):
        bot.rotate(cls.rotate_constant)


class RotateLeft(Rotate):
    rotate_constant = -1


class RotateRight(Rotate):
    rotate_constant = 1


class LoadCrystal(Order):
    @classmethod
    def execute(cls, bot):
        bot.loadCrystal()
        raise NotImplementedError()


class UnLoadCrystal(Order):
    @classmethod
    def execute(cls, bot):
        bot.unLoadCrystal()
        raise NotImplementedError()


class RotateLeftTwice(Rotate, SpecialOrder):
    rotate_constant = -1


class RotateRightTwice(Rotate, SpecialOrder):
    rotate_constant = 2


class AntiZap(SpecialOrder):
    @classmethod
    def execute(cls, bot):
        bot.anti_zap = True
        raise NotImplementedError()


class AntiTheft(SpecialOrder):
    @classmethod
    def execute(cls, bot):
        bot.anti_theft = True


class UTurn(Rotate, SpecialOrder):
    rotate_constant = 3


class ForwardThrice(Forward, SpecialOrder):
    forward_constant = 3


class ForwardLoad(SpecialOrder):
    @classmethod
    def execute(cls, bot):
        bot.moveForward(1)
        bot.loadCrystal()
        raise NotImplementedError()


class Dash(SpecialOrder):
    @classmethod
    def execute(cls, bot):
        bot.dash()


class Jump(SpecialOrder):
    @classmethod
    def execute(cls, bot):
        bot.jump()


class BackUp(Forward, SpecialOrder):
    forward_constant = -1


class Zap(Order):
    long_range, times = False, 2

    @classmethod
    def execute(cls, bot):
        bot.zap(times=cls.times, long_range=cls.long_range)


class ZapTwice(Zap, SpecialOrder):
    times = 2


class ZapLongRange(Zap, SpecialOrder):
    long_range = True


class ForwardZap(Forward, Zap, SpecialOrder):
    forward_constant = 1

    @classmethod
    def execute(cls, bot):
        Forward.execute(bot)
        Zap.execute(bot)


class Bot(object):
    """
    Attribute API:
    bot_team - access team of bot
    orders - access orders in bot
    """

    def __init__(self, initial_orders: OrderList):
        self.orders = initial_orders
        ...

    # TODO: Implement these methods

    def move_forward(self, units):
        raise NotImplementedError()

    def rotate(self, direction):
        raise NotImplementedError()

    def zap(self, times=1, long_range=False):
        raise NotImplementedError()
        if times > 1:
            self.zap(times - 1, long_range=long_range)

    def jump(self):
        raise NotImplementedError()

    def dash(self):
        raise NotImplementedError()
    # TODO: either make anti_zap and anti_theft properties (getter/setter)
    #  if they are not-permanent, or make them regular ol' attributes.


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
        self.owned_orders = []  # type: List[Order]
        self.owned_bots = []  # type: List[Bot]


class GameState(object):
    """
    Put helper functions to not pollute the namespace.
    Because globals are bad.
    Directly modify properties.
    """
    bots = []
    players = []

    def __init__(self):
        # we should have a simple system to swap out classes to make it extensible
        pass

    @property
    def num_players(self):
        return len(self.players)
