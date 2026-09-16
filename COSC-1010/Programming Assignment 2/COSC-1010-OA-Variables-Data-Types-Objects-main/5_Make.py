"""
Make Activity: Simple Inventory Tracker

This is your graded assignment for the week.

---
Problem Description
---
You are building a simple command-line tool to track the inventory of a small shop. The inventory consists of item names and their current stock quantity.

Your program must use a LIST of TUPLES to store the inventory data.
- Why a list? Because the number of items in the inventory can change (we can add or remove items).
- Why tuples? Because an individual item's data (its name and quantity) is a fixed pair.

---
Tasks
---
1.  **Initialize Inventory:**
    Create a list named `inventory`. This list should contain at least three tuples. Each tuple should contain two elements:
    - An item name (string)
    - A stock quantity (integer)
    Example: `[("apples", 15), ("bananas", 30), ("oranges", 12)]`

2.  **Display Initial Inventory:**
    Print a header like "Current Inventory:". Then, loop through your `inventory` list. For each item, print its name and quantity in a user-friendly format using an f-string.
    Example output for one item:
    - Item: apples, Quantity: 15

3.  **Add a New Item:**
    - Prompt the user to enter the name of a new item.
    - Prompt the user to enter the quantity for that new item.
    - Create a new tuple with the user's input.
    - Add this new tuple to the end of your `inventory` list.

4.  **Display Updated Inventory:**
    Print a header like "Updated Inventory:". Then, loop through the `inventory` list again and print all the items, including the new one, in the same user-friendly format.

---
Example Interaction
---
(Your program's output should look similar to this)

Current Inventory:
- Item: apples, Quantity: 15
- Item: bananas, Quantity: 30
- Item: oranges, Quantity: 12

Enter the new item name: grapes
Enter the quantity: 25

Updated Inventory:
- Item: apples, Quantity: 15
- Item: bananas, Quantity: 30
- Item: oranges, Quantity: 12
- Item: grapes, Quantity: 25

---
Stretch Goal (Optional)
---
After displaying the updated inventory, add a feature that allows a user to search for an item and update its quantity. This is tricky because tuples are immutable! You will need to find the item, remove the old tuple from the list, and then add a new tuple with the updated quantity.
"""

# --- Your Code Goes Below ---

# 1. Initialize your inventory list of tuples here.


# 2. Print the header and loop through the inventory to display it.


# 3. Prompt the user for a new item and its quantity.


# 4. Create the new item tuple and add it to the inventory list.


# 5. Print the header and loop through the updated inventory to display it.
