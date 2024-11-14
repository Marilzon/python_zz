import pytest
from bankaccount_poo import BankAccount, Bank


def test_deposit():
    voli_account = BankAccount("Volibear", 100)
    voli_account.deposit(50)
    assert voli_account.get_amount() == 150


def test_withdraw():
    singed_account = BankAccount("Singed", 100)
    message = singed_account.withdraw(50)
    assert singed_account.get_amount() == 50
    assert message == "Withdraw of 50 success"


def test_withdraw_insuficient_amount():
    trundle_account = BankAccount("Trundle", 500)
    message = trundle_account.withdraw(50000)
    assert trundle_account.get_amount() == 500
    assert message == "Insuficient amount: 500"


def test_add_account():
    bank = Bank()
    marilzon_account = BankAccount("Marilzon", 1000)
    bank.add_account(marilzon_account)
    assert bank.list_accounts() == [("Marilzon", 1000)]


def test_list_accounts():
    bank = Bank()
    voli_account = BankAccount("Volibear", 500)
    master_yi_account = BankAccount("MasterYI", 500)

    bank.add_account(voli_account)
    bank.add_account(master_yi_account)

    assert bank.list_accounts() == [("Volibear", 500), ("MasterYI", 500)]
