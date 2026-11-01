# Filename: 06_Strings_Make_Assignment.py
"""
Make Activity: Username and Email Generator

Your task is to create a program that generates a username and an email address for a new user based on their first name, last name, and birth year.

### Problem Description

The program should:
1.  Ask the user for their first name.
2.  Ask the user for their last name.
3.  Ask the user for their four-digit birth year.
4.  Generate a username following this format:
    - The first two letters of the first name.
    - The first three letters of the last name.
    - The last two digits of their birth year.
    - The entire username should be in lowercase.
    - Example: For "Grace Hopper" born in "1906", the username would be "grahop06".
5.  Generate a university email address using the created username.
    - The format should be `username@university.edu`.
    - Example: `grahop06@university.edu`.
6.  Print a welcome message and the generated username and email.

### Expected Input/Output

Here is an example of how the program should run:

Enter your first name: Grace
Enter your last name: Hopper
Enter your birth year: 1906

--- Welcome, Grace Hopper! ---
Your username is: grahop06
Your university email is: grahop06@university.edu

### Hints

- You will need to use string slicing to get parts of the names and the year. Remember that you can slice from the beginning `[:2]` or get the end `[-2:]`.
- Use the `.lower()` method to ensure the final username is in the correct case.
- f-strings are a great way to format the final output!

Good luck!
"""

# --- Your code starts here ---

# 1. Get user input
first_name = input("Enter your first name: ")


# 2. Generate the username


# 3. Generate the email


# 4. Print the output

