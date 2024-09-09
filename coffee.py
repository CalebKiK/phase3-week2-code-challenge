# Coffee class
class Coffee:

    all_coffees = []  # To keep track of all Coffee instances created

    # Initialize a Coffee instance
    def __init__(self, name):
        if len(name) < 3:
            raise ValueError("Coffee name string should be at least 3 characters")

        self._name = name
        self._orders = []
        Coffee.all_coffees.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) >= 3:
            self._name = value
        else:
            raise ValueError('Coffee name string should be at leats 3 characters')

    # Getting all the orders of a specific Coffee instance
    def orders(self):
        return self._orders

    # To get a unique list of the specific customers who ordered specific coffee
    def customers(self):
        return [{order.customer for order in self._orders}]

    # To calculate the number of orders of a specific Coffee instance
    def num_orders(self):
        return len(self._orders)

    # To calculate the average price of coffee orders
    def average_price(self):
        if self._orders:
            total_price = sum(order.price for order in self._orders)
            return total_price / len(self._orders)
        return 0.0
    
    def __repr__(self):
        return self.name
    
coffee1 = Coffee("Mocha")
coffee2 = Coffee("Cappuccino")
coffee3 = Coffee("Latte")
# coffee4 = Coffee("am")

# print(Coffee.all_coffees)
