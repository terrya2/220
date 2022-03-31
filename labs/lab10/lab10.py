"""
Autumn Terry
lab9.py
Create a program with classes and objects
I certify that this assignment is my own work, but I discussed it with: Margaret Kimery

"""

from button import Button
from door import Door
from graphics import *

def main():
    win = ("Win", 400, 400)
    win.draw(win)

    button = Button()
    door = Door()

    color = door.color_door(Door)

    door_close = door.close(Door)

    door_click = door.is_clicked(Door)

    button_click = button.is_clicked(Button)

    win.getMouse()
    win.close()









