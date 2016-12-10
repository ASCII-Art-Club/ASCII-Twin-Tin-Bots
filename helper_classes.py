from abc import ABCMeta
from collections import UserList


class TooManyOrders(ValueError):
    pass


class OrderList(UserList, metaclass=ABCMeta):
    """An abstract order list"""


class DefaultOrderList(OrderList):
    """
    An OrderList with max size three, like in the original game.
    Supports all Python list operations.
    """

    max_orders = 3  # type: int

    def __init__(self, orders=None):
        # This method is called every time an inherited list operation is run.
        # See the comment below docs.python.org/3/library/collections.html#collections.UserList.
        super().__init__()
        if orders is not None and len(orders) > self.max_orders:
            raise TooManyOrders("Bots can have at most {} orders; tried to have {}".format(self.max_orders, len(list)))
