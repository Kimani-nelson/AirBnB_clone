import os
import sys
import datetime
import math

# Constants should be named in uppercase with underscores.

PI = 3.14159
MAX_ATTEMPTS = 3

# Function and class definitions should be separated by two blank lines.


def greet(name):
    """
    This function greets the person passed in as a parameter.
    """
    message = f"Hello, {name}!"
    print(message)


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return PI * self.radius ** 2

    def circumference(self):
        return 2 * PI * self.radius


def main():
    """
    The main function of the program.
    """
    name = input("Enter your name: ")
    greet(name)

    radius = float(input("Enter the radius of the circle: "))
    circle = Circle(radius)

    print(f"Area of the circle: {circle.area()}")
    print(f"Circumference of the circle: {circle.circumference()}")


if __name__ == "__main__":
    main()
