from random import randrange

import hw1
from tests.test_framework import *


def main():
    builder = TestBuilder("hw 1", 'hw1.py', linter_points=20, default_test_points=2)
    builder.add_to_blacklist({
        'if (?!__name__).*:': 'if statements not allowed for this assignment. please remove it to continue',
        'while.*:': 'while loops not allowed for this assignment. please remove it to continue',
        '\[*\]': 'lists are not allowed for this assignment. please remove it to continue',
        'list': 'lists are not allowed for this assignment. please remove it to continue'
    })
    builder.add_items(
        build_section('calc_rec_area', [("2", "3")], ["6"], build_calc_rec_area_tests(9), hw1.calc_rec_area))
    builder.add_items(
        build_section('calc_volume', [("2", "3", "4")], ["24"], build_calc_volume_tests(9), hw1.calc_volume))
    builder.add_items(build_section('shooting_percentage', [("10", "4")], ["40.0"], build_shooting_percentage_tests(9),
                                    hw1.shooting_percentage))
    coffee_section = build_section('coffee', [["2"]], ["24.22"], build_coffee_tests(9), hw1.coffee)

    def coffee_comp_func(actual, expected):
        return abs(float(actual) - float(expected)) < 0.000000000001

    test: Test
    for test in coffee_section.outline:
        test.comp_func = coffee_comp_func

    builder.add_items(coffee_section)
    builder.add_items(
        build_section('kilometers_to_miles', [["1.61"]], ["1.0"], build_kilometers_to_miles_tests(9),
                      hw1.kilometers_to_miles))
    builder.run()


def build_section(name, tests, expected, dynamic_tests, test_func):
    section = Section(name)
    for test in dynamic_tests:
        tests.append(test['test'])
        expected.append(test['expected'])
    results = []
    for test in tests:
        results.append(get_IO(test_func, test))
    actual_results = gen(results)
    for i, ex in enumerate(expected):
        output, res, error = next(actual_results)
        test_name = f'{name} {i + 1}'
        if error:
            test = Test(test_name, f'error: {error}', ex)
        else:
            full_output = " ".join(output)
            output_numbers = get_all_numbers_in_string(full_output)
            try:
                test = Test(test_name, output_numbers[0], ex, data=[f'inputs: {tests[i]}'])
            except:
                test = Test(test_name, f'error: incorrect output', ex)
        section.add_items(test)
    return section


def build_kilometers_to_miles_tests(n):
    results = []
    for i in range(n):
        clicks = randrange(1, 100)
        results.append({'test': [(str(clicks))], 'expected': str(clicks / 1.61)})
    return results


def build_coffee_tests(n):
    results = []
    for i in range(n):
        lbs = randrange(1, 100)
        results.append({'test': [str(lbs)], 'expected': str(10.5 * lbs + 0.86 * lbs + 1.50)})
    return results


def build_shooting_percentage_tests(n):
    results = []
    for i in range(n):
        num = randrange(1, 100)
        denom = randrange(1, 100)
        results.append({'test': (str(denom), str(num)), 'expected': str(num / denom * 100)})
    return results


def build_calc_volume_tests(n):
    results = []
    for i in range(n):
        w = randrange(0, 100)
        multiplier_1 = randrange(0, 100)
        multiplier_2 = randrange(0, 100)
        expected = w * multiplier_1 * multiplier_2
        results.append({'test': (str(multiplier_1), str(w), str(multiplier_2)), 'expected': str(expected)})
    return results


def build_calc_rec_area_tests(n):
    results = []
    for i in range(n):
        w = randrange(0, 100)
        multiplier = randrange(0, 100)
        expected = w * multiplier
        results.append({'test': (str(multiplier), str(w)), 'expected': str(expected)})
    return results


if __name__ == '__main__':
    main()
