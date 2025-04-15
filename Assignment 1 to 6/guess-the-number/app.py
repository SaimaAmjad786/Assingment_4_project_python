# Project 2 : Guess the Number Game Computer
import random

def guess_the_number():
    """Project 2: Guess The Number Game By computer."""
    number = random.randint(1, 100)  # Random number between 1 and 100
    guesses_left = 7  # Maximum number of guesses

    # Welcome message
    print("Welcome to the number guessing game!")
    print("I am thinking of a number between 1 and 100.")

    # Loop for guessing
    while guesses_left > 0:
        print(f"\nYou have {guesses_left} guesses left.")
        try:
            guess = int(input("Take a guess of another number: "))  # Get input from the player
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue

        # Guess the secret number
        if guess < number:
            print("Too low number! Try another.")
        elif guess > number:
            print("Too high number! Try another.")
        else:
            print(f"Congratulations! You guessed the correct number in {7 - guesses_left + 1} tries.")
            return  # Exit the game if the correct number is guessed
        
        guesses_left -= 1  # Reduce the number of guesses left

    # Game over message
    print(f"\nYou ran out of guesses. The number was {number}.")

# Start the game
guess_the_number()
