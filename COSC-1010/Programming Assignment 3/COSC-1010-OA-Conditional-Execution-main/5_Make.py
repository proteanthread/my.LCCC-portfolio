"""
Make Activity: The Number Classifier (Graded Assignment)

Problem Description:
Write a Python program that asks the user to enter a number. The program
should then determine if the number is positive, negative, or zero,
and print an appropriate message.

Expected Input/Output:
- When the user enters a positive number (e.g., 5), the program should print:
  "The number 5 is positive."
- When the user enters a negative number (e.g., -3), the program should print:
  "The number -3 is negative."
- When the user enters 0, the program should print:
  "The number 0 is zero."

Hints:
1. You will need to use the `input()` function to get the user's number.
2. Remember that `input()` returns a string! You'll need to convert it
   to a number using `int()` or `float()`.
3. An `if-elif-else` structure is perfect for this problem.
"""

# --- WRITE YOUR CODE BELOW ---
number = int(input("Enter a number: "))

# Classify the number
if number > 0:
    print(f"The number {number} is positive.")
elif number < 0:
    print(f"The number {number} is negative.")
else:
    print(f"The number {number} is zero.")
