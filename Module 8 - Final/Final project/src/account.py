class Account:
    def __init__(self, account_number, first_name, last_name, ssn, pin):
        self.account_number = account_number
        self.first_name = first_name
        self.last_name = last_name
        self.ssn = ssn
        self.pin = pin
        self.balance = 0

    def deposit(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if isinstance(amount, (int, float)) and amount > 0 and amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def is_valid_pin(self, pin):
        return self.pin == pin

    def __str__(self):
        return f"Account #{self.account_number}\nOwner: {self.first_name} {self.last_name}\nSSN: {self.ssn}\nBalance: ${self.balance:.2f}"
