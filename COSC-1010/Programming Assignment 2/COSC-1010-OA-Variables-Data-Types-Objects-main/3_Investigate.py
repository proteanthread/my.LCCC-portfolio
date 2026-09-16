"""
Investigate Activity 1: String Properties

Task: Run this code and observe the output. Then, answer the questions below.

1.  The string `special_string` looks like it has many characters. What does `len(special_string)` report as its length? Why is it less than the number of characters you see typed out?
2.  What is the purpose of `\n` in a string?
3.  What is the purpose of `\t` in a string?
4.  How do you include a double-quote character (") inside a string that is also enclosed in double-quotes?
"""

# Code to run and investigate
special_string = "First line.\n\tSecond line, indented.\nShe said: \"Hello!\""

print(special_string)
print(f"The length of the string is: {len(special_string)}")


"""
Investigate Activity 2: Mutability with id()

Task: The `id()` function in Python returns the unique memory address of an object. Run this code and observe the output carefully.

1.  Look at the `id` for `shopping_list` before and after appending an item. Did the id change? What does this tell you about whether lists are mutable or immutable?
2.  Now look at the `id` for `rgb_color` before and after we create a "new" tuple. Did the id change? What does this tell you about whether tuples are mutable or immutable?
3.  In your own words, what is the key difference you observed between the list and the tuple in this experiment?
"""

# --- List Investigation ---
shopping_list = ["apples", "bananas", "carrots"]
print(f"Original list: {shopping_list}")
print(f"ID of original list: {id(shopping_list)}")

# Add an item to the list
shopping_list.append("dates")
print(f"Modified list: {shopping_list}")
print(f"ID of modified list: {id(shopping_list)}") # Did this change?

print("-" * 20)

# --- Tuple Investigation ---
rgb_color = (255, 128, 0) # An orange color
print(f"Original tuple: {rgb_color}")
print(f"ID of original tuple: {id(rgb_color)}")

# We can't append, so to "change" it, we must create a new one
rgb_color = rgb_color + (255,) # This creates a new tuple
print(f"New tuple: {rgb_color}")
print(f"ID of new tuple:     {id(rgb_color)}") # Did this change?
