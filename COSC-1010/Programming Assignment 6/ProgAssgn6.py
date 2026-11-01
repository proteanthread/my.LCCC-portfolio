# Programming Assignment 6 - Modules and Libraries
# Jeff Wood
# COSC 1010-500 26/FA - Dr. North
# 10-19-2026

import math

# Constants

SQ_FT_PER_GALLON = 112        # Wall area (sq ft)
HOURS_PER_GALLON = 8          # Labor hours
LABOR_RATE_PER_HOUR = 35.00   # Labor charge


def gallons_required(sq_ft):
    # Return the whole number of gallons needed to cover sq_ft of wall space.
    # Paint is sold by the gallon so end value is rounded to the nearest gallon.
    return math.ceil(sq_ft / SQ_FT_PER_GALLON)


def labor_hours(gallons):
    # Return the hours of labor required to apply the given gallons of paint.
    return gallons * HOURS_PER_GALLON


def paint_cost(gallons, price_per_gallon):
    # The cost of the paint.
    return gallons * price_per_gallon


def labor_charges(hours):
    # Return the total labor charges for the given number of hours.
    return hours * LABOR_RATE_PER_HOUR


def main():
    # Get the input from the user.
    sq_ft = float(input("Enter the square feet of wall space to be painted: "))
    price_per_gallon = float(input("Enter the price of the paint per gallon: "))

    # Calculate the estimate.
    gallons = gallons_required(sq_ft)
    hours = labor_hours(gallons)
    cost_of_paint = paint_cost(gallons, price_per_gallon)
    cost_of_labor = labor_charges(hours)
    total_cost = cost_of_paint + cost_of_labor

    # Display the results.
    print()
    print("Paint Job Estimate")
    print("------------------")
    print(f"Gallons of paint required:   {gallons}")
    print(f"Hours of labor required:     {hours}")
    print(f"Cost of the paint:           ${cost_of_paint:,.2f}")
    print(f"Labor charges:               ${cost_of_labor:,.2f}")
    print(f"Total cost of the paint job: ${total_cost:,.2f}")


# Call the main function.
if __name__ == "__main__":
    main()
