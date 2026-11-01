# Programming Assignment 8 - Lists
# Jeff Wood
# COSC 1010-500 26/FA - Dr. North
# 11-01-2026


def get_numbers():
    # Get 20 numbers from the user
    number_list = []

    for count in range(1, 21):
        number = float(input(f"Enter number {count} of 20: "))
        number_list.append(number)

    return number_list


def analyze_numbers(number_list):
    # Return the lowest, highest, total, and average values
    lowest_number = min(number_list)
    highest_number = max(number_list)
    total = sum(number_list)
    average = total / len(number_list)

    return lowest_number, highest_number, total, average


def main():
    # Start
    print("Number Analysis Program")
    print("Enter 20 numbers. Whole numbers and decimals are accepted.\n")

    numbers = get_numbers()
    lowest, highest, total, average = analyze_numbers(numbers)

    print("\nNumber Analysis Results")
    print(f"Lowest number:  {lowest:.2f}")
    print(f"Highest number: {highest:.2f}")
    print(f"Total:          {total:.2f}")
    print(f"Average:        {average:.2f}")


if __name__ == "__main__":
    main()
