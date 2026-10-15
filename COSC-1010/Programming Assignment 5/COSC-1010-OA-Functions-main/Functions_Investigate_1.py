"""
Filename: Functions_Investigate_1.py

Instructions:
This program calculates the area of a circle. It is broken down into two
functions. Run the code and observe the output.

Answer the following questions in your own words:

1. What is the purpose of the `get_radius_from_user()` function? What value
   does it `return`?

2. What is the purpose of the `calculate_area(radius)` function? What is the
   `radius` variable in this function called (an argument or a parameter)?

3. In the main part of the program, a variable named `user_radius` is created.
   How is its value used in the call to `calculate_area`?

4. Trace the flow of the program. Which function is called first? After that
   function finishes, what happens next?
"""

import math # We need this for the value of pi

def get_radius_from_user():
    """Asks the user for a radius and returns it as a float."""
    print("Let's calculate the area of a circle.")
    radius_input = float(input("Please enter the radius: "))
    return radius_input

def calculate_area(radius):
    """Takes a radius as a parameter and prints the area."""
    # The formula for the area of a circle is pi * r^2
    area = math.pi * (radius ** 2)
    print(f"A circle with a radius of {radius} has an area of {area:.2f}.")


# --- Main program execution starts here ---

# First, we get the radius from the user and store it.
user_radius = get_radius_from_user()

# Then, we pass that stored radius into our calculation function.
calculate_area(user_radius)
