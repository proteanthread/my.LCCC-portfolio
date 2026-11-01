# filename: 05_Lists_Investigate_1.py
"""
Activity: Investigate the Code

1.  Run this code and observe the output at each step.
2.  Answer the questions below in comments.

Questions:
1. What does the `sort()` method do to the `numbers` list? Does it create a new list or change the original?
   # Your Answer Here

2. What does the `reverse()` method do?
   # Your Answer Here

3. What happens if you call `sort()` on a list that is already sorted?
   # Your Answer Here
"""

numbers = [4, 1, 7, 3, 5]
print("Original list:", numbers)

# Sort the list
numbers.sort()
print("After sorting:", numbers)

# Reverse the list
numbers.reverse()
print("After reversing:", numbers)
