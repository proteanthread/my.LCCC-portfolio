# Programming Assignment 4 - Rainfall
# Jeff Wood
# COSC 1010-500 26/FA - Dr. North
# 09-30-2026

MONTHS_PER_YEAR = 12

num_years = int(input("Enter the number of years: "))
total_rainfall = 0.0

for year in range(1, num_years + 1):
    print(f"\n--- Data Collection for Year {year} ---")
    for month in range(1, MONTHS_PER_YEAR + 1):
        monthly_rain = float(input(f"Enter inches of rainfall for Year {year}, Month {month}: "))
        total_rainfall += monthly_rain

total_months = num_years * MONTHS_PER_YEAR
average_rainfall = total_rainfall / total_months

print("\n\n\n")
print("     RAINFALL REPORT")
print("\n")
print(f"Total period in months: {total_months}")
print(f"Total rainfall recorded: {total_rainfall:.2f} inches")
print(f"Average monthly rainfall: {average_rainfall:.2f} inches")
print("\n\n")
