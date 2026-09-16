"""
Modify Activity 1: Prettier Printing with F-Strings

Task: The code below works, but the output is not very readable. Your goal is to modify it.

1.  Delete the three existing `print()` statements.
2.  Replace them with a SINGLE `print()` statement that uses an f-string.
3.  The output should be a single, nicely formatted sentence, like this:
    "User 'AdaLovelace' is 207 years old and works as a Programmer."
"""

# Starter Code
username = "AdaLovelace"
age = 207
occupation = "Programmer"

# TODO: Replace these three lines with one f-string print statement
print("User:")
print(username)
print("is an Programmer")


"""
Modify Activity 2: Managing a To-Do List

Task: You are given a list representing a simple to-do list.

1.  A new task has come up: "Pay bills". Add this task to the END of the `todos` list.
2.  You have already completed the "Call mom" task. Remove this specific task from the list.
3.  Modify the final print statement to use an f-string that prints the corrected list.

The final output should be:
Your final to-do list: ['Buy groceries', 'Clean the house', 'Pay bills']
"""

# Starter Code
todos = ["Buy groceries", "Call mom", "Clean the house"]
print(f"Starting to-do list: {todos}")

# TODO: Add "Pay bills" to the end of the list


# TODO: Remove "Call mom" from the list


# TODO: Modify this print statement to use an f-string
print("Your final to-do list:", todos)
