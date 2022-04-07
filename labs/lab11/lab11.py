"""
Autumn Terry
lab11.py
Uses classes and object lists to create a program.
I certify that this assignment is my own work, but I discussed it with: Margaret Kimery.
"""

from graphics import *
from lab10.button import Button
from lab10.door import Door
from random import randint

def three_door_game():
    width = 500
    height = 500
    win = GraphWin("three door game", width, height)

    door1 = Rectangle(Point(70, 100), Point(160, 400))
    door1.setFill("tan")
    door1 = Door(door1, "door 1")
    door1.draw(win)

    door2 = Rectangle(Point(175, 100), Point(260, 400))
    door2.setFill("tan")
    door2 = Door(door2, "door 2")
    door2.draw(win)

    door3 = Rectangle(Point(270, 100), Point(360, 400))
    door3.setFill("tan")
    door3 = Door(door3, "door 3")
    door3.draw(win)

    have_txt = Text(Point(250, 80), "I have a secret door")
    have_txt.draw(win)
    guess_txt = Text(Point(250, 450), "Click to guess which is the secret door!")
    guess_txt.draw(win)

    wl_box1 = Rectangle(Point(40, 30), Point(100, 65))
    wl_box1.draw(win)
    wl_msg1 = Text(Point(40, 20), "wins")
    wl_msg1.draw(win)
    wl_box2 = Rectangle(Point(70, 30), Point(100, 65))
    wl_box2.draw(win)
    wl_msg2 = Text(Point(85, 20), "losses")
    wl_msg2.draw(win)
    win_score = Text(Point(50, 40), "0")
    win_score.draw(win)
    losses_score = Text(Point(90, 40), "0")
    losses_score.draw(win)

    quit_box = Rectangle(Point(330, 30), Point(400, 65))
    quit_box = Button(quit_box, "quit")
    quit_box.draw(win)

    random_door = randint(1, 3)

    if random_door == 1:
        door1.set_secret(True)
    elif random_door == 2:
        door2.set_secret(True)
    elif random_door == 3:
        door3.set_secret(True)

    user_click = win.getMouse()

    num_wins = 0
    num_losses = 0
    again = guess_txt.setText("click anywhere to play again")

    while not quit_box.is_clicked(user_click):

        if door1.is_clicked(user_click):
            if door1.is_secret():
                door1.color_door("green")
                have_txt.setText("you win!")
                wins = num_wins + 1
                wins = win_score.setText(win)
                return again
            else:
                door1.color_door("red")
                have_txt.setText("sorry, incorrect!")
                losses = num_losses + 1
                losses = win_score.setText(win)
                return again

        if door2.is_clicked(user_click):
            if door2.is_secret():
                door2.color_door("green")
                have_txt.setText("you win!")
                wins = num_wins + 1
                wins = win_score.setText(win)
                return again
            else:
                door2.color_door("red")
                have_txt.setText("sorry, incorrect!")
                losses = num_losses + 1
                losses = win_score.setText(win)
                return again

        if door3.is_clicked(user_click):
            if door3.is_secret():
                door3.color_door("green")
                have_txt.setText("you win!")
                wins = num_wins + 1
                wins = win_score.setText(win)
                return again
            else:
                door3.color_door("red")
                have_txt.setText("sorry, incorrect!")
                losses = num_losses + 1
                losses = win_score.setText(win)
                return again
        user_click = win.getMouse()

        if quit_box.is_clicked(user_click):
            win.close()
        else:
            have_txt.setText("i have a secret door")
            guess_txt.setText("click to guess which is the secret door")
            door1 = Rectangle(Point(70, 100), Point(160, 400))
            door1.setFill("tan")
            door1 = Door(door1, "door 1")
            door1.draw(win)
            door2 = Rectangle(Point(175, 100), Point(260, 400))
            door2.setFill("tan")
            door2 = Door(door2, "door 2")
            door2.draw(win)
            door3 = Rectangle(Point(270, 100), Point(360, 400))
            door3.setFill("tan")
            door3 = Door(door3, "door 3")
            door3.draw(win)

    win.close()










