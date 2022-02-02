import functools
import random
import statistics

import hw3
from tests.test_framework import *
from random import randrange


def main():
    builder = TestBuilder("hw 3", 'hw3.py', linter_points=20, default_test_points=2)
    builder.add_to_blacklist({
        'if (?!__name__).*:': 'if statements not allowed for this assignment. please remove it to continue',
        'while.*:': 'while loops not allowed for this assignment. please remove it to continue',
        '\[*\]': 'lists are not allowed for this assignment. please remove it to continue',
        'list': 'lists are not allowed for this assignment. please remove it to continue'
    })
    builder.add_items(
        build_IO_section('average', [('1', '10')], ["10.0"], build_average_tests(9), hw3.average))
    builder.add_items(
        build_IO_section('tip_jar', [("1", "2.25", "3.50", "4.75", "5.25")], ["16.75"], build_tip_jar_tests(9),
                         hw3.tip_jar))
    builder.add_items(
        build_IO_section('newton', [("4", "2")], ["2.05"], build_newton_tests(9), hw3.newton))
    builder.add_items(
        build_IO_section('sequence', [["5"]], [["1", "1", "3", "3", "5"]], build_sequence_tests(9), hw3.sequence,
                         test_all_output=True))
    builder.add_items(
        build_IO_section('pi', [("3")], ["3.5555555555555554"], build_pi_tests(9), hw3.pi))
    builder.run()


def build_pi_tests(n):
    res = []
    for i in range(n):
        terms = randrange(0, 1000)
        n, nums = 2, [2]
        d, dens = 1, [1]
        for i in range(terms - 1):
            if i % 2 == 1:
                n += 2
            else:
                d += 2
            nums.append(n)
            dens.append(d)
        acc = 1
        for i, num in enumerate(nums):
            acc *= num / dens[i]
        res.append({'test': [str(terms)], 'expected': str(acc * 2)})
    return res


def build_average_tests(n):
    res = []
    for i in range(n):
        num = randrange(1, 20)
        ges = [randrange(1, 100) for _ in range(num)]
        res.append({'test': [str(x) for x in [num] + ges], 'expected': str(float(statistics.mean(ges)))})
    return res


def build_tip_jar_tests(n):
    res = []
    for i in range(n):
        tips = [round(random.uniform(0.01, 100), 2) for _ in range(5)]
        res.append({"test": [str(x) for x in tips], "expected": str(sum(tips))})
    return res


def build_newton_tests(n):
    res = []
    for i in range(n):
        x = randrange(1, 100)
        l = randrange(0, 5)
        a = functools.reduce(lambda acc, n: (acc + x / acc) / 2, range(l), x)
        res.append({'test': (str(x), str(l)), 'expected': str(a)})
    return res


def build_sequence_tests(n):
    res = []
    for i in range(n):
        terms = randrange(0, 20)
        all = list(range(1, terms + 1)) * 2
        all.sort()
        vals = [x for x in all if x % 2 != 0][:terms]
        res.append({'test': [str(terms)], 'expected': [str(x) for x in vals]})
    return res


if __name__ == '__main__':
    main()
