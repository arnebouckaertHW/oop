from abc import ABC, abstractmethod

class transaction:
    """The transaction class is an abstract class that defines the methods that may be implemented by an Account class.
    """
    @abstractmethod
    def getBalance(self):
        """Return the current balance of this account.
        """
        pass

    @abstractmethod
    def isEmpty(self):
        """Check if the balance for this account is zero. Return True if the balance is zero, False otherwise.
        """
        pass

    @abstractmethod
    def credit(self, amount: float):
        """Increases the balance of this account by the amount specified.

        Args:
            amount (float): the amount to increase the balance by.
        """
        pass

    @abstractmethod
    def debit(self, amount: float):
        """Decreases the balance of this account by the amount specified.

        Args:
            amount (float): the amount to decrease the balance by.
        """
        pass