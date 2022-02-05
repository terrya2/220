"""
Autumn Terry
hw3.py
Create programs that can solve problems by using loops, inputs, and outputs.
I certify that this assignment is entirely my own work.

"""

def average():
    num_grades = eval(input("how many grades will you enter?: "))
    sum = 0
    for i in range(num_grades):
        grade_val = eval(input("enter grade: "))
        sum =  sum + grade_val
    avg = sum / num_grades
    print("average is ",avg)


def tip_jar():
    sum = 0
    for i in range(5):
        donation = eval(input("how much would you like to donate?: "))
        sum = sum + donation
    print("total tips: ", sum)


def newton():
    number = eval(input("what number do you want to square root?: "))
    approx = eval(input("how many times should we improve the approximation?: "))
    ans = (approx + (number / approx)) / (2)
    print("the square root is approximately ", ans)


def sequence():
    sum = 0
    terms = eval(input("how many terms would you like?: "))
    for i in range(terms):
        sum = (i + 1) % 2 + i
    print (sum)

def pi():
    terms = eval(input("how many terms in the series?: "))
    sum = 0
    for i in range(terms):
      sum = ((i - 1) % 2 + i) * ((i + 1) % 2 + i)
    print(sum)



if __name__ == '__main__':
    pass
