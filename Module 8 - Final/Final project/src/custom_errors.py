# custom_errors.py
# Defines custom exceptions for the banking application

class AccountNotFoundError(Exception):
    def __init__(self):
        super().__init__("Account not found.")

class IncorrectPinError(Exception):
    def __init__(self):
        super().__init__("Incorrect PIN.")

class InsufficientFundsError(Exception):
    def __init__(self):
        super().__init__("You do not have the required balance to conduct this transaction. Please try again.")

class InvalidAccountNumberError(Exception):
    def __init__(self):
        super().__init__("Invalid account number.")

class InvalidSSNError(Exception):
    def __init__(self):
        super().__init__("Invalid social security number. Please enter a 9-digit number.")

class InvalidPinFormatError(Exception):
    def __init__(self):
        super().__init__("Invalid PIN format. Please enter a 4-digit numeric PIN.")
