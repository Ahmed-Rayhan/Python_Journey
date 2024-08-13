#WORD GUESSING GAME by Characters
import random

# Prompting user for their name
player_name = input("What is your name? ")

print("Good Luck!", player_name)

# List of words to choose from
word_list = ['rainbow', 'computer', 'science', 'programming',
             'python', 'mathematics', 'player', 'condition',
             'reverse', 'water', 'board', 'geeks']

# Randomly selecting a word from the list
selected_word = random.choice(word_list)

print("Guess the characters")

# Variable to store guessed characters
guessed_chars = ''

# Number of allowed attempts
attempts_left = 12

# Loop for the guessing game
while attempts_left > 0:
    failed_attempts = 0

    # Displaying the current state of the guessed word
    for char in selected_word:
        if char in guessed_chars:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed_attempts += 1

    # Checking if the user has guessed the entire word
    if failed_attempts == 0:
        print("\nYou Win!")
        print("The word is:", selected_word)
        break

    # Prompting user to guess a character
    print()
    guess = input("Guess a character: ")

    # Adding the guessed character to the list of guesses
    guessed_chars += guess

    # If the guessed character is not in the word
    if guess not in selected_word:
        attempts_left -= 1
        print("Wrong guess")
        print("You have", attempts_left, "more guesses left")

        # If no attempts are left, the user loses
        if attempts_left == 0:
            print("You Lose")
