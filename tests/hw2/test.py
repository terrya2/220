import hw2
from tests.test_framework import *
from random import randrange


def main():
    builder = TestBuilder("hw 2", 'hw2.py', linter_points=20, default_test_points=2)
    builder.add_to_blacklist({
        'if (?!__name__).*:': 'if statements not allowed for this assignment. please remove it to continue',
        'while.*:': 'while loops not allowed for this assignment. please remove it to continue',
        '\[*\]': 'lists are not allowed for this assignment. please remove it to continue',
        'list': 'lists are not allowed for this assignment. please remove it to continue',
        'pow.*\(.*\d\)': 'cannot use pow function for this assignment!',
        '\*\*': 'cannot use exponent operator for this assignment!'
    })
    builder.add_items(
        build_section('sum_of_threes', [["15"]], ["45"], build_sum_of_threes_tests(9), hw2.sum_of_threes))
    builder.add_items(multiplication_table_test())
    builder.add_items(
        build_section('triangle_area', [("3", "4", "5")], ["6.0"], build_triangle_area_tests(9), hw2.triangle_area))
    builder.add_items(
        build_section('sum_squares', [("3", "5")], ["50"], build_sum_squares_tests(9), hw2.sum_squares))
    builder.add_items(build_power_section([("2", "3")], ["8"], hw2.power))
    builder.run()


def build_power_section(tests, expected, test_func):
    name = "power"
    section = Section(name)
    for test in build_power_tests(9):
        tests.append(test['test'])
        expected.append(test['expected'])
    results = []
    for test in tests:
        results.append(get_IO(test_func, test))
    actual_results = gen(results)
    for i, ex in enumerate(expected):
        output, res, error = next(actual_results)
        test_name = f'{name} {i + 1}'
        if str(error) == 'math domain error':
            test = Test(test_name, None, ex,
                        exception_message='cannot take square root of a negative. check your square root function',
                        data=[f'inputs: {tests[i]}'])
        elif error:
            test = Test(test_name, None, ex, exception_message=error, data=[f'inputs: {tests[i]}'])
        else:
            full_output = " ".join(output)
            output_numbers = get_all_numbers_in_string(full_output)
            try:
                test = Test(test_name, output_numbers[-1], ex, data=[f'inputs: {tests[i]}'])
            except:
                test = Test(test_name, f'error: incorrect output', ex, data=[f'inputs: {tests[i]}'])
        section.add_items(test)
    return section


def build_power_tests(n):
    res = []
    for i in range(n):
        base = randrange(1, 10)
        exponent = randrange(1, 10)
        answer = base ** exponent
        res.append({'test': (str(base), str(exponent)), 'expected': str(answer)})
    return res


def build_triangle_area_tests(n):
    res = []
    for i in range(n):
        side_a = randrange(2, 20)
        side_b = randrange(2, 20)
        big = max([side_a, side_b])
        side_c = randrange(abs(side_b - side_a) + 1, big)
        d = (side_a + side_b + side_c) / 2
        acc = d
        for i in [side_a, side_b, side_c]:
            acc *= d - i
        res.append({"test": [str(side_a), str(side_b), str(side_c)], "expected": str(acc ** (1 / 2))})
    return res


def multiplication_table_test():
    section = Section("multiplication_table")
    output, result, error = get_IO(hw2.multiplication_table)
    if error:
        for i in range(10):
            section.add_items(Test(f'multiplication_table line {i + 1}', show_actual_expected=False,
                                   exception_message=f"output errors: {error}"))
    else:
        multiplier = 1
        for i in range(10):
            expected_line = []
            for j in range(1, 11):
                expected_line.append(str(j * multiplier))
            expected_string = " ".join(expected_line)
            multiplier += 1
            try:
                line = output[i * 20:((i * 10) + 10) * 2:2]
                line_string = " ".join(line)
                section.add_items(Test(f'multiplication_table line {i + 1}', line_string, expected_string))
            except:
                section.add_items(Test(f'multiplication_table line {i + 1}', show_actual_expected=False,
                                       exception_message=f"unable to process line {i + 1}"))
    return section


def build_sum_squares_tests(n):
    res = []
    for i in range(n):
        lower = randrange(0, 10)
        upper = randrange(lower + 1, 20)
        r = range(lower, upper + 1)
        acc = sum([x * x for x in r])
        res.append({'test': (str(lower), str(upper)), 'expected': str(acc)})
    return res


def build_sum_of_threes_tests(n):
    res = []
    for i in range(n):
        s = 0
        c = 1
        upper_bound = randrange(1, 50)
        while c <= upper_bound:
            if c % 3 == 0:
                s += c
            c += 1
        res.append({'test': [str(upper_bound)], 'expected': str(s)})

    return res


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
        if str(error) == 'math domain error':
            test = Test(test_name, None, ex,
                        exception_message='cannot take square root of a negative. check your square root function',
                        data=[f'inputs: {tests[i]}'])
        elif error:
            test = Test(test_name, None, ex, exception_message=error, data=[f'inputs: {tests[i]}'])
        else:
            full_output = " ".join(output)
            output_numbers = get_all_numbers_in_string(full_output)
            try:
                test = Test(test_name, output_numbers[0], ex, data=[f'inputs: {tests[i]}'])
            except:
                test = Test(test_name, f'error: incorrect output', ex, data=[f'inputs: {tests[i]}'])
        section.add_items(test)
    return section


if __name__ == '__main__':
    main()
