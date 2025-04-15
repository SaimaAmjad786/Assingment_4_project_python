# Project 7 Hangman Game in Python
import random

# List of words to choose from
words = ['enum', 'python', 'collab', 'vscode', 'game']
word = random.choice(words)  # Randomly select a word
guessed_letters = []         # To store letters the user has guessed
attempts = 6                 # Total allowed attempts

print("Welcome to Hangman Game - Project 7")
print("_ " * len(word))      # Show initial blanks

while attempts > 0:
    guess = input("\nGuess a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter.")
        continue

    if guess in guessed_letters:
        print("this letter is already guess choose another letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        attempts -= 1
        print(f"Wrong  {attempts} attempts")

    # Display the current state of the word
    displayed_word = " ".join([letter if letter in guessed_letters else "_" for letter in word])
    print(displayed_word)

    # Check if the word has been completely guessed
    if "_" not in displayed_word:
        print(f"\n🎉 Congratulations! You guessed the word: {word}")
        break
else:
    print(f"\n💀 Game Over! The correct word is: {word}")







