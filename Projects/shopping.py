# create the variables
shopping = []
price = []
total = 0

# decorative text
print("\tEnter the requested data or press \"q\" to quit\n")
# iterate in the while loop
while True:
    shop = input("Enter the item: ")
    if shop.lower() == "q":
        break
    cost = float(input("Enter the price: "))
    shopping.append(shop)
    price.append(cost)
    total = float(total) + cost


print("----- YOUR CART -----")

# print the cart
x = 0
for cart in shopping:
    x += 1
    print(f"{x} - {cart}")
    

# print the total
print(f"\nYour total is : {total:.2f}$")