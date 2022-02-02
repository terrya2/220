import math
from random import randrange

import hw4
from tests.test_framework import *


def main():
    builder = TestBuilder("hw 4", 'hw4.py', linter_points=5, default_test_points=4)
    builder.add_to_blacklist({
        'if (?!__name__).*:': 'if statements not allowed for this assignment. please remove it to continue',
        'while.*:': 'while loops not allowed for this assignment. please remove it to continue',
        '\[*\]': 'lists are not allowed for this assignment. please remove it to continue',
        'list': 'lists are not allowed for this assignment. please remove it to continue'
    })
    pi_tests_section = build_IO_section('pi2', [('1')], [["4.0", "0.8584073464102069"]], build_pi_tests(9), hw4.pi2,
                                        test_all_output=True)

    def comp_func(actual, expected):
        return abs(float(actual[0]) - float(expected[0])) < 0.0000000000001 and abs(
            float(actual[1]) - float(expected[1])) < 0.0000000000001

    test: Test
    for test in pi_tests_section.outline:
        test.comp_func = comp_func
    builder.add_items(pi_tests_section)
    builder.run()


def build_pi_tests(n):
    res = []
    for i in range(n):
        positive = 1
        negative = -3
        sum = 0
        terms = randrange(1, 1000)
        for i in range(terms):
            if i % 2 == 0:
                sum += 4 / positive
                positive += 4
            else:
                sum += 4 / negative
                negative -= 4
        res.append({'test': [str(terms)], 'expected': [str(sum), str(abs(sum - math.pi))]})
    return res


if __name__ == '__main__':
    main()
