class Coffee:
    def __init__(self, name):
        self.name = name  
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        self._validate_name()

    def _validate_name(self):
        if not isinstance(self._name, str) or len(self._name) < 3:
            raise ValueError("Name must be a string with at least 3 characters.")

    def orders(self):
        return self._orders

    def customers(self):
        return list({order.customer for order in self._orders})

    def num_orders(self):
        return len(self._orders)

    def average_price(self):
        if not self._orders:
            return 0
        total_price = sum(order.price for order in self._orders)
        return total_price / len(self._orders)

    def __str__(self):
        return f"Coffee(name={self.name})"
    
# Example usage
if __name__ == "__main__":
    coffee1 = Coffee("Latte")
    print(coffee1)