""" challenge question 1"""

choice: int = int(input("Enter a number: "))

# print A if choice is < 25
# print B if choice is >= 24 and < 50 
# print c is choice is > 75
# print D if choice is >= 50 and <= 75
if choice < 25:
    print("A")
else:
    if choice < 50:
        print("B")
    else: 
        if choice <= 75:
            print("D")
        else:
            print("C")