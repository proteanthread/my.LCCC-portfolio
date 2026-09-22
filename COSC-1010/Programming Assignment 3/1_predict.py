"""
# PRIMM: Predict 1

## Instructions

Read the following Python code snippet carefully. 
**Without running the code**, write down what you think the exact output will be. 
Explain your reasoning in a sentence or two.

---

### Your Prediction

**Predicted Output:**

```
# Ticket price: $12 (Teen)
```

**Reasoning:**

#Because 15 is less than 18 but more than 23 so the if/elif evaluated 'age' correctly.

"""

# A simple program to check age for a movie ticket
age = 15

print("Welcome to the theater!")

if age < 13:
    print("Ticket price: $8 (Child)")
elif age < 18:
    print("Ticket price: $12 (Teen)")
else:
    print("Ticket price: $15 (Adult)")

print("Enjoy the show!")


"""
Predict Activity 2: Number Check

Task: Without running the code, predict what the output will be.
Write down your prediction and your reasoning in a comment.

What do you think will be printed to the screen when this program runs?
"""

# Your Prediction: It's not too hot today.
#
# Your Reasoning: the 'if/elif' evaluated temperature to be less than 30
# but if temperature is more than 30 you would get "It's a hot day!"
#

temperature = 25

if temperature > 30:
  print("It's a hot day!")
else:
  print("It's not too hot today.")
