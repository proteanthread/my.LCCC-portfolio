# Programming Assignment 4 - Bug Collector
# Jeff Wood
# COSC 1010-500 26/FA - Dr. North
# 09-29-2026

TOTAL_DAYS = 5
total_bugs = 0

for day in range(1, TOTAL_DAYS + 1):
    bugs_collected = int(input(f"Enter the number of bugs collected on day {day}: "))
    total_bugs += bugs_collected

print(f"\nThe total number of bugs collected over {TOTAL_DAYS} days is: {total_bugs}")
print("\n\n")
