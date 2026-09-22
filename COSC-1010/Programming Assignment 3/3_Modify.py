"""
# PRIMM: Modify 1

## Instructions

Here is the same code snippet again. Your task is to make the following modifications. For each change, first **predict** the new output, then run the code to **verify** your prediction.

---

### Modifications

1.  **Change the `age`:**
    * **Modification:** Change the line `age = 15` to `age = 65`.
    * **Predict:** What will the new output be?
    * **Verify:** Run the code. Was your prediction correct?

2.  **Add a Senior Discount:**
    * **Modification:** Add a new `elif` block to give a discount to seniors (age 65 and over). The price should be $10. Place this new block *before* the final `else`.
    * **Predict:** With `age` still set to 65, what will the output be now?
    * **Verify:** Run the code. Was your prediction correct?

3.  **Combine Conditions:**
    * **Modification:** Let's say there's a special student discount. Modify the `elif age < 18:` line to also check if the person has a student ID. The code might look something like this (you'll need to add a new variable for the student ID): `elif age < 18 and has_student_id == True:`.
    * **Predict:** What do you need to add to the program for this to work? How will the output change if `age` is 16 and `has_student_id` is `False`?
    * **Verify:** Make the changes and run the code to check your prediction.
"""

# A simple program to check age for a movie ticket
age = 65

print("Welcome to the theater!")

if age < 13:
    print("Ticket price: $8 (Child)")
elif age < 18:
    print("Ticket price: $12 (Teen)")
elif age >= 65:
    print("Senior disctount: $10 (Senior)")
else:
    print("Ticket price: $15 (Adult)")


print("Enjoy the show!")



"""
Modify Activity 2: Checking for Even Numbers

Task: The code below checks if a number is positive. Modify it
so that it checks if a number is EVEN.

Hint: An even number is a number that has no remainder when
divided by 2. The modulo operator (%) gives you the remainder.
For example, `10 % 2` is 0, but `9 % 2` is 1.
"""

number = -10 # Feel free to change this to test

# --- MODIFY THE CODE BELOW ---

if number > 0:
  print("The number is positive.")
elif number <=-1:
  print("The number is negative.")
else:
  print("The number is not positive.")


"""
Modify Activity 3: Adding a Shipping Tier

Task: The code below calculates shipping costs based on weight.
Your task is to add a new shipping tier.

Add an `elif` block that checks for weights up to 20 pounds
and sets the shipping_cost to $15.00.
"""

weight = 30 # Feel free to change this to test

shipping_cost = 0

if weight <= 2:
  shipping_cost = 5.00
elif weight <= 10:
  shipping_cost = 10.00
# --- ADD YOUR ELIF BLOCK HERE ---
elif weight <= 20:
    shipping_cost = 15.00
else:
  shipping_cost = 25.00 # For heavy items

print(f"The shipping cost for an item weighing {weight} pounds is ${shipping_cost:.2f}.")

