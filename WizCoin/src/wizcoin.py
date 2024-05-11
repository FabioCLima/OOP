# wizcoin.py
"""
WizCoin class represents a number of coins in a fictional wizard currency.
The WizCoin can be set as:
    >>>knuts, sickes and galleons
        >>> 1 sickles = 29 knuts
            >>> 1 galleons = 17 sickles or 493 knuts
            --------------------> galleons > sickles and galleons >> knuts

The objects in the WizCoin class represent a quantity of coins, not an amount
of money.
    Example:
            It will inform you that you are holding five quarters and one
            dime rather than $1.35
"""


class WizCoin:

    """Represents a quantity of coins in a fictional wizard currency.

    The WizCoin class represents a quantity of coins in a fictional wizard
    currency, allowing the creation of objects with specified quantities of
    galleons, sickles, and knuts.

    The conversion rates for the wizard currency are as follows:
        - 1 sickle = 29 knuts
        - 1 galleon = 17 sickles or 493 knuts

    Note:
        The objects in the WizCoin class represent a quantity of coins, not an
        amount of money. For example, it will inform you that you are holding
        five galleons, three sickles, and ten knuts, rather than representing
        a monetary amount.

    Example:
        coin = WizCoin(galleons=5, sickles=3, knuts=10)
        print(coin)  # Output: WizCoin(galleons=5, sickles=3, knuts=10)

    Attributes:
        galleons (int): The quantity of galleons in the WizCoin object.
        sickles (int): The quantity of sickles in the WizCoin object.
        knuts (int): The quantity of knuts in the WizCoin object.

    Methods:
        value(): Returns the total value of the coins in knuts.
        weightInGrams(): Returns the total weight of the coins in grams.
        __str__(): Returns a string representation of the WizCoin object.
        __repr__(): Returns a string representation of the WizCoin object for
        debugging.
    """

    def __init__(self, galleons: int, sickles: int, knuts: int) -> None:
        """Create a new WizCoin object with galleons, sickles, and knuts.

        Args:
            galleons (int): A quantity that means 17 sickles or 493 knuts.
            sickles (int): A quantity that means 29 knuts.
            knuts (int): A most basic quantity means 1 unidade of knuts
        """

        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def value(self) -> int:
        """The value (in knuts) of all the coins in this WizCoin object."""
        return (self.galleons * 17 * 29) + (self.sickles * 29) + (self.knuts)

    def weightInGrams(self):
        """Returns the weight of the coins in grams."""
        return (self.galleons * 31.103) + (self.sickles * 11.34) + \
            (self.knuts * 5.0)

    def __str__(self):
        """Return a string representation of the WizCoin object."""
        return f"WizCoin(galleons={self.galleons}, sickles={self.sickles},\
            knuts={self.knuts})"

    def __repr__(self):
        """Return a string representation of the WizCoin object for
        debugging."""
        cls_name = self.__class__.__qualname__
        return f"{cls_name}(galleons={self.galleons}, sickles={self.sickles},\
            knuts={self.knuts})"
