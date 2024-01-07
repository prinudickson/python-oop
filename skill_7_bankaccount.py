from icecream import ic

class BankAccount:

    interest_rate = None
    withdrawal_fee = None

    def __init__(self, initial_balance):
        self._balance = initial_balance

    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, balance):
        self._balance = balance
        return f"initial balance set as {balance}"
    
    def __repr__(self) -> str:
        return f"A {self.__class__} with ${self.balance} in it"
    
    def pay_interest(self):
        interest = self.balance * self.interest_rate
        self._balance += interest
        return f"A interest of ${interest} deposited into the account"
    
    def deposit(self, amount):
        self._balance += amount
        return f"A deposit of ${amount} deposited into the account"
    
    def withdraw(self, amount):
        if self.withdrawal_fee is None:
            self._balance -= amount
        else:
            self._balance -= (amount + self.withdrawal_fee)
        return f"A withdrawl of ${amount} taken out of the account"
    

class Savings(BankAccount):
    interest_rate = 0.0035
    
class HighInterest(BankAccount):
    interest_rate = 0.007

    def __init__(self, initial_balance=0, withdrawal_fee=5):
        super().__init__(initial_balance)
        self.withdrawal_fee = withdrawal_fee

class LockedIn(BankAccount):
    interest_rate = 0.009

    def withdraw(self, amount):
        return "Unable to withdraw amount from LockedIn account!"


if __name__ == "__main__":
    b = BankAccount(10)
    ic(b)
    ic(b.__dict__)
    ic(b.balance)
    b.balance = 20
    ic(b.balance)
    ic(b.__dict__)
    ic(b.interest_rate)

    s = Savings(100)
    s.pay_interest()
    ic(s)
    s.deposit(10)
    ic(s)
    s.withdraw(30)
    ic(s)
    ic(s.__dict__)
    ic(s.interest_rate)

    l = LockedIn(100)
    l.pay_interest()
    ic(l)
    l.deposit(10)
    ic(l)
    ic(l.withdraw(30))
    ic(l)
    ic(l.__dict__)
    ic(l.interest_rate)

    h = HighInterest(100, 10)
    h.pay_interest()
    ic(h)
    h.deposit(10)
    ic(h)
    h.withdraw(30)
    ic(h)
    ic(h.__dict__)
    ic(h.interest_rate)




        