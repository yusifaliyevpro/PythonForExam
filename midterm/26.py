# 26. Rock, Paper, Scissors Game
from random import choice

user = ""
while user != "q":
    user = input("Enter (r-Rock, p-Paper, s-Scissors, q-Quit): ")
    comp = choice(["r", "p", "s"])
    if user == comp:
        print("Draw")
    elif (user, comp) in [("s", "p"), ("p", "r"), ("r", "s")]:
        print("You won!")
    else:
        print("I won!")
