from account.account import *

class savingsaccount(account):
    """_summary_
    """

    def __init__(self, balance, interestRate):
        super().__init__(balance)
        self.__interestRate = float(interestRate)

    def setInterestRate(self, interestRate: float):
        self.__interestRate = interestRate

    def getInterestRate(self):
        return self.__interestRate
    
    def getInterest(self):
        return self.getInterestRate() * self.getBalance()
    
    def credit(self, amount: float):
        super().credit(amount * self.getInterestRate())

    def __str__(self):
        return f"Savings account balance: {self.getBalance()}\nInterest Rate: {self.getInterestRate()}\nInterest: {self.getInterest()}"
    
    