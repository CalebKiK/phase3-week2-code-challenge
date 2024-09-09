import pytest
from coffee import Coffee
from customer import Customer
from order import Order


def test_coffee_name():
    coffee = Coffee("Mocha")
    assert coffee.name == "Mocha"
    
def test_coffee_name_validation():
    with pytest.raises(ValueError):
        Coffee("Mo")

def test_has_many_orders():
    coffee_1 = Coffee("Hazelnut Latte")
    coffee_2 = Coffee("Mocha")
    customer = Customer("Steve")
    order_1 = Order(customer, coffee_1, 2.0)
    order_2 = Order(customer, coffee_1, 5.0)
    order_3 = Order(customer, coffee_2, 5.0)

    assert len(coffee_1.orders()) == 2
    assert len(coffee_2.orders()) == 1
    assert order_1 in coffee_1.orders()
    assert order_2 in coffee_1.orders()
    assert order_3 not in coffee_1.orders()
    assert order_3 in coffee_2.orders()
             
def test_get_number_of_orders():
    coffee_1 = Coffee("Mocha")
    coffee_2 = Coffee("Vanilla Latte")
    customer = Customer("Steve")
    Order(customer, coffee_1, 2.0)
    Order(customer, coffee_1, 5.0)

    assert coffee_1.num_orders() == 2
    assert coffee_2.num_orders() == 0
    
def test_average_price():
    coffee = Coffee("Mocha")
    customer = Customer("Jasmine")
    customer.create_order(coffee, 4.0)
    assert coffee.average_price() == 4.0
    