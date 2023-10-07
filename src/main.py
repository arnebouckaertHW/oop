from account.account import *

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

    

if __name__ == "__main__":
    main()