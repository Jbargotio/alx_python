#!/usr/bin/python3
print("Welcome to this quiz game!")

play = input("Do you want to play? ")
if play.lower() != "yes":
    quit()
print("Let's play!")
choice = int(input("Which category of questions do you want?\n 1.General knowledge.\n 2. Computer questions.\n3.Sports.\n4. Entertainment.\n "))
score = 0
def computer_questions():
    global score
    answer = input("What does CPU stand for?" )
    if answer.lower() == "central processing unit":
        print("Correct!")
        score +=1
    else:
        print("Incorrect!")
    answer = input("What does GPU stand for? ")
    if answer.lower() == "graphics processing unit":
        print("Correct!")
        score +=1
    else:
        print("Incorrect!")
    answer = input("What does RAM stand for? ")
    if answer.lower() == "random access memory":
        print("Correct!")
        score +=1
    else:
        print("Incorrect!")
    
if choice == 2:
    computer_questions()

    print("You got " + str(score) + " questions correct!")
    print("You got " + str((score/ 3) * 100) + "%.")
