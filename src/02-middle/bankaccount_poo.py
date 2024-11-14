class BankAccount:
    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount

    def deposit(self, quantity):
        self.amount += quantity

    def withdraw(self, quantity):
        if quantity > self.amount:
            return f"Insuficient amount: {self.amount}"
        else:
            self.amount -= quantity
            return f"Withdraw of {quantity} success"

    def get_amount(self):
        return self.amount


class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def list_accounts(self):
        return [(account.owner, account.amount) for account in self.accounts]
