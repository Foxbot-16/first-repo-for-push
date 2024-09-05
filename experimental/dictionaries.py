menu = {"pizza": 5.99,
        "popcorn": 3.99,
        "soda": 1.59,
        "lemonade": 4.49,
        "tortilla": 2.99}

# print the keys
for key in menu.keys():
    print(f"this print the key: {key}")

# print the values
for value in menu.values():
    print(f"this print the values: {value}")

# print both
for key, value in menu.items():
    print(f"this is the key: {key} with it's value: {value}")