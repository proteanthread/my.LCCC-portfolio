"""
Filename: Functions_Investigate_2.py

Instructions:
This program demonstrates the concept of variable scope. There are two
variables named `color`: one outside the function (global scope) and one
inside the function (local scope).

Run the code and carefully observe the output.

Answer the following questions:

1. What is the value of the `color` variable *before* the function is called?

2. What is the value of the `color` variable that is printed *from inside*
   the `change_color()` function?

3. What is the value of the `color` variable *after* the function has
   finished running?

4. Why did the value of the global `color` variable not change, even though
   the function seemed to change it to "Blue"?
"""

# This is a global variable.
color = "Green"

def change_color():
    """
    This function defines its own LOCAL variable named 'color'.
    This local variable only exists while the function is running.
    It is completely separate from the global 'color' variable.
    """
    color = "Blue" # This creates a new, local variable.
    print(f"Inside the function, the color is: {color}")

# --- Main program execution starts here ---

print(f"Before the function call, the color is: {color}")

# We call the function.
change_color()

print(f"After the function call, the color is: {color}")
