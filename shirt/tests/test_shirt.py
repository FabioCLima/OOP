from pathlib import Path
import sys

current_dir = Path(__file__).resolve().parent
parent_dir = current_dir.parent
sys.path.append(str(parent_dir))

from OOP.shirt.shirt_v3 import Shirt


# Test of attributes of new object
def test_shirt_attributes(): 
    # new instance
    polo = Shirt('Blue', 'XL', 'Polo', 24.99)
    assert polo.color == 'Blue'
    assert polo.size == 'XL'
    assert polo.style == 'Polo'
    assert polo.price == 24.99

def test_shirt_change_price(): 
    polo = Shirt('Blue', 'XL', 'Polo', 24.99)
    assert polo.price == 24.99
    polo.change_price(45.78)
    assert polo.price == 45.78

def test_discounted_price():
    polo = Shirt('Blue', 'XL', 'Polo', 24.99)
    assert polo.discount(0.20)== 19.992    
