import pytest
from coffee import Coffee
from customer import Customer

def test_coffee_name():
    coffee = Coffee("Mocha")
    assert coffee.name == "Mocha"
    
def test_coffee_name_validation():
    with pytest.raises(ValueError):
        Coffee("Mo")
        
def test_num_orders():
    coffee = Coffee("Mocha")
    customer = Customer("Jasmine")
    customer.create_order(coffee, 4.0)
    assert coffee.num_orders() == 1
    
def test_average_price():
    coffee = Coffee("Mocha")
    customer = Customer("Jasmine")
    customer.create_order(coffee, 4.0)
    assert coffee.average_price() == 4.0
    