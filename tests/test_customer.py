import pytest
from customer import Customer
from coffee import Coffee

def test_customer_name():
    customer = Customer("Jasmine")
    assert customer.name == "Jasmine"
    
def test_customer_name_validation():
    with pytest.raises(ValueError):
        Customer("w")
        
def test_create_order():
    customer = Customer("Jasmine")
    coffee = Coffee("Mocha")
    order = customer.create_order(coffee, 4.0)
    assert order.coffee == coffee
    assert order.price == 4.0
    assert customer.order() == [order]