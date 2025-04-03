class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("So tien khong hop le")

    def transfer(self, target_account, amount):
        if self.balance >= amount:
            self.__balance -= amount
            target_account.__balance += amount
            return True
        else:
            return False

    @property
    def balance(self):
        return self.__balance
    def __str__(self):
        return f"so du: {self.__balance}"


#test
if __name__ == "__main__":
    account = BankAccount(1000)
    account.deposit(500)
    account.withdraw(200)

    print(account)

