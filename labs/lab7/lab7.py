"""
Autumn Terry
lab7.py
Create a function that uses numeric information from a text file.
I certify that this assignment is entirely my own work.
"""


def weighted_average(in_file_name, out_file_name):
    file = open(in_file_name, "r")
    new_file = open(out_file_name, "w")
    info = file.readlines()
    string = len(info)
    class_avg = 0
    for i in range(string):
        index = info[i]
        colon = index.find(":")
        first_part = index[:colon]
        second_part = index[colon + 2: len(index) - 1]
        #print(first_part)
        #print(second_part)
        info_list = second_part.split()
        length = len(info_list)
        denominator = length / 2
        total_weight = 0
        total_grade = 0
        class_avg = 0
        for j in range(0, length, 2):
            weight = eval(info_list[j])
            grade = eval(info_list[j + 1])
            total_weight = total_weight + weight
            total_grade = total_grade + grade
            class_avg = class_avg + (weight * grade) + (weight * grade) + (weight * grade)
        if total_weight == 100:
            ans_individual = (first_part + "'s average:", round((total_grade / denominator), 1))
            new_file.write(str(ans_individual))
        elif total_weight < 100:
            ans_total = (first_part + "'s average: Error: The weights are less than 100.")
            new_file.write(str(ans_total))
        else:
            ans_weight = (first_part + "'s average: Error: The weights are more than 100.")
            new_file.write(str(ans_weight))

    ans = "Class average:", class_avg / 100
    new_file.write(str(ans))
    file.close()
    new_file.close()
