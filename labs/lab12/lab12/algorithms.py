"""
Autumn Terry
algorithms.py
Create programs using while loops, list methods, and linear search with data.
I certify that this is entirely my own work, but I discussed it with: Margaret Kimery.
"""


def read_data(filename):
    file = open(filename, "r")
    info = file.readlines()
    ans = eval("info")
    file.close()
    return ans


def is_in_linear(search_val, values):
    i = 0
    while i < len(values):
        if search_val == values[i]:
            return True
        i = i + 1
    return False

