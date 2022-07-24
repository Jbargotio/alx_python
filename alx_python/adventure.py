#!/usr/bin/python3

name = input("Type your name:")
print("Welcome", name, "to this adventure")

answer =input("You are on a dirt road, you can go left or right. Choose right or left:")
if answer == "left":
    answer = input("You have come to a river. Type walk to walk around the river or swim to swim across:")
    if answer == "walk":
        print("You walked for a long distance and grew tired and lost the game.")
    elif answer == "swim":
        print("You swam across and you were eaten by a crocodile.")
elif answer == "right":
    answer = input("You have come to a wobbly bridge you can either cross it or go back. Type cross to cross it or back to go back:")
    if answer == "cross":
        answer = input("You crossed the bridge and met a stranger.Do you can talk to them or not. Type yes to talk to them or no not to talk to them: ")
        if answer == "yes":
            print("You talked to the stranger and they gave you a gold coin. You won!")
        elif answer == "no":
            print("You ignored a stranger and he was offended. You lost!")
    elif answer == "back":
        print("You went back and lost")

else:
    print("Not a valid option.You lose")
print("Thank you for trying", name)
