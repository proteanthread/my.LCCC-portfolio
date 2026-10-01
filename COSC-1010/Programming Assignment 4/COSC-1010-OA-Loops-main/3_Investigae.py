"""
Investigate Activity 1: Finding Even Numbers

This code is meant to print all the even numbers between 0 and 10.

Task:
Run the code and observe the output. Then, answer the following questions.

1. What do the numbers 0, 11, and 2 mean in `range(0, 11, 2)`?
2. What does the `%` (modulo) operator do in the line `if number % 2 == 0:`?
3. What happens if you change `if number % 2 == 0:` to `if number % 2 != 0:`?
4. Why does the code print "Found an even number:" for each even number, but what is actually printed is the number itself?
"""

for number in range(0, 11):
    # Check if the number is even
    if number % 2 == 0:
        print(f"Found an even number: {number}")


"""
Investigate Activity 2: Validating User Input

This program asks the user to enter 'yes' or 'no' and won't stop until it gets a valid answer.

Task:
Run the program. Try entering different things like 'YES', 'y', 'hello', etc.
Then, answer the questions below.

1. What is the purpose of the line `response = ""` before the loop starts?
2. The condition for the `while` loop is `response != "yes" and response != "no"`. Explain in your own words what this means.
3. How does the `.lower()` method help this program work? What would happen if you removed it?
4. Why is the `input()` function called *inside* the loop? What would happen if it were called before the loop started?
"""

response = ""

while response != "yes" and response != "no":
    response = input("Please enter 'yes' or 'no': ")
    response = response.lower() # Convert input to lowercase

print("Thank you for your response!")
