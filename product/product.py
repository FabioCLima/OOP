""" Atributos com um ou dois underlines não devem ser usada fora 
da classe """
class Product:
    def __init__(self, name: str, price: float) -> None:
        # private protected
        self._name = name # attribute com underline não utilize esse atributo
        self._price = price
    
    @property
    def name(self):
        # getter method = get a value from attribute
        print('This is getter method')
        return self._name
    
    @name.setter
    def name(self, value: str):
        print(f'Estou no SETTER, {value}')
        if not isinstance(value, str):
            raise ValueError('Must be a string type')
        self._name = value
    
    @property
    def price(self):
        print('This is getter method')
        return self._price
    
    


if __name__ == "__main__":
    product1 = Product('beer', 5.75)

    print(product1.name)  # getter method call
    print(product1.price) # getter method call
    product1.name = 'coffee' # setter method call
    print(product1.name) # getter method call
    product1.name = 25
