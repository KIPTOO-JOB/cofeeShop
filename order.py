from customer import Customer
from coffee import Coffee
class Order:
    def __init__(self, customer, coffee, price):
        self.customer = customer  
        self.coffee = coffee      
        self.price = price       

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
        self._validate_price()

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        if not isinstance(value, Customer):
            raise ValueError("Customer must be an instance of Customer class.")
        self._customer = value

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        if not isinstance(value, Coffee):
            raise ValueError("Coffee must be an instance of Coffee class.")
        self._coffee = value

    def _validate_price(self):
        if not isinstance(self._price, (int, float)) or not (1.0 <= self._price <= 10.0):
            raise ValueError("Price must be a number between 1.0 and 10.0.")

    def __str__(self):
        return (f"Order(customer={self.customer.name}, coffee={self.coffee.name}, "
                f"price={self.price:.2f})")
    
# Example usage
if __name__ == "__main__":
    customer = Customer("JOB")
    coffee = Coffee("Latte")
    order = Order(customer, coffee, 4.5)
    print(order)