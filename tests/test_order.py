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
    
def test_customer_validation():
    with pytest.raises(Exception):
        Customer("Anne")
    
def test_coffee_validation():
    with pytest.raises(Exception):
        Coffee("Robusta")
    
def test_price_validation():
    with pytest.raises(Exception):
        price = 12.0