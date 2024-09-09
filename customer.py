# Customer class
class Customer:
    
    all_customers = []  # To keep track of all Customer instances created 
    
    # Initialize class
    def __init__(self, name):
        if isinstance (name, str) and 1 <= len(name) <= 15:
            self._name = name
            self._orders = []
            Customer.all_customers.append(self)
            
        else:
            raise ValueError("Name should be a string between 1 and 15 characters")
        
    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self, new_customer):
        if isinstance (new_customer, str) and 1 <= len(new_customer) <= 15:
            self._name = new_customer
        else:   
            raise ValueError("Name should be a string between 1 and 15 characters")
            
    # To return the specific customer orders        
    def orders(self):
        return self._orders
    
    # To get a unique list of the coffee orders of the specific customer
    def coffees(self):
        return [{order.coffee for order in self._orders}]
     
    # To create an order   
    def create_order(self, coffee, price):
        from order import Order
        new_order = Order(customer = self, coffee = coffee, price = price)
            
        return new_order
    
    def __repr__(self):
        return self.name
    
    
# customer1 = Customer("Robert")
# customer2 = Customer("Nicole")
# customer3 = Customer("a")
# customer4 = Customer("Bruno")

# print(customer1)
# print(Customer.all_customers)
# print(f"{customer1}'s Order: {[(order.coffee.name, order.price) for order in customer1.orders()]}")
# print(f"{customer2}'s Order: {[(order.coffee.name, order.price) for order in customer2.orders()]}")

# customer1.add_order("Mocha")
# customer1.add_order("Latte")
# order1 = customer1.create_order("Cappuccino", 2.0)
# print(customer1.orders())
# print(customer1.coffees())
