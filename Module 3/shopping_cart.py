class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item_name, item_price):
        self.items.append((item_name, item_price))

    def total_cost(self):
        total = 0
        for item_in_cart in self.items:
            total += item_in_cart[1]
        return total

cart = ShoppingCart()
cart.add_item("apple", 1.0)
cart.add_item("banana", 0.5)
cart.add_item("orange", 0.75)
print("Total cost:", cart.total_cost())
