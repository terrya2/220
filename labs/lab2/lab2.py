"""

Autumn Terry
lab2.py
Calculating the means of a set of numbers by creating codes to provide outputs through the methods of RMS average,
Harmonic mean, and Geometric mean.
I certify that this assignment is entirely my own work.

"""

def means():

    rms_average = 0
    harmonic_mean = 0
    geometric_mean = 1
    user_values = eval(input("enter the values to be entered: "))
    for i in range(user_values):
        values = eval(input("enter value: "))
        rms_average = rms_average + values ** 2
        harmonic_mean = harmonic_mean + (1/values)
        geometric_mean = geometric_mean * values
    rms = rms_average / user_values
    print("The RMS is", rms**(1/2))
    harmonic = (user_values/harmonic_mean)
    print("The harmonic mean is", harmonic)
    geometric = (geometric_mean)**(1/user_values)
    print("The geometric mean is", geometric)
