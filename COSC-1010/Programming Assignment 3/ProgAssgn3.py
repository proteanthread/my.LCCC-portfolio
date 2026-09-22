# Jeffrey Wood
# COSC 1010 - Dr. North
# Programming Assignment 3

Days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

DayOfWeek = int(input("Enter a number (1-7) to display the day of the week: "))

if 1 <= DayOfWeek <=7:
    print ("You selected " + Days[DayOfWeek - 1])
else:
    print ("Please enter a valid number from 1 to 7 only.")

