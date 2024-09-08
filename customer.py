from order import Order

class Customer:
    
    all_customers = []
    
    def __init__(self, name):
        if not isinstance (name, str) and 1 > len(name) > 15:
            raise ValueError("Name should be a string between 1 and 15 characters")
        
        self._name = name
        self._orders = []
        Customer.all_customers.append(self)
        
    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self, new_customer):
        if not isinstance (new_customer, str) and 1 > len(new_customer) > 15:
            raise ValueError("Name should be a string between 1 and 15 characters")
            
        self._name = new_customer
            
        
    def add_order(self, order):
        self._orders.append(order)
            
    def orders(self):
        return self._orders
        
    def coffees(self):
        return [order.coffee for order in self._orders]
        
    def create_order(self, coffee, price):
        new_order = Order(customer = self, coffee = coffee, price = price)
        self.add_order(new_order)
        coffee.add_order(new_order)
            
        return new_order