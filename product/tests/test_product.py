from product.product import Product 


def test_product_attributes():
    playstation = Product("PS5", "Console Gamer", 4500)
    assert playstation.name == "PS5"
    assert playstation.description == "Console Gamer"
    assert playstation.price == 4500
    
def test_product_str():
    iphone = Product('iPhone', 'Smartphone', 13.99)
    assert str(iphone) == 'Product: name=iPhone, description=Smartphone, price=13.99'
    
def test_product_repr():
    # Initialize a Product object
    notebook = Product('notebook computer', 'battery personal computer', 9780)
    assert repr(notebook) == "Product('notebook computer', 'battery personal computer', 9780)"