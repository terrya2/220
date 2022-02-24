"""
Autumn Terry
lab6.py
Creating code that processes string data and implements ciphers.
I certify that this assignment is entirely my own work.
"""

from graphics import *

def vigenere():
    width = 500
    height = 500
    win = GraphWin("Vigenere", width, height)

    instructions = Text(Point(70, 80), "Message to code")
    instructions.draw(win)

    instructions2 = Text(Point(100, 115), "Key to use")
    instructions2.draw(win)

    messageBox = Entry(Point(300, 80), 50)
    messageBox.draw(win)
    messageBox.setFill("grey")

    messageBox2 = Entry(Point(250, 115), 30)
    messageBox2.draw(win)
    messageBox2.setFill("grey")

    rect = Rectangle(Point(200,210), Point(300,260))
    rect.draw(win)

    text = Text(Point(250, 250), "Encode")
    text.draw(win)

    win.getMouse()
    rect.undraw()
    text.undraw()

    result_text = Text(Point(250, 270), "Resulting Message")
    result_text.draw(win)
    result = messageBox.getText()
    result = result.upper()
    result = result.replace(" ", "")
    print(result)
    result2 = messageBox2.getText()
    result2 = result2.upper()
    result2 = result2.replace(" ", "")
    print(result2)

    ret = ""
    for i in range(len(result)):
        a = (ord(result[i]) - 65)
        b = (ord(result2[i % len(result2)]) - 65)
        c = ((a + b) % 26) + 65
        ret += (chr(c))

    msg = Text(Point(250, 290), ret)
    msg.draw(win)


    instructions = Text(Point(250, 450), "Click Anywhere to Close Window")
    instructions.draw(win)
    win.getMouse()
    win.close()
