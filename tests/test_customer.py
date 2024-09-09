import pytest
from customer import Customer
from coffee import Coffee
from order import Order


def test_customer_name():
    customer = Customer("Jasmine")
    assert customer.name == "Jasmine"
    
def test_customer_name_validation():
    with pytest.raises(ValueError):
        Customer("")
        
def test_has_many_orders():
        coffee = Coffee("Vanilla Latte")
        customer_1 = Customer("Steve")
        customer_2 = Customer("Dima")
        order_1 = Order(customer_1, coffee, 2.0)
        order_2 = Order(customer_1, coffee, 5.0)
        order_3 = Order(customer_2, coffee, 5.0)

        assert len(customer_1.orders()) == 2
        assert len(customer_2.orders()) == 1
        assert order_1 in customer_1.orders()
        assert order_2 in customer_1.orders()
        assert order_3 not in customer_1.orders()
        assert order_3 in customer_2.orders()
        
        
def test_create_order():
        coffee_1 = Coffee("Vanilla Latte")
        coffee_2 = Coffee("Flat White")
        customer_1 = Customer("Steve")
        customer_2 = Customer("Dima")
        order_1 = customer_1.create_order(coffee_1, 2.0)
        order_2 = customer_2.create_order(coffee_2, 5.0)
        
        
        assert isinstance(order_1, Order)
        assert isinstance(order_2, Order)
        
        assert order_1.customer == customer_1
        assert order_1.coffee == coffee_1
        assert order_2.customer == customer_2
        assert order_2.coffee == coffee_2