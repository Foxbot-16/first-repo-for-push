# working on args
""" 
def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total


print(add(1, 2, 3, 5)) 
"""

#working on kwargs
def print_address(**kwargs):
    for key, values in kwargs.items():
        print(f"the key \"{key}\" has a value \"{values}\"")

print_address(street="Ciccio bello", city="blq", country="USA")