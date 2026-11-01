"""
Activity: Predict the Output

1.  Read the code below.
2.  Without running the code, write down what you think the final output will be in the `prediction` variable.
3.  Think about your reasoning. How does each line change the `grocery_list`?
"""

# What will be the final state of this list?
prediction = "" # Example: ["bread", "milk", "eggs"]

grocery_list = ["apples", "bananas"]

# Add an item to the end
grocery_list.append("carrots")

# Add another item
grocery_list.append("bread")

# Remove the last item
grocery_list.pop()

# Add milk
grocery_list.append("milk")

print("Final grocery list:", grocery_list)
