from account.account import *

class savingsaccount(account):
    """The SavingsAccount class has methods to manage the balance
    and interest rate of a savings account.

    Args:
        account (account): class that includes methods to manage the balance
    of a bank account.
    """

    def __init__(self, balance, interestRate):
        """Constructs a savings account with a specified balance and interest rate.

        Args:
            balance (float): balance
            interestRate (float): interest rate
        """

        super().__init__(balance)
        self.__interestRate = float(interestRate)

    def setInterestRate(self, interestRate: float):
        """Sets the interest rate for the calling savings account.

        Args:
            interestRate (float): interest rate
        """

        self.__interestRate = interestRate

    def getInterestRate(self):
        """Returns the interestrate for the calling savings account.

        Returns:
            float: interestrate
        """

        return self.__interestRate
    
    def getInterest(self):
        """Returns the interest for the calling savings account.

        Returns:
            float: interest
        """

        return self.getInterestRate() * self.getBalance()
    
    def credit(self, amount: float):
        """Increases the balance of the calling savings account by the specified
        amount times the interest rate of this savings account.

        Args:
            amount (float): the amount to increase the balance by
        """

        super().credit(amount * self.getInterestRate())

    def __str__(self):
        """Returns string representation of the calling savings account.

        Returns:
            str: string representation of the calling savings account
        """

        return f"Savings account balance: {self.getBalance()}\nInterest Rate: {self.getInterestRate()}\nInterest: {self.getInterest()}"
    
    def __eq__(self, other):
        """Tests if the calling savings account is equal to the specified object.

        Args:
            other: the specified object

        Returns:
            Boolean: True if the calling savings account is equal to the specified
            object, else False
        """
        
        # check if other is not None
        if other is not None:
            # check if other is an instance of account
            if isinstance(other, account):
                # check if other's balance and interestrate is equal to the balance
                # of the calling object
                return self.getBalance() == other.getBalance() and self.getInterestRate() == other.getInterestRate()
        
        return False