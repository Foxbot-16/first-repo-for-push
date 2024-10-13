""" 
the user there balance
if the user is not present in the data print an error message
if the user is available print there balance
ask them the operation they want to do i.e. withdraw deposit or view balance
if withdraw or deposit is selected view the updated balance
"""
#create the database
people = {"John": 1200,
          "Peter": 50,
          "Marty": 14000}

# create the function to interact with the user
def main():
    # welcome message
    print("******* Welcome to the bank *******")
    # get the username
    username = input("Insert the username: ").lower()
    # check if the username is in the database
    if database(username) == "Username found":
        print(database(username))
        

        # ask the user the opertaion they want to do
        print("----- Select the operation you want to do -----")
        print("1. Check balance")
        print("2. Witdraw")
        print("3. Deposit")
        option = input(">>> ")
        # address to the according function
        match option:
            case "1":
                # get the balance of the user
                balance = int(0)
                for key, value in people.items():
                    if username == key.lower():
                        balance = value
                print(f"Current balance: {balance}$")
            case "2":
                print(withdraw(balance))
            case "3":
                deposit()
    else:
        print("Username not found")

# create a function checking if the username is in the database
def database(username):
    # iterate thorug the database
    for key in people.keys():
        # check if the username is in the database
        if username == key.lower():
            return "Username found"


def withdraw():
    amount = int(input("Select the amount to withdraw: "))
    # print the remaining balance
    for value in people.values():
        #check if the requested balance is avialable
        if amount > value:
            return "Not enough balance"
        else:
            return f"Remaining balance {value - amount}"

def deposit():
    pass

if __name__ == "__main__":
    main()