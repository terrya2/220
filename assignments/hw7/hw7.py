"""
Autumn Terry
hw7.py
Writing functions and reading and writing text files.
I certify that this assignment is entirely my own work.
"""

from encryption import encode

def number_words(in_file_name, out_file_name):
    file = open(in_file_name, "r")
    text = file.read().split()
    new_file = open(out_file_name, "x")
    new_text = ""
    for i in range(len(text)):
        new_text += (str(i + 1) + " " + text[i]) + "\n"
    new_file.write(new_text)
    file.close()
    new_file.close()

def hourly_wages(in_file_name, out_file_name):
    file = open(in_file_name, "r")
    out_file = open(out_file_name, "a")
    text = file.read()
    x = text.split("\n")
    for person in x:
        data = person.split()
        hourly_wage = eval(data[2])
        number_of_hours_worked = eval(data[3])
        pay = (number_of_hours_worked * hourly_wage) + (1.65 * number_of_hours_worked)
        out = data[0] + " " + data[1] + " " + "{:.2f}" + "\n"
        out_file.write(out.format(pay))
    file.close()
    out_file.close()

def calc_check_sum(isbn):
    enter_isbn = isbn.replace("-", "")
    total_ans = 0
    for i in range(10):
        curVal = eval(enter_isbn[::-1])
        digit = eval(curVal[i])
        total_ans = total_ans + (digit * (1+i))
    return total_ans

def send_message(file_name, friend_name):
    file = open(file_name, "r")
    info = file.read()
    new_file = open(friend_name + ".txt", "w")
    new_file.write(info)

    file.close()
    new_file.close()


def send_safe_message(file_name, friend_name, key):
    file = open(file_name, "r")
    content = file.read()
    info = content.split("\n")
    new_friend = open(friend_name, "a")
    for i in range(len(info)):
        encoded = encode(info[i], key)
        new_friend.write(encoded)


def send_uncrackable_message(file_name, friend_name, pad_file_name):
    file = open(file_name, "r")
    pad_file = open(pad_file, "w")


if __name__ == '__main__':
    pass
