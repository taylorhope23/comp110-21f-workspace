""" looping thorugh a string"""

user_string: str = input("Give me a string! ")

i: int = 0 

while i < len(user_string):
    print(user_string[i])
    i = i + 1 