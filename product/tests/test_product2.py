import pytest
from product.product import Product

@pytest.fixture
def product():
    return Product('PS5', 'Console Gamer', 4500)

class TestProduct:
    def test_name(self, product):
        assert product.name == 'PS5'

    def test_description(self, product):
        assert product.description == 'Console Gamer'

    def test_price(self, product):
        assert product.price == 4500

    def test_str(self, product):
        assert str(product) == "Product: name=PS5, description=Console Gamer, price=4500"

    def test_repr(self, product):
        assert repr(product) == "Product('PS5', 'Console Gamer', 4500)"
