# create a weight converter program in python
# from kg to pound or punds to kg

print("1 - POUNDS to kg")
print("2 - kg to POUNDS")

option = int(input("Select the converting option: "))
weigth = float(input("Insert your weigth: "))

if option == 1:
    result = weigth * 0.453592
elif option == 2:
    result = weigth * 2.20462
print(f"Final weigth: {round(float(result), 3)}")