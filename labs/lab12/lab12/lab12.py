"""
Autumn Terry
lab12.py
Create programs using while loops, list methods, and linear search with data.
I certify that this is entirely my own work, but I discussed it with: Margaret Kimery.
"""

from random import randint


def find_and_remove_first(list, value):
    val = list.index(value)
    list.remove(value)
    name = "autumn"
    list.insert(val, name)


def good_input():
    number = eval(input("enter a number: "))
    while number in range(1, 11):
        number = eval(input("enter a number: "))
        if number < 1:
            print("this is wrong, input another number in the range: ")
        number = eval(input("enter a number: "))
        if number > 11:
            print("this is wrong, input another number in the range: ")
        number = eval(input("enter a number: "))
        if number <= 11 or number >= 1:
            print(number)


def num_digits():
    value = eval(input("enter a positive integer: "))
    while value > 0 or value > -1:
        i = 0
        if value > 0 or value > -1:
            ans = value / int(10)
            i = i + 1
            print(i + ans, "is the number of digits")
        value = eval(input("enter a positive integer: "))


def hi_lo_game():
    num = randint(1, 100)
    num_guesses = 7
    while num_guesses in range(1, 8):
        guess = eval(input("enter a guess: "))
        if guess > num:
            print("too high")
        if guess < num:
            print("too low")
        if guess == num:
            print("correct")
            print("You win in", 7 - num_guesses, "guesses!")
            num_guesses = 9
        num_guesses = num_guesses - 1

    if num_guesses == 0:
        print("Sorry, you lose. The number was", num)


def main():
    good_input()
    num_digits()
    hi_lo_game()