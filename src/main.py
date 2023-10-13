from account.account import *
from savingsaccount.savingsaccount import *

def main():
    # create an account object named account1 with a balance of 100.0
    # account1 = account(100.0, 200.0, 300.0)
    # account1 = account(-100.0) a balance less than zero will result in our code raising a ValueError
    account1 = account(100.0)

    # print(account1.public) referencing a public instance variable will not result in an error
    # print(account1.__balance) referencing a private instance variable will result in an AttributeError
    # print(account1._protected) referencing a protected instance variable will not result in an error
    # print(account1._account__balance)

    # account1.__privateMethod() referencing a private method will result in an AttributeError
    # account1._account__privateMethod()
    # account1._protectedMethod() referencing a protected method will not result in an error
    # account1.publicMethod() referencing a public method will not result in an error

    # display the balance of account1
    print("$%.2f" % account1.getBalance())

    # increase the balance of account1 by $50
    account1.credit(50.0)
    # account1.credit(-50.0)

    # display the balance of account1
    print("$%.2f" % account1.getBalance())

    # decrease the balance of account1 by $75
    account1.debit(75.0)
    # account1.debit(-75.0)
    # account1.debit(151.0)

    # display the balance of account1
    print("$%.2f" % account1.getBalance())

    # display the balance for account1 is empty
    print("Is account1 empty?", account1.isEmpty())

    # create a seacond balance object named account2 with a balance of 0.0
    account2 = account()

   # display the balance of account2
    print("$%.2f" % account2.getBalance())

    # increase the balance of account2 by $150
    account2.credit(150.0)

    # display the balance of account2
    print("$%.2f" % account2.getBalance())

    # decrease the balance of account2 by $75
    account2.debit(75.0)

    # display the balance of account2
    print("$%.2f" % account2.getBalance())

    # display the balance for account2 is empty
    print("Is account2 empty?", account2.isEmpty())

    # display a string representation of account1 and account2
    print(account1)
    print(account2)

    # create an object named account3 that is equal to None
    account3 = None

    # test if account1 is equal to account3
    print("Is account1 equal to account3?", account1.__eq__(account3))

    # create a string object named s1
    s1 = "I love Python"

    # test if account1 is equal to s1
    print("Is account1 equal to s1?", account1.__eq__(s1))

    # test if account1 is equal to account2
    print("Is account1 equal to account2?", account1.__eq__(account2))

    # change the balance in account2
    account2.credit(75.0)

    # test if account1 is equal to account2
    print("Is account1 equal to account2?", account1.__eq__(account2))

    # display the sum of the balances in account1 and account2
    print("Sum of account1 and account2 balances: $%.2f" % account.sum(account1, account2))

    # display the sum of the balances in account1 and account3
    print("Sum of account1 and account3 balances: $%.2f" % account.sum(account1, account3))

    # display the sum of the balances of account1 and s1
    print("Sum of account1 and s1 balances: $%.2f" % account.sum(account1, s1))

    # transfer $25 out of account1 and put it into a new account named account4
    account4 = account.transfer(account1, 25.0)
    # account4 = account.transfer(account1, -25.0) this line of code results in a ValueError
    # account4 = account.transfer(account1, 2500.0) this line of code results in a ValueError
    # account4 = account.transfer(account3, 25.0)
    # account4 = account.transfer(s1, 25.0)

    # display the balance of account1 and account4
    print("account1 balance: $%.2f" % account1.getBalance())
    print("account4 balance: $%.2f" % account4.getBalance())

    # create a savings account object named savingsAccount1
    # with a balance of 10000.0 and an interest rate of 6%
    savingsAccount1 = savingsaccount(10000.0, 0.06)

    # display the balance of savingsAccount1
    print(f"Balance in savingsAccount1 {savingsAccount1.getBalance()}")

    # display the interest of savingsAccount1
    print(f"Interest of savingsAccount1 {savingsAccount1.getInterest()}")

    # display if the balance of savingsAccount1 is empty
    print("Is savingsAccount1 empty?", savingsAccount1.isEmpty())

    # display a string representation of savingsAccount1
    print(savingsAccount1)

    # display the result of testing if savingsAccount1 is equal to account1
    print("Is savingsAccount1 equal to account1?", savingsAccount1.__eq__(account1))

    # display the result of testing if savingsAccount1 is equal to account3
    print("Is savingsAccount1 equal to account3?", savingsAccount1.__eq__(account3))

    # create a savings account object named savingsAccount2 
    # with a balance of 10000.0 and an interest rate of 5%
    savingsAccount2 = savingsaccount(10000.0, 0.05)

    # display the result of testing if savingsAccount1 is equal to savingsAccount2
    print("Is savingsAccount1 equal to savingsAccount2?", savingsAccount1.__eq__(savingsAccount2))

    # change the interest rate of savingsAccount2 to 6%
    savingsAccount2.setInterestRate(0.06)

    # display the result of testing if savingsAccount1 is equal to savingsAccount2
    print("Is savingsAccount1 equal to savingsAccount2?", savingsAccount1.__eq__(savingsAccount2))

    # credit savingsAccount2 with $1000
    savingsAccount2.credit(1000.0)

    # display the balance of savingsAccount2
    print("$%.2f" % savingsAccount2.getBalance())

    # debit savingsAccount2 with $1000
    savingsAccount2.debit(1000.0)

if __name__ == "__main__":
    main()