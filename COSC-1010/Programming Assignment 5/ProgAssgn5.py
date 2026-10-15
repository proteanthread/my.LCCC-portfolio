# Programming Assignment 4 - Automobile costs
# Jeff Wood
# COSC 1010-500 26/FA - Dr. North
# 10-15-2026

import math

MONTHS_PER_YEAR = 12

# Prompts the user to input a cost of 0 or more.
def get_cost(prompt):
    while True:
        try:
            amount = float(input(prompt))
        except ValueError:
            print("  That is not a number. Use digits only, such as 125.50")
            continue
        # float() also accepts 'nan' and 'inf', so reject those here as well.
        if not math.isfinite(amount) or amount < 0:
            print("  A cost must be 0 or more, such as 125.50")
            continue
        return amount

# Calculates the total of 6 monthly expenses
def calculate_monthly_total(loan, insurance, gas, oil, tires, maintenance):
    return loan + insurance + gas + oil + tires + maintenance

# Calculates the annual costs 
def calculate_annual_total(monthly_total):
    return monthly_total * MONTHS_PER_YEAR

# Prints both totals with dollar amounts.
def display_results(monthly_total, annual_total):
    print()
    print(f"Total monthly cost: ${monthly_total:,.2f}")
    print(f"Total annual cost:  ${annual_total:,.2f}")

# Reads the 6 monthly costs, then shows the monthly and annual totals.
def main():
    print("Automobile Costs")
    print("Enter the monthly cost of each expense.")
    print()

    loan = get_cost("Monthly loan payment: $ ")
    insurance = get_cost("Monthly insurance:    $ ")
    gas = get_cost("Monthly gas:          $ ")
    oil = get_cost("Monthly oil:          $ ")
    tires = get_cost("Monthly tires:        $ ")
    maintenance = get_cost("Monthly maintenance:  $ ")

    monthly_total = calculate_monthly_total(
        loan, insurance, gas, oil, tires, maintenance
    )
    annual_total = calculate_annual_total(monthly_total)
    display_results(monthly_total, annual_total)


if __name__ == "__main__":
    main()
