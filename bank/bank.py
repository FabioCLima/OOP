# bank.py
'''
A module to study public access or no public access
'''


class BankAccount:

    def __init__(self, accountHolder) -> None:
        # BankAccount methods can access self._balance, but code outside of
        # this class should not:
        self._balance = 0
        self._name = accountHolder
        with open(self._name + "Ledger.txt", "w") as ledgerFile:
            ledgerFile.write('Balance is 0\n')

    def deposit(self, amount):
        if amount <= 0:
            return  # Don't allow negative "deposits".
        self._balance += amount
        with open(self._name + "Ledger.txt", "w") as ledgerFile:
            ledgerFile.write('Deposit ' + str(amount) + '\n')
            ledgerFile.write('Balance is ' + str(self._balance) + '\n')

    def withdraw(self, amount):
        if self._balance < amount or amount < 0:
            return  # Not enough is account, or withdraw is negative.
        self._balance -= amount
        with open(self._name + "Ledger.txt", "w") as ledgerFile:
            ledgerFile.write('Withdraw ' + str(amount) + '\n')
            ledgerFile.write('Balance is ' + str(self._balance) + '\n')


if __name__ == "__main__":
    alice_acc = BankAccount('Alice')
    alice_acc.deposit(120)  # _balance can be affected through deposit()
    alice_acc.withdraw(40)  # _balance can be affected through withdraw()

    # Changing _name or _balance outside of BankAccount is impolite, but
    # allowed:
    alice_acc._balance = 10000000
    alice_acc.withdraw(1000)

    alice_acc._name = "Fabio"  # Now we're modifying Fabio's account ledger!
    alice_acc.withdraw(1000)   # This withdrawal is recorded in FabioLedger.txt
