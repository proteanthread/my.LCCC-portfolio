"""
Predict Activity 1: Strings and F-Strings

Task: Without running the code, predict what the following lines will print to the console. Write down your prediction and a brief reason for it.

What do you think `message[0]` will be?
What do you think `message[-1]` will be?
What will the final `print()` statement output?
"""

# Code to analyze
message = "Programming is fun!"
first_char = message[0]
last_char = message[-1]

print(f"The first character is '{first_char}' and the last character is '{last_char}'.")

"""
Predict Activity 2: Lists vs. Tuples

Task: Without running the code, predict the output.
1. What will the final value of `my_list` be when it is printed?
2. What will happen when the line `my_tuple[0] = "Earth"` is executed? If you think it will cause an error, what is the name of the error?

Write down your prediction and reasoning.
"""

# A list of planets (mutable)
my_list = ["Mars", "Jupiter", "Saturn"]
print(f"Original list: {my_list}")

# Let's update the first planet
my_list[0] = "Venus"
print(f"Updated list: {my_list}")


# A tuple of planets (immutable)
my_tuple = ("Mars", "Jupiter", "Saturn")
print(f"Original tuple: {my_tuple}")

# Now, let's try to update the first planet in the tuple
# my_tuple[0] = "Earth"  # What happens here?
