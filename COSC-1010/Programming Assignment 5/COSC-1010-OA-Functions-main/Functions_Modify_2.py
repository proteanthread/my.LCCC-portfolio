"""
Filename: Functions_Modify_2.py

Instructions:
This script calculates and prints the cost for two different customers at a
coffee shop. Notice that the three lines of code for calculating the total
cost are repeated. This is a perfect opportunity to use a function!

Your task:
1.  Define a function called `calculate_total_cost`.
2.  This function should accept two parameters: `price` and `tax_rate`.
3.  Inside the function, perform the calculation to find the total cost
    (price + price * tax_rate) and `return` the result.
4.  In the main part of the script, replace the two repeated blocks of
    calculation code with calls to your new `calculate_total_cost` function.
5.  Make sure the final output of the program remains the same!
"""

# --- Main program execution starts here ---
print("Calculating costs...")

# Customer 1
price_1 = 5.00
tax_rate_1 = 0.07
# --- This block of code is repetitive ---
tax_amount_1 = price_1 * tax_rate_1
total_cost_1 = price_1 + tax_amount_1
print(f"Customer 1 total: ${total_cost_1:.2f}")
# ----------------------------------------

# Customer 2
price_2 = 7.50
tax_rate_2 = 0.07
# --- This block of code is also repetitive ---
tax_amount_2 = price_2 * tax_rate_2
total_cost_2 = price_2 + tax_amount_2
print(f"Customer 2 total: ${total_cost_2:.2f}")
# -----------------------------------------
