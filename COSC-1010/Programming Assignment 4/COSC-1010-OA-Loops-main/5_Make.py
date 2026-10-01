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

# 1. Set the secret number
secret_number = 42
print("I'm thinking of a number between 1 and 100.")

# 2. Start a loop that will run until the user guesses correctly.
#    A `while True:` loop is a good choice here.
while True:
    # 3. Get the user's guess. Remember to convert it to an integer!
    guess_str = input("Guess a number between 1 and 100: ")
    guess = int(guess_str)

    # 4. Use if/elif/else to compare the guess to the secret number
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        # 5. If they got it right, print a success message and exit the loop.
        #    The `break` keyword is perfect for this.
        print("You got it!")
        break
