"""
Autumn Terry
algorithms.py
Create programs using while loops, list methods, and linear search with data.
I certify that this is entirely my own work, but I discussed it with: Margaret Kimery.
"""


def read_data(filename):
    file = open(filename, "r")
    info = file.readlines()
    ans = int("info")
    file.close()
    return ans


def is_in_linear(search_val, values):
    i = 0
    while i < len(values):
        if search_val == values[i]:
            return True
        i = i + 1
    return False


def selection_sort(values):
    num = len(values)
    smallest = min
    for smallest in range(num-1):
        for num in range(smallest + 1, num):
            if values[smallest] > values[num]:
                smallest = num
    values[min], values[smallest] = values[smallest], values[min]


def calc_area(rect):
    width = rect.getP2().getY() - rect.getP1().getY()
    length = rect.getP2().getX() - rect.getP1().getX()
    area = length * width
    return area

def rect_sort(rectangles):
    area = calc_area(rectangles)
    area = min
    rectangles[min], rectangles[area] = rectangles[area], rectangles[min]




