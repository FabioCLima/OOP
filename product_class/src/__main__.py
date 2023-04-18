import doctest
from product import Product


p1 = Product("PS5", "Console Gamer", 4500)
print(p1)
print(repr(p1))
doctest.testmod()
