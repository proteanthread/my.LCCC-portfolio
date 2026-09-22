"""
# PRIMM: Investigate 1

## Instructions

Now, let's investigate the code from the "Predict" activity. 
Run the code in a Python environment to see the actual output. 
Then, answer the questions below.

---

### Questions

1.  **First Question:** The first `if` statement checks the condition `age < 13`. Is this condition `True` or `False`? Why?
# False because age is greater than 13 here.
2.  **Second Question:** The `elif` statement checks the condition `age < 18`. Why does the program check this condition *after* the first `if` statement?
# Because if you swapped 18 with 13 and 13 with 18 it would not pass through to here because 18 is true.
3.  **Flow of Control:** Which of the three `print` statements for the ticket price was executed? Why were the other two skipped?
# The other ticket prices were skipped because age < 18 was the only one to return a true value.
4.  **Indentation:** What do you think would happen if you removed the indentation (the spaces) before `print("Ticket price: $12 (Teen)")`?
# Python would error out.

"""

# A simple program to check age for a movie ticket
age = 15

print("Welcome to the theater!")

if age < 18:
    print("Ticket price: $8 (Child)")
elif age < 13:
    print("Ticket price: $12 (Teen)")
else:
    print("Ticket price: $15 (Adult)")

print("Enjoy the show!")


"""
Investigate Activity 2: Grade Boundaries

Task: Run this code with different values for `score`.
Answer the questions in the comments below.
"""

score = 90 # Try changing this value! (e.g., 89, 90, 91)

if score > 90:
  grade = "A"
elif score >= 80:
  grade = "B"
elif score >= 70:
  grade = "C"
else:
  grade = "Needs Improvement"

print(f"A score of {score} gets a grade of {grade}.")

"""
Questions:

1. What is the lowest score you can get and still receive a "B"?
   Why does this happen?
# 80 - because in this case we are evaluating the other direction (higher to lower)

2. What happens if you enter a score of 89.9? What about 90?
   What does the `>=` operator mean?
# Anything between 80 and 89.999 would evaluate to a 'B'

3. If the first `if` statement was `if score > 90:`, how would that
   change the grade for a score of 90?
# it would give the student a grade of 'B' still since score is not more than 90

"""

"""
Investigate Activity 3: Nested Conditions

Task: Run this code and observe its behavior.
Answer the questions in the comments below.
"""

is_logged_in = False
is_admin = True # Try changing this to True!

if is_logged_in:
  print("Welcome to the system.")
  if is_admin:
    print("You have admin privileges.")
  else:
    print("You have standard user privileges.")
else:
  print("Please log in to continue.")


"""
Questions:

1. What two conditions must be true for the message "You have admin privileges."
   to be printed?
# both 'is_logged_in' and 'is_admin'

2. Why is the second `if/else` block indented inside the first `if` block?
   What does this indentation tell Python?
# because this tells python if you are logged in or not and if you are then it tells you if you have admin privileges or not.

3. What is printed if `is_logged_in` is `False`? Does the program even
   check if the user is an admin in that case? Why?
# No because first 'if' is telling Python the user isn't even logged in.
   
"""


