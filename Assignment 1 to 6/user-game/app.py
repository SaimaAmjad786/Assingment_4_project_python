# #Project 3 : Guess the Number Game Python Project (User)

import random

print("Guess the number between 1 to 100!")
# Generate random number
number = random.randint(1, 100)

while True:
    guess = int(input("Enter your guess number: "))  # Ask user for input

    if guess < number:
        print("Too Low Number! Try again.")
    elif guess > number:
        print("Too High Number! Try again.")
    else:
        print("Congratulations! You got it right!")
        break  # Exit the loop once the correct guess is made


