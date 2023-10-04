from account.account import *

def main():
    # create an account object named account1 with a balance of 100.0
    # account1 = account(100.0, 200.0, 300.0)
    # account1 = account(-100.0) a balance less than zero will result in our code raising a ValueError
    account1 = account(100.0)
    account2 = account()

    # print(account1.public) referencing a public instance variable will not result in an error
    # print(account1.__balance) referencing a private instance variable will result in an AttributeError
    # print(account1._protected) referencing a protected instance variable will not result in an error
    # print(account1._account__balance)

    # account1.__privateMethod() referencing a private method will result in an AttributeError
    # account1._account__privateMethod()
    # account1._protectedMethod() referencing a protected method will not result in an error
    # account1.publicMethod() referencing a public method will not result in an error


if __name__ == "__main__":
    main()