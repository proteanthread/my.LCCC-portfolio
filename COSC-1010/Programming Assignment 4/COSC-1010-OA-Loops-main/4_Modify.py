"""
Modify Activity 1: Changing The Range

This program prints a sequence of numbers.

Task:
Your goal is to modify the program to achieve the following outcomes.
For each modification, first predict what will happen, then change the code and run it to check your prediction.

1.  **Modification 1:** Make the program print the numbers from 10 to 15 (inclusive).
    * Prediction:
    * Code Change:

2.  **Modification 2:** Make the program print all the odd numbers from 1 to 20.
    * Prediction:
    * Code Change:

3.  **Modification 3:** Make the program count backwards from 10 down to 1.
    * Prediction:
    * Code Change:
"""

# Original code
print("Original sequence:")
for i in range(1, 5):
    print(i)


"""
Modify Activity 2: Adjusting the Condition

This program simulates a battery level, printing a warning when it gets low.

Task:
Modify the code to meet the new requirements below. For each, predict the new output before running.

1.  **Modification 1:** The battery is more powerful. Change the loop so it starts at 100 and stops when the level is 20 or less.
    * Prediction:
    * Code Change:

2.  **Modification 2:** Add a new warning. If the battery level is exactly 25, print "Warning: Battery level critical!" in addition to the normal output.
    * Hint: You'll need an `elif`.
    * Prediction:
    * Code Change:
"""

battery_level = 50

# The loop continues as long as the battery is above 30
while battery_level > 30:
    print(f"Battery at {battery_level}%")
    if battery_level <= 40:
        print("Low battery warning!")
    battery_level -= 5

print("Battery depleted.")
