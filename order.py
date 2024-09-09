from coffee import Coffee
from customer import Customer

class Order:
    
    # Initialize Order instances and checking if they follow certian guidelines
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
        customer._orders.append(self)
        coffee._orders.append(self)
        
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
    
    
    
customer1 = Customer("Robert")
customer2 = Customer("Nicole")
customer3 = Customer("a")
customer4 = Customer("Bruno")

coffee1 = Coffee("Mocha")
coffee2 = Coffee("Cappuccino")
coffee3 = Coffee("Latte")
# coffee4 = Coffee("am")

order1 = Order(customer1, coffee1, 3.5)
# order2 = Order("Sally", coffee3, 2.0)
order3 = customer2.create_order(coffee2, 5.0)
# order4 = customer4.create_order("Iced Coffee", 8.0)
order5 = Order(customer2, coffee3, 2.0)
order6 = customer1.create_order(coffee2, 5.0)
        
        