# Assignment 1 - Expressions
# Jeff Wood
# COSC 1010-500 26/FA - Dr. North
# 09-07-2026

print ("Assignment 1 by Jeff Wood")
x = int(input ("please enter 1st number? "))
y = int(input ("please enter 2nd number? "))

print ("1. add")
print ("2. subtract")
print ("3. multiply")
print ("4. divide")

choice = int(input("pick one: "))

if choice == 1:
    print ("answer: ", x + y)
elif choice == 2:
    print ("answer: ", x - y)
elif choice == 3:
    print ("answer: ", x * y)
elif choice == 4:
    if y !=0:
        print ("answer: ", x / y)
    else:
        prit ("sorry. cannot divide by zero")
else:
    print ("invalid choice")
