# @property in Python -- What is it and How do you use it?

from mass import Mass

mass = Mass(112)
print(f"The mass object created is {mass}")

print("Changing the quantity of kilogram, for lets 115 kg")
mass.kg = 115
print(f"The kilogram of the object it was updated is: {115} kg")
# print(f"When we update a attribute of object directly, the others attributes remain the same: {mass.grams}g")

mass = Mass(21.32)
print(f"The mass object created is {mass}")
# print(f"The mass object in grams is {mass.grams()}")

mass1 = Mass(94.45)
mass2 = Mass(0.45)

print(f"The addition between mass1 and mass2, is mass={mass1.__add__(mass2)} kg")
# print(f"The addition between mass1 and mass3, is mass={mass1.__add__('a')} kg")

print("You can call mass.grams anymore, because grams is method")
print('To be able call grams method without parentheses, you need the @property decorator')

mass3 = Mass(94.55)
print(f"The grams of the mass3 is {mass3.grams}")

mass4 = Mass(93.7)
print(mass4.kg)
print(mass4.grams)
mass4.grams = 500
print(mass4.kg)
print(mass4.grams)

del mass1.grams
print(mass1.kg)
print(mass1.grams)