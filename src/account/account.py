from transaction.transaction import *

class account(transaction):
    """The Account class includes methods to manage the balance
    of a bank account.

    Args:
        transaction (transaction): abstract class that defines methods 
        that may be implemented by an account class.
    """

    def __init__(self, *args):
        """Constructs an account with a specified balance if args length is 1,
        else constructs an account with a balance of 0.

        :ivar __balance: balance of this account

        Raises:
            ValueError: indicates args[0] is less than 0.
        """

        # print(args)
        if len(args) == 1:
            try:
                if args[0] < 0.0:
                    raise ValueError("Balance is less than zero")
            except ValueError as e:
                exit(e)
            finally:
                self.__balance = float(args[0]) # this is a private instance variable
                self.public = 'public'          # this is a public instance variable
                self._protected = 'protected'    # this is a protected instance variable
        else:
            self.__balance = 0.0
    
    def __privateMethod(self):
        print('Private method')

    def _protectedMethod(self):
        print('Protected method')

    def publicMethod(self):
        print('Public method')

    """def __del__(self):
        print('Account destroyed')"""
    
    def getBalance(self):
        """Returns the balance of the calling account.

        Returns:
            float: the balance
        """

        return self.__balance
    
    def isEmpty(self):
        """Check if the balance of the calling account is 0

        Returns:
            bool: is balance of calling account 0, True if 0, else False
        """
        return self.__balance == 0
    
    def credit(self, amount: float):
        """Increases the balance of the calling account by the specified amount.

        Args:
            amount (float): the amount to be credited to the calling account

        Raises:
            ValueError: indicates amount is less than 0
        """

        try:
            if amount < 0.0:
                raise ValueError("Credit amount is less than zero")
        except ValueError as e:
            exit(e)
        finally:
            self.__balance += amount

    def debit(self, amount: float):
        """Decreases the balance of the calling account by the specified amount.

        Args:
            amount (float): the amount to be debited from the calling account

        Raises:
            ValueError: indicates amount is less than 0
            ValueError: indicates amount is greater than the balance of the calling account
        """

        try:
            if amount < 0.0:
                raise ValueError("Debit amount is less than zero")
            
            if amount > self.__balance:
                raise ValueError("Debit amount exceeded account balance")
        except ValueError as e:
            exit(e)
        finally:
            self.__balance -= amount

    def __str__(self):
        """Returns string representation of the calling account.

        Returns:
            str: string representation of the calling account
        """
        return f"Account balance: {self.__balance}"
    
    def __eq__(self, other):
        """Checks wether the provided account is equal to the calling account.

        Args:
            other (account): the account to compare

        Returns:
            bool: True if the balance of the accounts is equal, else False
        """

        # check if other is not None
        if other is not None:
            # check if other is an instance of account
            if isinstance(other, account):
                # check if other's balance is equal to the balance
                # of the calling object
                return self.__balance == other.__balance
        
        return False
    
    @staticmethod
    def sum(account1, account2):
        """Returns the sum of the balances of the provided accounts.

        Args:
            account1 (account): first account
            account2 (account): second account

        Returns:
            float: If either accounts are None or not an instance of account it is 0, 
            else the sum of the balances of the provided accounts
        """

        if account1 is None or account2 is None:
            return 0.0
        elif not isinstance(account1, account) or not isinstance(account2, account):
            return 0.0
        else:
            return account1.__balance + account2.__balance
    
    @staticmethod
    def transfer(a, amount: float):
        """Adds the specified amount to a new account object and debits 
        the amount from the specified account object.

        Args:
            a (account): specified account object to be debited
            amount (float): debit amount

        Raises:
            ValueError: indicates debit amount is less than zero
            ValueError: indicates account is None
            ValueError: indicates account is not an account type
            ValueError: indicates debit amount is greater than the balance
            in the specified account object to be debited
            
        Returns:
            account: new account object
        """
        
        try:
            if amount < 0.0:
                raise ValueError("Transfer amount is less than zero")
            elif a is None:
                raise ValueError("a is None")
            elif not isinstance(a, account):
                raise ValueError("a is not an instance of account")
            elif amount > a.getBalance():
                raise ValueError("Transfer amount exceeded account balance")
        except ValueError as e:
            exit(e)
        else:
            a.debit(amount)
            newAccount = account(amount)
            return newAccount

    