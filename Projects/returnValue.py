# calculate the amount that a financial instrument can give

tot_inv = 0
return_perc = 0

# get the total investment
while tot_inv <= 0:
    tot_inv = float(input("Enter the total investment: "))
    if tot_inv <= 0:
        print("Your total investment can't be negative or zero") 

# get the return percent
while return_perc <= 0:
    return_perc = float(input("Enter the return percentage: "))
    if return_perc <= 0:
        print("Your return percentage can't be negative or zero")

amount = round((tot_inv * return_perc) / 100, 3) + tot_inv
print(f"Your total return is: {amount}$")