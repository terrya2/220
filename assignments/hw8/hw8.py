"""
Autumn Terry
hw8.py
Create programs with accumulations and conditional control structures.
I certify that this assignment is entirely my own work.

"""
import math
from graphics import *

def add_ten(nums):
    for i in range(len(nums)):
        nums[i] += 10

def square_each(nums):
    for i in range (len(nums)):
        nums[i] = nums[i]*nums[i]


def sum_list(nums):
    sum = 0
    for i in nums:
        sum += i
    return sum

def to_numbers(nums):
    for i in range(len(nums)):
        nums[i] = float (nums[i])

def sum_of_square(nums):
    numbers = []
    for i in nums:
        list = i.split(", ")
        to_numbers(list)
        square_each(list)
        numbers.append(sum_list(list))
    return numbers



def starter(weight, wins):
    if 150 <= weight < 160 and wins > 5:
        return True
    if weight > 199 or wins > 20:
        return True
    else:
        return False


def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True1
    return False


def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = math.sqrt(
        (center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)
    circle_one = Circle(center, radius)
    circle_one.setFill("light blue")
    circle_one.draw(win)

    win.getMouse()


def did_overlap(circle_one, circle_two):
    if math.sqrt(math.pow(circle_two.getCenter().getX() - circle_one.getCenter().getX(), 2)) + (math.pow(circle_two.getCenter().getY() - circle_one.getCenter().getY(), 2)) <= circle_one.getRadius() + circle_two.getRadius():
        return True
    return False

if __name__ == '__main__':
    pass
