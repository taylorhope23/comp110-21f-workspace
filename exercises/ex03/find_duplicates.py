"""Finding duplicate letters in a word."""

__author__ = "730318770"

word: str = input("Enter a word: ")
dup: bool = False

i: int = 0 
while i< len(word):
    j: int = i + 1
    char = word[j] == word[i]
    while j < len(word):
       if  


i = i + 1 
