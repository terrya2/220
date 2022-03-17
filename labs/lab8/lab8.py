"""
Autumn Terry
lab8.py
Create a program using graphics and deicison statements.
I certify that this assignment is entirely my own work.
"""
import math

from graphics import *
from random import randint

def bumper():
    width = 500
    height = 500
    win = GraphWin("Bumper", width, height)

    center1 = Point(100, 100)
    radius1 = 70
    circle1 = Circle(center1, radius1)
    circle1.draw(win)
    circle1.setFill("White")

    center2 = Point(300, 400)
    radius2 = 100
    circle2 = Circle(center2, radius2)
    circle2.draw(win)
    circle2.setFill("Yellow")
    move_value = 5
    circle1_x = get_random(move_value)
    circle1_y = get_random(move_value)
    circle2_x = get_random(move_value)
    circle2_y = get_random(move_value)
    while win.checkKey()!=("G"):
        circle1.move(circle1_x, circle1_y)
        circle2.move(circle2_x, circle2_y)
        if did_collide(circle1, circle2):
            circle1_x = -circle1_x
            circle1_y = -circle1_y
            circle2_x = -circle2_x
            circle2_y = -circle2_y
        if hit_verticle(circle1, win):
            circle1_y = -circle1_y
        if hit_verticle(circle2, win):
            circle2_y = -circle2_y
        if hit_horizontal(circle1, win):
            circle1_x = -circle1_x
        if hit_horizontal(circle2, win):
            circle2_x = -circle2_x
    win.close()

def get_random(move_amount):
    return randint(-move_amount, move_amount)

def did_collide(ball, ball2):
    if math.sqrt(math.pow(ball2.getCenter().getX() - ball.getCenter().getX(),2)) + (math.pow(ball2.getCenter().getY() - ball.getCenter().getY(),2)) <= ball.getRadius() + ball2.getRadius():
        return True
    return False
def hit_verticle(ball, win):
    if ball.getCenter().getY() - ball.getRadius() == 0:
        return True
    if ball.getCenter().getY() + ball.getRadius() == win.getHeight():
        return True
    return False

def hit_horizontal(ball, win):
    if ball.getCenter().getX() - ball.getRadius() == 0:
        return True
    if ball.getCenter().getX() + ball.getRadius() == win.getWidth():
        return True
    return False

def get_random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return color_rgb(r, g, b)