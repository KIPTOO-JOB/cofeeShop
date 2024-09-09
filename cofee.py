class Coffee:
    def __init__(self, name):
        self._orders = []
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not hasattr(self, "_name") and isinstance(value, str) and len(value) >= 3:
            self._name = value
        else:
            raise ValueError("Name must be a string with at least 3 characters.")

    def orders(self):

        return self._orders

    def customers(self):
        unique_customers = []
        for order in self._orders:
            if order.customer not in unique_customers:
                unique_customers.append(order.customer)
        return unique_customers

    def num_orders(self):
        return len(self._orders)

    def average_price(self):
        if len(self._orders) == 0:
            return 0

        total_price = sum(order.price for order in self._orders)
        return total_price / len(self._orders)
    
    def __repr__(self):
        return f"Coffee(name={self._name})"