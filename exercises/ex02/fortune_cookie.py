"""Program that outputs one of at least four random, good fortunes."""

__author__ = 730318770

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


print("Your fortune cookies says...")
n = randint(1, 4)
if n == 1:
    print("Today you will find a million dollars!")
else:
    if n == 2: 
        print("You are going to pass COMP110!")
    else:
        if n == 3:
            print("You have a secret admirer!")
        else:
            print("The best is yet to come!")
print("Now, go spread positive vibes!")