
# NUMBER GUESSING GAME

import random
import math

# Getting user input for the range
lower_bound = int(input("Enter Lower bound: "))
upper_bound = int(input("Enter Upper bound: "))

# Generating a random number within the specified range
target_number = random.randint(lower_bound, upper_bound)
max_attempts = math.ceil(math.log(upper_bound - lower_bound + 1, 2))
print("\n\tYou have", max_attempts, "chances to guess the number!\n")

# Initializing the number of attempts
attempts = 0
guessed_correctly = False

# Loop for the guessing game
while attempts < max_attempts:
    attempts += 1
    guess = int(input("Guess a number: "))

    # Checking the guess
    if guess == target_number:
        print("Congratulations! You guessed it in", attempts, "attempt(s).")
        guessed_correctly = True
        break
    elif guess < target_number:
        print("Your guess is too low!")
    else:
        print("Your guess is too high!")

# If the number wasn't guessed within the allowed attempts
if not guessed_correctly:
    print("\nThe number was:", target_number)
    print("\tBetter luck next time!")
