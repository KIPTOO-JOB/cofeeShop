

class Customer:
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
        if not isinstance(self._name, str) or not (1 <= len(self._name) <= 15):
            raise ValueError("Name must be a string between 1 and 15 characters.")

    def orders(self):
        return self._orders

    def coffees(self):
        return list({order.coffee for order in self._orders})

    def create_order(self, coffee, price):
        order = Order(self, coffee, price)
        self._orders.append(order)
        return order

    def __str__(self):
        return f"Customer(name={self.name}, orders={len(self._orders)}, coffees={self.coffees()})"
    

customer1 = Customer("Job")
print(customer1)