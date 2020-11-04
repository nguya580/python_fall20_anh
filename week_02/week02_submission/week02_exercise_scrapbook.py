# %% codecell
# Exercise 2
# Print the first 10 natural numbers using a loop

# Expected output:
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

x = 0

while x <= 10:
    print(x)
    x += 1

# %% codecell
# Exercise 3:
# Execute the loop in exercise 1 and print the message Done! after

# Expected output:
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# Done!

x = 0

while x <= 10:
    print(x)
    x += 1

    if x > 10:
        print("Done!")

# %% codecell
# Exercise 4:

# Print the numbers greater than 150 from the list

# list = [12, 15, 47, 63, 78, 101, 157, 178, 189]
# Expected output:
# 157
# 178
# 189

list = [12, 15, 47, 63, 78, 101, 157, 178, 189]

for number in list:
    if number > 150:
        print(number)

# %% codecell
# Exercise 5:
# Print the number that is even and less than 150

# list = [12, 15, 47, 63, 78, 101, 157, 178, 189]
# Expected output:

# 12
# 78

# Hint: if you find a number greater than 150, stop the loop with a break

list = [12, 15, 47, 63, 78, 101, 157, 178, 189]

for number in list:
    if number < 150 and number % 2 == 0:
        print(number)

# %% codecell
# Exercise 6:

# This will be a challenging!

# Write a while loop that flips a coin 10 times

# Hint: Look into the random library using:
# https://docs.python.org/3/library/random.html
# https://www.pythonforbeginners.com/random/how-to-use-the-random-module-in-python

import random

head_count = []
tail_count = []

def flip_coin():
    """this function generates random value 0-1 for coin
    1 is head
    0 is tail"""

    coin = random.randrange(2)

    if coin == 1:
        print(f"You got a head. Value is {coin}")
        head_count.append("head")
    else:
        print(f"You got a tail. Value is {coin}")
        tail_count.append("tail")

def flip():
    """this function generate flipping coin 10 times"""

    for x in range(10):
        flip_coin()

    print(f"\nYou flipped HEAD {len(head_count)} times, and TAIL {len(tail_count)} times.\n")
    again()


def again():
    """ask user if they want to flip coint again."""

    ask = input("Do you want to flip coint again? \nEnter 'y' to flip, or 'n' to exit.\n")

    if ask == "y":
        #clear lists output to remains list length within 10
        del head_count[:]
        del tail_count[:]

        #run flipping coin again
        flip()

    elif ask == "n":
        print("\nBye bye.")

#call function
flip()
