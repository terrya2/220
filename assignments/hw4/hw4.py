"""
Autumn Terry
hw4.py
Creating programs that create graphics through the use of previously supplied packages.
I certify that this assignment is entirely my own work.
"""

from graphics import *


def squares():
    width = 400
    height = 400
    win = GraphWin("Clicks", width, height)

    num_clicks = 5

    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move square")
    instructions.draw(win)

    rect = Rectangle(Point(50, 0), Point(0, 50))
    rect.setOutline("red")
    rect.setFill("red")
    rect.draw(win)

    for i in range(num_clicks):
        click = win.getMouse()
        center = rect.getCenter()

    rect_new = rect.clone()
    change_x = click.getX() - center.getX()
    change_y = click.getY() - center.getY()
    rect_new.move(change_x, change_y)
    rect_new.draw(win)

    instructions.setText("Click again to close")
    win.getMouse()
    win.close()

    squares()

def rectangle():
    width = 400
    height = 400
    win = GraphWin("Build a Rectangle", width, height)

    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)

    rectangle = Rectangle(p1, p2)
    rectangle.draw(win)

    rect_width = p1
    rect_length = p2
    perimeter = 2 * (rect_length + rect_width)
    area = p1 * p2
    perimeter.setText(perimeter)
    area.setText(area)

    instructions = Text("Click again to close")
    instructions.setText("Click again to close")
    win.getMouse()
    win.close()

    rectangle()


def circle():
    width = 400
    height = 400
    win = GraphWin("Draw a circle", width, height)

    center = win.getMouse()
    center.draw(win)
    circum = win.getMouse()
    circum.draw(win)

    xvar = circum.getX() - center.getX()
    yvar = circum.getY() - center.getY()
    radius = ((xvar ** 2) + (yvar ** 2)) ** (1 / 2)

    circle = Circle(center, radius)
    circle.draw(win)

    instructions = Text("Click again to close")
    instructions.setText("Click again to close")
    win.getMouse()
    win.close()

    circle()

def pi2():
    num_terms = eval(input("enter number of terms to sum:"))
    total = 0
    for i in range(1, num_terms):

        print("pi approximation:")
        print("accuracy: ")

    pi2()
if __name__ == '__main__':
    pass
