"""
Autumn Terry
lab4.py
Create an animation through the use of graphics and text.
I certify that this assignment is entirely my own work.
"""

from graphics import *

def greeting_card():
    win = GraphWin("Heart", 400, 200)
    tri = Polygon(Point(30, 50), Point(70, 110), Point(105, 50))
    tri.setOutline("pink")
    tri.setFill("pink")
    tri.draw(win)

    shape1 = Circle(Point(50, 50), 20)
    shape1.setOutline("pink")
    shape1.setFill("pink")
    shape1.draw(win)
    shape2 = Circle(Point(85, 50), 20)
    shape2.setOutline("pink")
    shape2.setFill("pink")
    shape2.draw(win)

    greeting = Text(Point(70, 70), "Happy Valentine's Day!")
    greeting.setFace("arial")
    greeting.setTextColor("red")
    greeting.draw(win)

    line = Line(Point(50,110), Point(100, 100))
    line.setArrow("last")
    line.draw(win)

    for i in range(4):
        line.move(20, 0)
        time.sleep(0.1)

    greeting.setText("Click anywhere to close")
    greeting.move(100,100)
    win.getMouse()
    win.close()

