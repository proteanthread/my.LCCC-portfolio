# filename: 09_Lists_Make_Assignment.py
"""
Assignment: My Shopping Cart

In this assignment, you will create a simple interactive program that lets a user
build a shopping list.

Instructions:
1.  Create an empty list called `shopping_cart`.
2.  Create a loop that will continue to run until the user types 'done'.
3.  Inside the loop, ask the user to "Enter an item to add to the cart (or type 'done'): ".
4.  If the user enters 'done', the loop should stop.
5.  If the user enters anything else, you should add that item to the `shopping_cart` list.
6.  After the loop has finished, you should print out the final shopping cart.

Example Run:
> Enter an item to add to the cart (or type 'done'): milk
> Enter an item to add to the cart (or type 'done'): bread
> Enter an item to add to the cart (or type 'done'): eggs
> Enter an item to add to the cart (or type 'done'): done
>
> Your final shopping cart is:
> ['milk', 'bread', 'eggs']

Stretch Goals (Optional):
1.  Before printing the final list, use the `sort()` method to display the items in
    alphabetical order.
2.  Add another option for the user, 'remove', that allows them to remove an item
    from the cart. You'll need another `input()` to ask them which item to remove.
"""

# 1. Initialize an empty list for the shopping cart
shopping_cart = []

# --- YOUR CODE GOES BELOW ---

# 2. Start your loop here

# 6. Print the final list after the loop
print("\nYour final shopping cart is:")
print(shopping_cart)
