from customer import Customer
from coffee import Coffee
from order import Order

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
order3 = customer2.create_order(coffee1, 5.0)
# order4 = customer4.create_order("Iced Coffee", 8.0)
order5 = Order(customer2, coffee3, 2.0)
order6 = customer1.create_order(coffee3, 5.0)

print(Customer.all_customers)
print(Coffee.all_coffees)
print(order1.order_details())

print(coffee3.orders())
print(coffee3.customers())

print(f"{customer1}'s Order: {[(order.coffee.name, order.price) for order in customer1.orders()]}")
print(f"{customer2}'s Order: {[(order.coffee.name, order.price) for order in customer2.orders()]}")

print(f"{coffee3} has {coffee3.num_orders()} orders and has an average price of {coffee3.average_price()}")
print(f"{coffee2} has {coffee2.num_orders()} orders and has an average price of {coffee2.average_price()}")
print(customer1.orders())
print(customer1.coffees())