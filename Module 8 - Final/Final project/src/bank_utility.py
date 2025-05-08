import random

class BankUtility:
    @staticmethod
    def prompt_for_positive_float(prompt):
        while True:
            try:
                value = float(input(prompt))
                if value > 0:
                    return value
            except ValueError:
                pass
            print("Please enter a positive number.")

    @staticmethod
    def prompt_for_atm_amount(prompt):
        while True:
            try:
                value = int(input(prompt))
                if value > 0 and value % 5 == 0 and value <= 1000:
                    return value
                else:
                    print("Invalid amount.")
            except ValueError:
                    print("Invalid amount.")

    @staticmethod
    def prompt_for_change_string(prompt):
        while True:
            try:
                value = int(input(prompt))
                if value > 0 and value % 5 == 0 and value <= 1000:
                    return value
                else:
                    print("Invalid amount.")
            except ValueError:
                    print("Invalid amount.")

    @staticmethod
    def validate_ssn(ssn):
        if len(ssn) == 9 and str(ssn).isdigit():
            return True
        return False
    
    @staticmethod
    def validate_pin(pin):
        if len(pin) == 4 and str(pin).isdigit():
            return True
        return False

    @staticmethod
    def convert_from_dollars_to_cents(amount):
        return int(round(amount * 100))

    @staticmethod
    def generate_new_account_number(accounts):
        new_num = random.randint(100000000, 999999999)
        for acct in accounts:
            if acct.account_number == new_num:
                return BankUtility.generate_new_account_number(accounts)
        return new_num
