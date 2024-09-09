import pytest
from order import Order
from coffee import Coffee
from customer import Customer

def test_order_initialization():
    customer = Customer("Jasmine")
    coffee = Coffee("Mocha")
    order = Order(customer, coffee, 4.0)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 4.0

def test_has_price():
    coffee = Coffee("Latte")
    customer = Customer('Sharon')
    order_1 = Order(customer, coffee, 2.0)
    order_2 = Order(customer, coffee, 5.0)

    assert (order_1.price == 2.0)
    assert (order_2.price == 5.0)
    
def test_price_is_valid():
    coffee = Coffee("Mocha")
    customer = Customer('Steve')
    order_1 = Order(customer, coffee, 2.0)
    order_2 = Order(customer, coffee, 5.0)
        
    assert isinstance(order_1.price, float)
    assert isinstance(order_2.price, float)
    
def test_has_a_customer():
    coffee = Coffee("Mocha")
    customer_1 = Customer('Wayne')
    customer_2 = Customer('Dima')
    order_1 = Order(customer_1, coffee, 2.0)
    order_2 = Order(customer_2, coffee, 5.0)

    assert (order_1.customer == customer_1)
    assert (order_2.customer == customer_2)

def test_customer_of_type_customer():
    coffee = Coffee("Vanilla Latte")
    customer_1 = Customer('Wayne')
    customer_2 = Customer('Dima')
    order_1 = Order(customer_1, coffee, 2.0)
    order_2 = Order(customer_2, coffee, 5.0)

    assert (isinstance(order_1.customer, Customer))
    assert (isinstance(order_2.customer, Customer))
    
def test_has_a_coffee():
    coffee_1 = Coffee("Mocha")
    coffee_2 = Coffee("Peppermint Chai")
    customer = Customer('Wayne')
    order_1 = Order(customer, coffee_1, 2.0)
    order_2 = Order(customer, coffee_2, 5.0)

    assert (order_1.coffee == coffee_1)
    assert (order_2.coffee == coffee_2)

def test_coffee_of_type_coffee():
    coffee_1 = Coffee("Vanilla Latte")
    coffee_2 = Coffee("Peppermint Chai")
    customer = Customer('Steve')
    order_1 = Order(customer, coffee_1, 2.0)
    order_2 = Order(customer, coffee_2, 5.0)

    assert (isinstance(order_1.coffee, Coffee))
    assert (isinstance(order_2.coffee, Coffee))
