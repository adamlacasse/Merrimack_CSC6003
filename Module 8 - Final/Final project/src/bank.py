class Bank:
    def __init__(self, max_accounts = 100):
        self.accounts = []
        self.max_accounts = max_accounts

    def can_account_be_opened(self):
        return len(self.accounts) < self.max_accounts

    def add_account_to_bank(self, account):
        self.accounts.append(account)
        return True

    def remove_account_from_bank(self, account_number):
        for i, acc in enumerate(self.accounts):
            if acc.account_number == account_number:
                del self.accounts[i]
                return True
        return False

    def find_account(self, account_number):
        for acc in self.accounts:
            if str(acc.account_number) == str(account_number):
                return acc
        return None

    def add_monthly_interest(self, annual_rate):
        if self.accounts == []:
            print("No accounts to add interest to!")
            return
        for acc in self.accounts:
            interest = int(acc.balance * (annual_rate / 100) / 12)
            acc.deposit(interest)
            print(f"Monthly interest added to account {acc.account_number}.")
            print(f"New balance: ${acc.balance:.2f}")
