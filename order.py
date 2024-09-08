from coffee import Coffee
from customer import Customer

class Order:
    def __init__(self, customer, coffee, price):
        if not isinstance (customer, Customer):
            raise Exception("customer should be a Customer instance")
        if not isinstance (coffee, Coffee):
            raise Exception("coffee should be a Coffee instance")
        if not isinstance(price, float) or 1.0 > price > 10.0:
            raise Exception("coffee price should be more than 1.0 and less than 10.0")
        
        self._customer = customer
        self._coffee = coffee
        self._price = price
        customer.add_order(self)
        coffee.add_order(self)
        
    @property
    def customer(self):
        return self._customer
        
    @customer.setter
    def customer(self, value):
        if not isinstance (value, Customer):
            raise Exception("customer should be a Customer instance")
            
        self._customer = value
            
    @property
    def coffee(self):
        return self._coffee
        
    @coffee.setter
    def coffee(self, value):
        if not isinstance (value, Coffee):
            raise Exception("coffee should be a Coffee instance")
            
        self._coffee = value
            
    @property
    def price(self):
        return self._price
        
    @price.setter
    def price(self, value):
        if not isinstance(value, float) and 1.0 > value > 10.0:
            raise Exception("coffee price should be more than 1.0 and less than 10.0")
            
        self._price = value
            
    def order_details(self):
        return f"Customer name: {self._customer.name}, Coffee: {self._coffee.name}, Price: {self.price:.2f}"
        
        