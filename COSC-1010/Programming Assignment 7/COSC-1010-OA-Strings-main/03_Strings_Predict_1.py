"""
Predict Activity: Strings

Without running the code, predict what the following lines will print.
Write down your prediction and your reasoning.

Example:
my_string = "hello"
print(my_string[1])

Prediction: e
Reasoning: Indexing starts at 0, so the character at index 1 is 'e'.
"""

# Predict the output of each print statement below

# 1. Basic Indexing
school = "Wyoming"
print(f"1. The character at index 3 is: {school[3]}")

# 2. Negative Indexing
print(f"2. The last character is: {school[-1]}")

# 3. Slicing
print(f"3. A slice from index 1 to 4 is: {school[1:4]}")

# 4. Slicing to the end
print(f"4. A slice from index 4 to the end is: {school[4:]}")

# 5. Concatenation
first_name = "Grace"
last_name = "Hopper"
full_name = first_name + " " + last_name
print(f"5. The full name is: {full_name}")

# 6. Length of a string
print(f"6. The length of the school name is: {len(school)}")

