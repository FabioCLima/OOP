# Encapsulation:

class BankAccount:
    
    def __init__(self, balance: float) -> None:
        self._balance = balance #! private attribute
    
    @property
    def balance(self):
        return self._balance
    #! internal method hidden from the user    
    def deposit(self, amount: float):
        if amount < 0:
            raise ValueError("Deposit must be a positive.")
        self._balance += amount
    
    #! internal method hidden from the user    
    def withdraw(self, amount: float):
        if amount < 0:
            raise ValueError("Withdrawal amount must positive.")
        if amount > self._balance:
            raise ValueError("Insufficient balance.") 
        self._balance -= amount
    
    #* take away this later    
    # def get_balance(self) -> float:
    #     return self._balance


if __name__ == "__main__":
    bank_acc1 = BankAccount(1250.12)
    print(f"The initial balance is: R$ {bank_acc1._balance}")
    
