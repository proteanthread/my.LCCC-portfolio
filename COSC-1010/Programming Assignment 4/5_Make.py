"""
Make Activity: The Number Guessing Game

This is your graded assignment for the week.

Task:
Create a number guessing game with the following rules:
1.  The computer should "think" of a secret number between 1 and 100.
    You can hard-code this number for now (e.g., `secret_number = 42`).
2.  The program should loop forever (or until the user guesses the right number).
3.  Inside the loop, it should ask the user to guess the number.
4.  It should then tell the user if their guess was "Too high!", "Too low!", or "You got it!".
5.  If the user guesses the correct number, the program should congratulate them and then stop looping.

Example Interaction:
> Guess a number between 1 and 100: 50
> Too high!
> Guess a number between 1 and 100: 25
> Too low!
> Guess a number between 1 and 100: 42
> You got it!

Stretch Goals (Optional Challenges):
-   Keep track of how many guesses the user took and print it at the end.
-   Instead of a fixed number, make the computer choose a random number at the start.
    Hint: You'll need to `import random` and use `random.randint(1, 100)`.

Here is a starting point for your code.
"""

import random

# Stretch Goal: Make the computer choose a random number at the start
secret_number = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100.")

# Stretch Goal: Keep track of how many guesses the user takes
guess_count = 0

# Start a loop that will run until the user guesses correctly
while True:
    # Get the user's guess and convert it to an integer
    guess_str = input("Guess a number between 1 and 100: ")
    guess = int(guess_str)
    
    # Increase the guess count by 1 every time the loop runs
    guess_count += 1

    # Compare the guess to the secret number
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        # If they got it right, print the success message with their score, then exit.
        print(f"You got it! It took you {guess_count} guesses.")
        break
