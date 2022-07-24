#!/usr/bin/python3
import random

maxi = input("Type a number: ")
chances = 0
if maxi.isdigit():
    maxi = int(maxi)

    if maxi <=0:
        print("Please type a number greater than 0")
        quit()
else:
    print("Please type a number next time")

r = random.randrange(maxi)
while True:
    chances += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time")
        continue
    if user_guess == r:
        print("You got it correct!")
        break
    elif user_guess > r:
        print("That is above the number")
    else:
        print("That is below than the number")
print("You got it in", chances,"guesses")
