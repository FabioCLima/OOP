# __main__.py
'''The entry point to test the wizcoin package development
'''

from wizcoin import WizCoin


if __name__ == "__main__":

    purse = WizCoin(2, 5, 99)
    print(purse)
    print(f"'G':{purse.galleons}, 'S':{purse.sickles}, 'K':{purse.knuts}")
    print(f"Total value: {purse.value()}")
    print(f"Weight: {purse.weightInGrams(), 'grams'}\n")
    print("*****************")
    print("")
    coinJar = WizCoin(13, 0, 0)
    print(coinJar)
    print(
        f"'G':{coinJar.galleons}, 'S':{coinJar.sickles}, 'K':{coinJar.knuts}"
    )
    print(f"Total value: {coinJar.value()}")
    print(f"Weight: {coinJar.weightInGrams(), 'grams'}\n")
    print("*****************")
    print("")
    change = WizCoin(9, 7, 20)
    print(change.sickles)
    change.sickles += 10
    print(change.sickles)
    print("-----------------------------------------------------")
    print("")
    pile = WizCoin(2, 3, 31)
    print(pile.sickles)
    pile.someNewAttribute = "a new attr"  # A new attribute is created.
    print(pile.someNewAttribute)
