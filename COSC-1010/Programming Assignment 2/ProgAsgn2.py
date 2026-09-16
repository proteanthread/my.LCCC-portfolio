# Programming Assignment 2 - Objects & Data Types
# Jeff Wood
# COSC 1010-500 26/FA - Dr. North
# 09-15-2026

class Car:
    """Represents a car traveling at a constant speed."""

    def __init__(self, speed):
        """Constructor that initializes the car with a given speed (mph)."""
        self.speed = speed

    def calculate_distance(self, time):
        """Calculates and returns distance using the formula: Distance = Speed * Time."""
        return self.speed * time


def main():
    # Car {object} with a constant speed of 70 mph
    my_car = Car(70)

    # Define the {list} of time intervals in hours
    intervals = [6, 10, 15]

    # Calculate and display traveled for each interval (uses f-strings)
    for hours in intervals:
        distance = my_car.calculate_distance(hours)
        print(f"In {hours} hours, the car will travel {distance} miles.")


# Execute main()
if __name__ == "__main__":
    main()
