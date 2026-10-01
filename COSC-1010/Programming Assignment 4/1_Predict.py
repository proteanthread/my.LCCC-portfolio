"""
Predict Activity 1: Counting Up

Task:
Read the code below. Without running it, what do you think the output will be?
Write down your prediction and a short reason for it.

Think about these questions:
- What does the range(5) function do? SETS THE RANGE OF THE LOOP FROM 0-4
- What numbers will the variable 'i' hold? THE VALUES 0-4
- How many times will the print statement run? WHICH PRINT STATEMENT
"""

print("Getting ready to count...") # ONCE HERE

for i in range(5):
    print(i) # FIVE TIMES HERE

print("All done!") # ONCE HERE


"""
Predict Activity 2: Countdown

Task:
Look at this 'while' loop. What will it print to the screen?
Write down what you think the final output will be.

Think about these questions:
- What is the starting value of 'counter'? 3
- What condition is the 'while' loop checking? IF COUNTER IS GREATER THAN 0
- What happens to the value of 'counter' inside the loop? REDUCES BY 1
- When will the loop stop? WHEN COUNTER REACHES 0
"""

counter = 3

while counter > 0:
    print(f"T-minus {counter}...")
    counter = counter - 1

print("Blast off!")
