# filename: 07_Lists_Modify_1.py
"""
Activity: Modify the Code

The program below removes the last item from the `tasks` list using `pop()`.

Your goal:
1.  Modify the code to remove the item "Mow the lawn" specifically.
    Hint: You'll need to use a different list method.
2.  Predict what the output will be after your change.
3.  Run the code to verify your prediction.
"""

tasks = ["Walk the dog", "Do homework", "Mow the lawn", "Wash dishes"]
print("Original tasks:", tasks)

# --- MODIFY THE LINE BELOW ---
tasks.pop()
# --- END MODIFICATION ---

print("Final tasks:", tasks)
