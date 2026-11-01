# Filename: 04_Strings_Investigate_1.py
"""
Investigate Activity: String Methods

Run this code. Then, answer the questions below.
"""

messy_string = "   COSC 1010 is Awesome!   "

# Applying some string methods
stripped_string = messy_string.strip()
upper_case_string = messy_string.upper()
lower_case_string = messy_string.lower()
replaced_string = messy_string.replace("Awesome", "Great")

print(f"Original: '{messy_string}'")
print(f"Stripped: '{stripped_string}'")
print(f"Uppercase: '{upper_case_string}'")
print(f"Lowercase: '{lower_case_string}'")
print(f"Replaced: '{replaced_string}'")
print(f"Original after all methods: '{messy_string}'")


"""
Answer the following questions based on the output:

1. What does the `.strip()` method do? Where does it remove whitespace from?

2. Does `.upper()` change the original `messy_string`? Why or why not?
   (Hint: Think about string immutability).

3. What are the arguments for the `.replace()` method? What does it do?

4. Can you chain methods together? Try to predict what the following line would print,
   and then uncomment it and run the code to check your prediction.
"""
# print(f"Chained: '{messy_string.strip().lower()}'")

