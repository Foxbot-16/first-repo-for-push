import random
# create the variables
guesses = 0
low_number = 1
high_number = 100
answer = random.randint(low_number, high_number)
breaker = True

# print the conditions
print(f"Enter a number between {low_number} and {high_number}")
print("------------------------------------------------------")

# enter the while loop
while breaker:
    # get the guess from the user
    guess = input("Enter your input: ")

    # check if the answer is a digit or not
    if guess.isalpha():
        print("❌ Invalid input!!! ❌ TRY AGAIN") 
    # the input is a digit --> proceed
    # the guess i out of range
    if int(guess) < low_number or int(guess) > high_number:
        print("The guess is out of range")
        print(f"Select a number between {low_number} and {high_number}")
    # input is too low
    elif int(guess) < answer:
        print("TOO LOW")
        # increment the counter
        guesses += 1
    # input is too high
    elif int(guess) > answer:
        print("TOO HIGH")
        guesses += 1
    # input is correct
    else:
        print("Correct")
        guesses += 1
        # break the while loop
        breaker = False
        
# print the total number of guesses
print(f"Total number of guesses: {guesses}")