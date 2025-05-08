class CoinCollector:
    @staticmethod
    def validate_change_string(change_str):
        valid_coins = {'P', 'N', 'D', 'Q', 'H', 'W'}
        for coin in str(change_str).upper():
            if coin not in valid_coins:
                return False
        return True

    @staticmethod
    def parse_change(change_str):
        # Parses a string of coins and returns the total in cents
        values = {'P': 0.01, 'N': 0.05, 'D': 0.10, 'Q': 0.25, 'H': 0.50, 'W': 1.00}
        total = 0
        for coin in str(change_str).upper():
            if coin in values:
                total += values[coin]
        return total
