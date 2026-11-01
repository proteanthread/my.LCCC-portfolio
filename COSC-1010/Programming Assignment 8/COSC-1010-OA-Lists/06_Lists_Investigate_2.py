# filename: 06_Lists_Investigate_2.py
"""
Activity: Investigate the Code

1. Run the code below. It will cause an error!
2. Read the error message. What does it say?
3. Answer the questions in the comments below.

Questions:
1. Why did the line `print(instruments[4])` cause an `IndexError`?
   # Your Answer Here

2. What is the value of `list_length`? How is that number related to the *last valid index* of the list?
   # Your Answer Here

3. How would you correctly print the last item of the list (`'Drums'`) using its index?
   # Your Answer Here
"""

instruments = ['Guitar', 'Piano', 'Bass', 'Drums']

list_length = len(instruments)
print("The number of instruments is:", list_length)

# This line will cause an error. Try to understand why!
print(instruments[4])
