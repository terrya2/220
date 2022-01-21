"""
Autumn Terry
HW1.py
This program allows individuals to write code with various tools and create needed environments.
I certify that this assignment is entirely my own work.
"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)

def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume =", volume)

def shooting_percentage():
    total_shots = eval(input("Enter total shots: "))
    shots_made = eval(input("Enter shots made: "))
    shooting_percentage = total_shots * shots_made
    print("Shooting percentage =", shooting_percentage, "%")

def coffee():
    coffee = eval(input('Enter how many coffee pounds: '))
    print("How many pounds of coffee would you like", coffee)

    total = (10.5 * coffee) + (0.86 * coffee) + (1.5)
    print("You're total is: ", total)

def kilometers_to_miles():
    kilometers = eval(input("Enter kilometers: "))
    print("How many kilometer did you travel?", kilometers)

    miles = kilometers * 0.621371
    print("That's", miles, "miles!")

if __name__ == '__main__':

