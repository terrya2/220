"""
Name: Autumn Terry
hw2.py
Creating codes that allow users to do arithmetic by giving input and producing output.
I certify that this assignment is entirely my own work.

"""
import math
# dot notation

def sum_of_threes():
    upper = eval(input("enter the upper bound: "))
    for i in range(upper):
        sum = i % upper
    print("sum of threes is", sum)


def multiplication_table():
    for i in range (1,11):
        for j in range (1,11):
            print(i * j, end='\t')
        print()

def triangle_area():
    side_a = eval(input("enter length of side a: "))
    side_b = eval(input("enter length of side b: "))
    side_c = eval(input("enter length of side c: "))
    s = (side_a + side_b + side_c) / 2
    area = math.sqrt(s * (s - side_a) * (s - side_b) * (s - side_c))
    print("area is: ", area)

def sum_squares():
    lower = eval(input("enter lower range: "))
    upper = eval(input("enter upper range: "))
    sum = 0
    for i in range(lower,upper, 1):
        sum = (lower ^ 2) * (i ^ 2) * (upper ^ 2)
    sum_squares = sum                                  
    print("sum of squares is: ",sum_squares)

def power():
    base = eval(input("enter base: "))
    exponent = eval(input("enter exponent: "))
    total = base ^ (exponent)
    print("The answer is: ", total)

if __name__ == '__main__':
    pass
