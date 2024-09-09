class Order:
    def __init__(self, customer, coffee, price):
        from customer import Customer  # Import here to avoid circular import
        from coffee import Coffee  # Import here to avoid circular import
        self.customer = customer
        self.coffee = coffee
        self.price = price
        
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if isinstance(value, float) and 0.0 <= value <= 10.0:
            self._price = value
        else:
            raise ValueError("Price must be a float between 0.0 and 10.0.")

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        from customer import Customer  # Import here to avoid circular import
        if isinstance(value, Customer):
            self._customer = value
        else:
            raise ValueError("Customer must be an instance of Customer.")

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        from coffee import Coffee  # Import here to avoid circular import
        if isinstance(value, Coffee):
            self._coffee = value
        else:
            raise ValueError("Coffee must be an instance of Coffee.")
    
    def __repr__(self):
        return f"Order(customer={self.customer.name}, coffee={self.coffee.name}, price={self.price})"