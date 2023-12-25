class Account():

    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance


def main():
    account = Account()
    # here "account" is object and Account() represents the constructor used to create an instance of the Account
    print("Blc: ", account._balance)
    account.deposit(100)
    account.withdraw(50)
    print("New Blc: ", account._balance)


if __name__ == "__main__":
    main()
