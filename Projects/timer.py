import time

my_time = int(input("Enter the amount of time: "))

# Use a for loop to iterate through the range
for x in range(my_time, 0, -1):
    seconds = int(x % 60)
    minutes = int((x / 60) % 60)
    hours = int(x / 3600)
    print
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)  # Adds a 1-second delay between iterations

print("Time up!!!🏋️")