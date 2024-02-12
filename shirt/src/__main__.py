from src.shirt_v1 import Shirt

"""  
In this refactored code:
     
    - I changed the `Shirt` class to have `__init__`, `change_price`, and `discount` methods.
    - I added the `__dict__` attribute to Example 1 to display the shirt object's attributes.
    - I put the code examples inside the `__main__` conditional.
    - I used the `extend` method to add multiple t-shirts to `tshirt_collection`.
    - I simplified the `for` loop in Example 4 by iterating through the `tshirt_collection` list directly.
    Example 1: Creating a new shirt object with attributes and printing it
    out as string. 
"""
print(f"How many shirts was created so far: {Shirt.get_num_instances()}")

new_shirt = Shirt("Blue", "XL", "Polo", 24.99)
print(new_shirt.__dict__)

# Example 2: Changing the price of an existing Shirt object and then 
# printing out the updated price.
new_shirt2 = Shirt("Green", "L", "Polo", 24.99)
new_shirt2.change_price(19.99)
print(new_shirt2.price)

# Example 3: Applying a discount to an existing Shirt object and then 
# printing out the discounted price.
new_shirt3 = Shirt("Yellow", "M", "Button Up", 34.99)
discounted_price = new_shirt3.discount(0.2)
print(discounted_price)

# # Create a collection of tshirt 
# # Manager more than on object or instance from the same class
    
# tshirt_collection= []
# tshirt_collection.extend((new_shirt, new_shirt2, new_shirt3))
# for item in tshirt_collection:
#     print(item.color)