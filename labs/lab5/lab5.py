"""
Autumn Terry
lab5.py
Creating programs with graphics, strings, and lists.
I certify that this assignment is entirely my own work.
"""

from graphics import *
import math

def triangle():
    width = 500
    height = 500
    win = GraphWin("Triangle", width, height)

    instructions = Text(Point(300, 300), "Click three times to draw triangle")
    instructions.draw(win)

    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    triangle = Polygon(p1, p2, p3)
    triangle.draw(win)

    length_1 = math.sqrt((p2.getX() - p1.getX()) ** 2 + ((p2.getY() - p1.getY()) ** 2))
    length_2 = math.sqrt((p3.getX() - p1.getX()) ** 2 + ((p3.getY() - p1.getY()) ** 2))
    length_3 = math.sqrt((p3.getX() - p2.getX()) ** 2 + ((p3.getY() - p2.getY()) ** 2))

    perimeter = length_1 + length_2 + length_3

    side = (length_1 + length_2 + length_3) / 2
    area = math.sqrt(side * (side - length_1) * (side - length_2) * (side - length_3))

    perimeter_text = Text(Point(250, 450), "Perimeter: " + str(perimeter))
    perimeter_text.draw(win)
    area_text = Text(Point(250, 400), "Area:" + str(area))
    area_text.draw(win)

    instructions = Text(Point(250, 250), "Click to close")
    instructions.draw(win)
    win.getMouse()
    win.close()

def color_shape():
    win_width = 500
    win_height = 500
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    r = Entry(Point(win_width / 2 - 25, win_height / 2 + 40), 3)
    r.draw(win)
    g = Entry(Point(win_width / 2 - 25, win_height / 2 + 70), 3)
    g.draw(win)
    b = Entry(Point(win_width / 2 - 25, win_height / 2 + 100), 3)
    b.draw(win)

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    for i in range(5):
        win.getMouse()
        red = eval(r.getText())
        blue = eval(b.getText())
        green = eval(g.getText())
        shape.setFill(color_rgb(red, green, blue))

    # Wait for another click to exit
    win.getMouse()
    win.close()


def process_string():
    string = str(input("Enter a string"))
    character_first = string[0]
    print("First character is: ", character_first)
    character_last = string[-1]
    print("Last character is :", character_last)
    position = string[2:6]
    print(position)
    first = character_first
    last = character_last
    print(first, last)
    first_three = string[0:4] * 10
    print(first_three)
    for letter in string:
        print(letter)
    len(string)
    print(len(string))

def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    print("x: ", values[1] + values[3])
    print("x: ", values[0] + values[2])
    print("x: ", values[1] * 5)
    print("x: ", values[2:5])
    print("x: ", [values[3:4], values[0]])
    print("x: ", [values[3], values[0], values[5]])
    print("x: ", values[0] + values[2] + float(values[5]))
    print("x: ", len(values))


def another_series():
    num_terms = eval(input("enter number of terms: "))
    sum = 0
    for i in range(int(((num_terms - 1) + 3) / 3)):
        sum = sum + 2

    for i in range(int(((num_terms - 2) + 3) / 3)):
        sum = sum + 4

    for i in range(int(((num_terms - 3) + 3) / 3)):
        sum = sum + 6

    print(sum)

def target():
    width = 500
    height = 500
    win = GraphWin("Target", width, height)

    center1 = Point(250, 250)
    radius1 = 250
    circle_white = Circle(center1, radius1)
    circle_white.draw(win)
    circle_white.setFill("white")

    center2 = Point(250, 250)
    radius2 = 200
    circle_black = Circle(center2, radius2)
    circle_black.draw(win)
    circle_black.setFill("black")

    center3 = Point(250, 250)
    radius3 = 150
    circle_blue = Circle(center3, radius3)
    circle_blue.draw(win)
    circle_white.setFill("blue")

    center4 = Point(250, 250)
    radius4 = 100
    circle_red = Circle(center4, radius4)
    circle_red.draw(win)
    circle_red.setFill("red")

    center1 = Point(250, 250)
    radius1 = 50
    circle_yellow = Circle(center1, radius1)
    circle_yellow.draw(win)
    circle_yellow.setFill("yellow")


    instructions = Text(Point(250, 250), "Click to close")
    instructions.draw(win)
    win.getMouse()
    win.close()