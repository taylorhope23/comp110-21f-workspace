"""An exercise in remainders and boolean logic."""

__author__ = "730318770"


number: int = int(input("Enter an int: "))
if abs(number) % 2 and 7 == 0:
    print("TAR HEELS")
else:
    if abs(number) % 2 == 0:
        print("TAR")
    else:
        if abs(number) % 7 == 0:
            print("HEELS")
        else: 
            print("CAROLINA")

