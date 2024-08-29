# create the dictionary for the stand
menu = {"pizza": 5.99,
        "popcorn": 3.99,
        "soda": 1.59,
        "lemonade": 4.49,
        "tortilla": 2.99}
# create vaeìriables for total and cart
cart = []
total = 0

# iterate through the dictionary
print("------------------ MENU ------------------")
for key, value in menu.items():
    print(f"{key:10}: ${value}")
print("------------------------------------------")

# get the user input
while True:
    user = input("Enter the items to buy (q to quit): ").lower()
    # match the user input
    if user in menu:
        print(f"found {user} at a price of ${menu[user]}")
        total += menu[user]
        cart.append(user)
    # q to break the while loop
    elif user == "q":
        break
    # item not found
    else:
        print("Not found")

# print the total
print("------------------ TOTAL ------------------")
print(f"Your total is: ${total:.2f}")

# print the cart
print("------------------ CART ------------------")
for shop in cart:
    print(shop)