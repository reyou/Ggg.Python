class BankAccount:
    def __init___(self):
        self.account_number = 0  # Account number
        self.ssn = 123456789  # Social security number
        self.name = ""  # Customer name
        self.balance = 0.00  # Funds available in the account
        self.min_balance = 100.00  # Balance cannot fall below this amount
        self.active = False  # Account is active or inactive

    def __init___(self, acct, ss, name, balance):
        self.account_number = acct  # Account number
        self.ssn = ss  # Social security number
        self.name = name  # Customer name
        self.balance = balance  # Funds available in the account
        self.min_balance = 100.00  # Balance cannot fall below this amount
        self.active = False  # Account is active or inactive

    def __init__(self, number, ssn, name, balance):
        self.__account_number = number  # Account number
        self.__ssn = ssn  # Social security number
        self.__name = name  # Customer name
        self.__balance = balance  # Funds available in the account
        self.__min_balance = 100  # Balance cannot fall below this amount
        self.__active = True  # Account is active or inactive

    def deposit(self, amount):
        """
        Add funds to the account, if possible
        Return true if successful, false otherwise
        """
        if self.is_active():
            print("Account is active.")
            print("Depositing", amount, end=".")
            self.__balance += amount
            return True  # Successful deposit
        else:
            print("Account is not active.")
            return False  # Unable to deposit into an inactive account

    def withdraw(self, amount):
        """
        Remove funds from the account, if possible
        Return true if successful, false otherwise
        """
        result = False;  # Unsuccessful by default
        print("\nAttempting to withdraw", amount, end=".")
        if self.is_active() and self.__balance - amount >= self.__min_balance:
            self.__balance -= amount;
            print("Withdrawing", amount, end="...")
            print("New Balance", self.__balance, end=".")
            result = True;  # Success
        else:
            print("\nAccount is not active \n"
                  "or you do not have enough balance or \n"
                  "you exceeded minimum balance", self.__min_balance, end=".")
        return result

    def set_active(self, act):
        """
        Activate or deactivate the account
        """

        self.__active = act

    def is_active(self):
        """
        Is the account active or inactive?
        """
        return self.__active


def main():
    acct = BankAccount(31243, 123456789, "Joe", 1000.00)
    acct.deposit(100)
    acct.withdraw(2000.00);


main()
