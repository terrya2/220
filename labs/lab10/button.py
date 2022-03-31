"""
Autumn Terry
button.py
Create a program with classes and objects
I certify that this assignment is my own work, but I discussed it with: Margaret Kimery
"""
from graphics import *
class Button:
    def __init__(self, shape, label):
        self.shape = shape
        self.text = Text(shape.getCenter(), label)

    def get_label(self):
        button_label = self.text.getText()
        return button_label

    def set_label(self, label):
        self.text.setText(label)

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self, win):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point):
        point1 = self.shape.getP1()
        point2 = self.shape.getP2()

        if point1.getX() <= point.getX() <= point2.getX() and point1.getY() <= point.getY <= point2.getY():
            return True
        else:
            return False

    def color_button(self, color):
        self.shape.setFill(color)
