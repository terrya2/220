"""
Autumn Terry
hw9.py
Create a program using files, functions, conditionals, decision, and repeitition structures
I certify that this assignment is my own work
"""

import random

def get_words(file_name):
    word_file = open(file_name, "r")
    words = word_file.read()
    return words

def get_random_words(words):
     return random.randint(words.txt, words.txt)

def letter_in_secret_word(letter, secret_word):
    if letter <= secret_word:
        return True
    else:
        return False
def already_guessed(letter, guesses):
    if letter ==  guesses:
        return True
    else:
        return False
def make_hidden_secret(secret_word, guesses):
    for guesses in secret_word:
        word = str("_")
        guesses = secret_word + word

def won(guessed):
    if guessed == get_random_words:
        return True
    else:
        return False

def play_graphics(secret_word):
    pass

def play_command_line(secret_word):
    print("enter a letter: ")

    if letter_in_secret_word == secret_word:
        print("winner!", secret_word)
    else:
        print(" you have not won", secret_word)
if __name__ == '__main__':
    pass
    # play_command_line(secret_word)
    # play_graphics(secret_word)