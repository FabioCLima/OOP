from shirt import Shirt

new_shirt = Shirt('red', 'S', 'short sleeve', 15)

print(new_shirt.color)
print(new_shirt.size)
print(new_shirt.style)
print(new_shirt.price)

new_shirt.change_price(10)
print(new_shirt.price)

print(new_shirt.discount(.2))

new_shirt2 = Shirt('orange', 'L', 'short-sleeve', 10)
print(repr(new_shirt2))
print(str(new_shirt2))

total_discount = new_shirt.discount(.14) + new_shirt2.discount(.06)
print(total_discount)
