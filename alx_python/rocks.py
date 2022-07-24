#!/usr/bin/python3
import random
user_win = 0
comp_win = 0
options = ["rock", "paper", "scissors"]
while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    #rock = 0, paper = 1, scissors = 2
    computer_guess = options[random_number]
    print("Computer picked", computer_guess + ".")

    if user_input == "rock" and computer_guess == "scissors":
        print("You won!")
        user_win += 1
    elif user_input == "paper" and computer_guess == "rock":
        print("You won!")
        user_win += 1
    elif user_input == "scissors" and computer_guess == "paper":
        print("You won!")
        user_win += 1
    elif user_input == computer_guess:
        user_win += 0
        comp_win +=0
    else:
        print("You lost!")
        comp_win += 1
print("You won" , user_win, "times")
print("The computer won", comp_win, "times")
print("Goodbye!")
