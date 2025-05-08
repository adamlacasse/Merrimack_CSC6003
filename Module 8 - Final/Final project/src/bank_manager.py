from bank import Bank
from account import Account
from bank_utility import BankUtility
from coin_collector import CoinCollector

class BankManager:
    @staticmethod
    def main():
        bank = Bank()
        while True:
            print("\nMain Menu:")
            print("1. Open an account")
            print("2. Get account information and balance")
            print("3. Change PIN")
            print("4. Deposit money in account")
            print("5. Transfer money between accounts")
            print("6. Withdraw money from account")
            print("7. ATM withdrawal")
            print("8. Deposit change")
            print("9. Close an account")
            print("10. Add monthly interest to all accounts")
            print("11. End Program")

            choice = input("Select an option: ")
            if choice == '11':
                print("Thank you for using the banking app!")
                return

            if choice == '1':
                bank.can_account_be_opened()
                if not bank.can_account_be_opened():
                    print("Sorry, the bank is at full capacity.")
                    continue

                first = input("First name: ")
                last = input("Last name: ")

                while True:
                    ssn = input("Social Security Number (9 digits): ")
                    if BankUtility.validate_ssn(ssn):
                        break
                    print("Invalid SSN. Please enter a 9-digit number.")

                while True:
                    pin = input("Choose a 4-digit PIN: ")
                    if BankUtility.validate_pin(pin):
                        break
                    print("Invalid PIN. Please enter a 4-digit number.")

                acct_num = str(BankUtility.generate_new_account_number(bank.accounts))
                account = Account(acct_num, first, last, ssn, pin)
                bank.add_account_to_bank(account)
                print(f"Account created! Your account number is: {acct_num}")
            elif choice == '2':
                account = BankManager.prompt_for_account_number_and_pin(bank)
                if account:
                    print(account)
            elif choice == '3':
                account = BankManager.prompt_for_account_number_and_pin(bank)
                if account:
                    while True:
                        new_pin = input("Enter new 4-digit PIN: ")
                        if BankUtility.validate_pin(new_pin):
                            account.pin = new_pin
                            print("PIN changed successfully.")
                            break
                        print("Invalid PIN. Please enter a 4-digit number.")
            elif choice == '4':
                account = BankManager.prompt_for_account_number_and_pin(bank)
                if account:
                    amount = BankUtility.prompt_for_positive_float("Enter amount to deposit: ")
                    if account.deposit(amount):
                        print(f"Deposited ${amount:.2f} into account {account.account_number}.")
                        print(f"New balance: ${account.balance:.2f}")
                    else:
                        print("Deposit failed.")
            elif choice == '5':
                from_account = BankManager.prompt_for_account_number_and_pin(bank)
                if from_account:
                    to_account = BankManager.prompt_for_account_number_and_pin(bank)
                    if to_account:
                        amount = BankUtility.prompt_for_positive_float("Enter amount to transfer: ")
                        if from_account.withdraw(amount):
                            to_account.deposit(amount)
                            print(f"Transferred ${amount:.2f} from account {from_account.account_number} to account {to_account.account_number}.")
                            print(f"New balance for {from_account.account_number}: ${from_account.balance:.2f}")
                            print(f"New balance for {to_account.account_number}: ${to_account.balance:.2f}")
                        else:
                            print("Transfer failed.")
            elif choice == '6':
                account = BankManager.prompt_for_account_number_and_pin(bank)
                if account:
                    amount = BankUtility.prompt_for_positive_float("Enter amount to withdraw: ")
                    if account.withdraw(amount):
                        print(f"Withdrew ${amount:.2f} from account {account.account_number}.")
                        print(f"New balance: ${account.balance:.2f}")
                    else:
                        print("Withdrawal failed.")
            elif choice == '7':
                account = BankManager.prompt_for_account_number_and_pin(bank)
                if account:
                    amount = BankUtility.prompt_for_atm_amount("Enter amount to withdraw (in five dollar increments, up to $1,000): ")
                    if account.withdraw(amount):
                        print(f"ATM withdrawal of ${amount:.2f} from account {account.account_number}.")
                        print(f"New balance: ${account.balance:.2f}")
                    else:
                        print("ATM withdrawal failed.")
            elif choice == '8':
                account = BankManager.prompt_for_account_number_and_pin(bank)
                if account:
                    change_string = input("Enter your coins to deposit(P, N, D, Q, H, W); one letter per coin: ")
                    if not CoinCollector.validate_change_string(change_string):
                        print("Invalid coin string. Please use only P, N, D, Q, H, W.")
                        continue
                    amount = CoinCollector.parse_change(change_string)
                    if amount == 0:
                        print("No valid coins entered.")
                        continue
                    if account.deposit(amount):
                        print(f"Deposited ${amount:.2f} in change into account {account.account_number}.")
                        print(f"New balance: ${account.balance:.2f}")
                    else:
                        print("Deposit failed.")
            elif choice == '9':
                account = BankManager.prompt_for_account_number_and_pin(bank)
                if account:
                    print(f"Account {account.account_number} will be closed.")
                    print(f"The closing balance is: ${account.balance:.2f}")
                    if bank.remove_account_from_bank(account.account_number):
                        print(f"Account {account.account_number} closed successfully.")
                    else:
                        print("Failed to close account. Please try again.")
            else:
                print("Need to figure this out")

    @staticmethod
    def prompt_for_account_number_and_pin(bank):
        account_number = input("Enter account number: ")
        account = bank.find_account(account_number)
        if account:
            pin = input("Enter PIN: ")
            if account.is_valid_pin(pin):
                return account
            else:
                print("Incorrect PIN.")
                return None
        else:
            print("Account not found.")
            return None
        
if __name__ == "__main__":
    BankManager.main()

