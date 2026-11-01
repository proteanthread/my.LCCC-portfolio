# Filename: 05_Strings_Modify_1.py
"""
Modify Activity: String Formatting

The code below is intended to take a user's first and last name and create a username.
It's not quite right. Follow the modification tasks to fix and enhance it.
"""

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# The current username is just the first and last name concatenated.
username = first_name + last_name
email = username + "@uwyo.edu"

print(f"Welcome, {first_name}!")
print(f"Your username is: {username}")
print(f"Your email is: {email}")


"""
Modification Tasks:

For each task, predict what the change will do, then make the change and run the code to verify.

1.  **Lowercase Username:** The username should be all lowercase. Modify the line where `username` is
    created to make the entire string lowercase.

2.  **Formatted Email:** The email should also be all lowercase. Modify the line where `email` is created.
    Can you do this without changing the `username` variable again?

3.  **Username with Initial:** A better username format would be the first letter of the first name,
    followed by the full last name. For example, "Grace Hopper" would become "ghopper".
    Modify the `username` creation line to achieve this format (and make sure it's still all lowercase!).

4.  **Greeting with Last Name:** Change the welcome message to greet the user by their title and last
    name, like "Welcome, Dr. Hopper!". Assume the title is "Dr.". You will need to use string
    concatenation or an f-string to format this.
"""

