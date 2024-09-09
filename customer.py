class Customer:
    all_customers = []

    def __init__(self, name):
        self.name = name
        self._orders = []
        Customer.all_customers.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Name must be a string between 1 and 15 characters")


    def orders(self):
        """Returns a list of all orders for this customer"""
        return self._orders

    def coffees(self):
        """Returns a unique list of all coffees a customer has ordered"""
        unique_coffees = []
        for order in self._orders:
            if order.coffee not in unique_coffees:
                unique_coffees.append(order.coffee)
        return unique_coffees

    def new_order(self, coffee, price):
        """Creates a new Order instance and associates it with this customer and the provided coffee"""
        from order import Order  # Import here to avoid circular import
        order = Order(self, coffee, price)
        self._orders.append(order)
        coffee._orders.append(order)
        return order

    @classmethod
    def most_aficionado(cls, coffee):
        """Returns the customer that has spent the most money on a given coffee instance"""
        spending_by_customer = {}

        for customer in cls.all_customers:
            total_spent = sum(order.price for order in customer.orders() if order.coffee == coffee)
            if total_spent > 0:
                spending_by_customer[customer] = total_spent

        if spending_by_customer:
            max_spender = max(spending_by_customer, key=spending_by_customer.get)
            return max_spender
        else:
            return None
    
    def __repr__(self):
        return f"Customer(name={self._name})"