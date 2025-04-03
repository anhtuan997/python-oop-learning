from bank_account import BankAccount

def test_deposit():
    acc = BankAccount(1000)
    acc.deposit(500)
    assert acc.balance == 1500

def test_withdraw():
    acc = BankAccount(1000)
    acc.withdraw(200)
    assert acc.balance == 800

def test_transfer():
    acc1 = BankAccount(1000)
    acc2 = BankAccount(500)
    acc1.transfer(acc2, 300)
    assert acc1.balance == 700
    assert acc2.balance == 800

if __name__ == "__main__":
    test_deposit()
    test_withdraw()
    test_transfer()
    print("Tất cả test passed!")