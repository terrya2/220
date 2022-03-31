import math

import hw8
from tests.test_framework import *
from graphics import *


def main():
    builder = TestBuilder("hw 8", 'hw8.py', linter_points=20, default_test_points=2)
    builder.add_to_blacklist({
        'while.*:': 'while loops not allowed for this assignment. please remove it to continue',
    })
    builder.add_items(build_add_ten_tests(10))
    builder.add_items(build_square_each_tests(10))
    builder.add_items(build_sum_list_tests(10))
    builder.add_items(build_to_numbers_tests(10))
    builder.add_items(build_sum_of_squares_tests(10))
    builder.add_items(build_starter_tests())
    builder.add_items(build_leap_year_tests(10))
    builder.add_items(build_did_overlap_tests(10))
    builder.run()


def build_did_overlap_tests(n):
    test_name = 'did_overlap'
    section = Section(test_name)
    test_result = True
    c1 = []
    c2 = []
    results = []
    for i in range(1, n + 1):
        p1_x = random.randint(-100, 100)
        p1_y = random.randint(-100, 100)
        p2_x = random.randint(-100, 100)
        p2_y = random.randint(-100, 100)
        distance = math.sqrt(math.pow(p2_x - p1_x, 2) + math.pow(p2_y - p1_y, 2))
        r1 = random.randint(1, int(distance))
        margin = 0 if test_result else 0.00001
        r2 = distance - r1 - margin
        c1.append(Circle(Point(p1_x, p1_y), r1))
        c2.append(Circle(Point(p2_x, p2_y), r2))
        results.append(test_result)
        test_result = not test_result

    c1_generator = gen(c1)
    c2_generator = gen(c2)
    results_generator = gen(results)

    for j in range(1, n + 1):
        section.add_items(
            Test(f'{test_name} {i}', lambda: hw8.did_overlap(next(c1_generator), next(c2_generator)),
                 next(results_generator),
                 data=[f'Circle 1 - ({p1_x}, {p1_y}), radius: {r1}', f'Circle 2 - ({p2_x}, {p2_y}), radius: {r2}']))
    return section


def build_leap_year_tests(n):
    test_name = 'leap_year'
    section = Section(test_name)
    leap_years = []
    for i in range(2020):
        year = i * 4
        check_year = str(year / 100)
        if check_year.split('.')[-1] == '0':
            if str(year / 400).split('.')[-1] == '0':
                leap_years.append(year)
        else:
            leap_years.append(year)
    all_years = [x for x in range(5000)]
    start = 0
    step = len(all_years) // n
    stop = step
    all_year_groups = []
    for i in range(n):
        all_year_groups.append(all_years[start:stop])
        start += step
        stop += step
    for test_number, year_group in enumerate(all_year_groups):
        passed_all = True
        for year in year_group:
            outcome, result = run_safe(lambda: hw8.leap_year(year))
            if not outcome:
                section.add_items(Test(f'{test_name} {test_number + 1}', True, False, show_actual_expected=False,
                                       exception_message=result))
                break
            else:
                passed_all = (year in leap_years) == result
                if not passed_all:
                    section.add_items(
                        Test(f'years {test_number * step} - {(test_number + 1) * step - 1}', result, not result,
                             data=[year]))
                    break
        if passed_all:
            section.add_items(Test(f'years {test_number * step} - {(test_number + 1) * step - 1}', True, True))
    return section


def build_starter_tests():
    test_name = 'starter'
    section = Section(test_name)
    input_expected = [(150, 5, True), (150, 4, False), (149, 5, False), (160, 5, False), (161, 5, False),
                      (200, 1, True), (199, 20, False), (199, 21, True), (201, 21, True), (300, 0, True)]
    expected_list = [x[2] for x in input_expected]
    weight_list = [x[0] for x in input_expected]
    wins_list = [x[1] for x in input_expected]
    expected = gen(expected_list)
    weight = gen(weight_list)
    wins = gen(wins_list)
    test_number = 1
    for _ in input_expected:
        section.add_items(
            Test(f'{test_name} {test_number}', lambda: hw8.starter(next(weight), next(wins)), next(expected),
                 data=[(weight, wins)]))
        test_number += 1
    return section


def build_sum_of_squares_tests(n):
    test_name = 'sum_of_squares'
    section = Section(test_name)
    for i in range(n):
        lines = random.randint(1, 7)
        line_list_strings_input = []
        line_list_nums = []
        line_list_sums_expected = []
        for j in range(lines):
            numbers_count = random.randint(1, 7)
            numbers_list = [round(random.uniform(1, 9), 2) for _ in range(numbers_count)]
            line_list_nums.append(numbers_list)
            line_list_sums_expected.append(sum([x ** 2 for x in numbers_list]))
            line_string = ', '.join([str(x) for x in numbers_list])
            line_list_strings_input.append(line_string)
        outcome, result = run_safe(lambda: hw8.sum_of_squares(line_list_strings_input))
        if outcome:
            section.add_items(
                Test(f'{test_name} {i + 1}', result, line_list_sums_expected, data=[line_list_strings_input]))
        else:
            section.add_items(
                Test(f'{test_name} {i + 1}', True, False, show_actual_expected=False, exception_message=result))
    return section


def build_add_ten_tests(n):
    test_name = 'add_ten'
    section = Section(test_name)
    for i in range(n):
        list_len = random.randint(0, 25)
        original_list = [random.randint(-100, 100) for _ in range(list_len)]
        add_ten_list = [x + 10 for x in original_list]
        outcome, result = run_safe(lambda: hw8.add_ten(original_list))
        if outcome and not result:
            section.add_items(Test(f'{test_name} {i + 1}', original_list, add_ten_list, data=[original_list]))
        elif not outcome:
            section.add_items(
                Test(f'{test_name} {i + 1}', True, False, show_actual_expected=False, exception_message=result))
        elif result:
            section.add_items(Test(f'{test_name} {i + 1}', True, False, show_actual_expected=False,
                                   exception_message='function should not return a value'))
        else:
            section.add_items(Test(f'{test_name} {i + 1}', True, False, show_actual_expected=False,
                                   exception_message='an unknown error occurred'))

    return section


def build_square_each_tests(n):
    test_name = 'square_each'
    section = Section(test_name)
    for i in range(n):
        list_len = random.randint(0, 25)
        original_list = [random.randint(-100, 100) for _ in range(list_len)]
        square_list = [x ** 2 for x in original_list]
        outcome, result = run_safe(lambda: hw8.square_each(original_list))
        if outcome:
            section.add_items(Test(f'{test_name} {i + 1}', original_list, square_list, data=[original_list]))
        elif not outcome:
            section.add_items(
                Test(f'{test_name} {i + 1}', True, False, show_actual_expected=False, exception_message=result))
        elif result:
            section.add_items(Test(f'{test_name} {i + 1}', True, False, show_actual_expected=False,
                                   exception_message='function should not return a value'))
        else:
            section.add_items(Test(f'{test_name} {i + 1}', True, False, show_actual_expected=False,
                                   exception_message='an unknown error occurred'))

    return section


def build_sum_list_tests(n):
    test_name = 'sum_list'
    section = Section(test_name)
    inputs = []
    for i in range(n):
        list_len = random.randint(0, 25)
        inputs.append([random.randint(-100, 100) for _ in range(list_len)])
    inputs_gen = gen(inputs)
    for i in range(n):
        section.add_items(
            Test(f'{test_name} {i + 1}', lambda: hw8.sum_list(next(inputs_gen)), sum(inputs[i]), data=[inputs[i]]))
    return section


def build_to_numbers_tests(n):
    test_name = 'to_numbers'
    section = Section(test_name)
    for i in range(n):
        list_len = random.randint(0, 25)
        original_list = [random.uniform(-100, 100) for _ in range(list_len)]
        string_list = [str(x) for x in original_list]
        original_string_list = [x for x in string_list]
        outcome, result = run_safe(lambda: hw8.to_numbers(string_list))
        if outcome and not result:
            section.add_items(Test(f'{test_name} {i + 1}', string_list, original_list, data=[original_string_list]))
        elif not outcome:
            section.add_items(
                Test(f'{test_name} {i + 1}', True, False, show_actual_expected=False, exception_message=result))
        elif result:
            section.add_items(Test(f'{test_name} {i + 1}', True, False, show_actual_expected=False,
                                   exception_message='function should not return a value'))
        else:
            section.add_items(Test(f'{test_name} {i + 1}', True, False, show_actual_expected=False,
                                   exception_message='an unknown error occurred'))

    return section
