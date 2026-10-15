"""
Filename: Functions_Make_Assignment.py

The Universal Converter

Problem Description:
You're tasked with building a flexible unit converter. Your program should be
able to convert between different units of measurement, such as temperature
(Celsius to Fahrenheit) and distance (Miles to Kilometers).

The power of your program will come from functions. You will create small,
specialized functions for each conversion, and then a main part of your
program will decide which function to call based on user input.

Detailed Instructions:

Part 1: Create the Conversion Functions
-   Define a function `celsius_to_fahrenheit(celsius)` that takes a temperature
    in Celsius and returns the equivalent in Fahrenheit.
    -   Formula: F = (C * 9/5) + 32
-   Define a function `fahrenheit_to_celsius(fahrenheit)` that takes a temperature
    in Fahrenheit and returns the equivalent in Celsius.
    -   Formula: C = (F - 32) * 5/9
-   Define a function `miles_to_kilometers(miles)` that takes a distance in
    miles and returns the equivalent in kilometers.
    -   Formula: 1 mile = 1.60934 kilometers
-   Define a function `kilometers_to_miles(kilometers)` that takes a distance
    in kilometers and returns the equivalent in miles.
    -   Formula: 1 kilometer = 0.621371 miles

Part 2: Implement the Main Program Logic
-   In the main part of your script (after your function definitions), you should:
    1.  Welcome the user to your Universal Converter.
    2.  Ask the user for the numeric value they want to convert (e.g., 100).
    3.  Ask for the starting unit (e.g., "celsius", "miles").
    4.  Ask for the target unit (e.g., "fahrenheit", "kilometers").
-   Use an `if/elif/else` structure to check the user's start and target units.
-   Based on the units provided, call the appropriate conversion function you
    created in Part 1.
-   Store the returned value from the function in a `result` variable.
-   Print a formatted, easy-to-read output string that shows the original value,
    its unit, the converted value, and its unit.
    -   Example output: "100.0 celsius is equal to 212.0 fahrenheit."
-   If the user enters an unsupported conversion (e.g., trying to convert
    celsius to miles), print an error message.

Example Interaction:
Welcome to the Universal Converter!
Enter the value to convert: 32
Enter the starting unit (e.g., fahrenheit, miles): fahrenheit
Enter the target unit (e.g., celsius, kilometers): celsius
32.0 fahrenheit is equal to 0.0 celsius.

Hints:
-   Make sure to convert the user's input for the value to a float.
-   Use `.lower()` on the user's unit inputs to make your `if` statements
    case-insensitive (e.g., so "Celsius" and "celsius" both work).
-   Test each of your conversion functions individually before writing the
    main logic to make sure they work correctly.

Stretch Goals (Optional):
-   Add more conversions (e.g., feet to meters, pounds to kilograms).
-   Put your main logic inside a function called `main()` and call `main()`
    at the very end of your script. This is a common practice in Python.
-   Use a loop to allow the user to perform multiple conversions without
    restarting the script.
"""

# Part 1: Define your conversion functions here.


# Part 2: Implement your main program logic here.

print("Welcome to the Universal Converter!")

# Get input from the user

# Use if/elif/else to call the correct function and print the result
