"""an example of conditional if else statements"""

SECRET: int = 3 

print("I am thinking of a number between 1-5, what is it?")
guess: int = int(input("What is your guess? "))

if guess == SECRET:  
    print("You guessed correctly!!!")
    print("Have a wonderful day")
else: 
    print("Sorry, wrong answer :(")
    print("Try running the program again.")
print("Game over.")