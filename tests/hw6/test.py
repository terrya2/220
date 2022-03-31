import math

import hw6
from tests.test_framework import *


def main():
    builder = TestBuilder("hw 6", 'hw6.py', linter_points=20, default_test_points=2)
    builder.add_to_blacklist({
        'if (?!__name__).*:': 'if statements not allowed for this assignment. please remove it to continue',
        'while.*:': 'while loops not allowed for this assignment. please remove it to continue'
    })
    builder.add_items(
        build_IO_section('cash_converter', [["7"]], ["7.00"], build_cash_converter_tests(9), hw6.cash_converter))
    builder.add_items(
        build_IO_string_section('encode', [["The time has come, the Walrus said", "7"]],
                                ["[ol'{ptl'ohz'jvtl3'{ol'^hsy|z'zhpk"], build_encode_tests(9), hw6.encode, 2))
    builder.add_items(build_sphere_area_tests(10))
    builder.add_items(build_sphere_volume_tests(10))
    builder.add_items(build_sum_n_tests(10))
    builder.add_items(build_sum_n_cubes_tests(10))
    builder.add_items(
        build_IO_string_section('encode_better', [["dolphin", "ace"]],
                                ["JWVVPST"], build_encode_better_tests(9), hw6.encode_better, 2))
    builder.run()


def build_cash_converter_tests(n):
    tests = []
    for i in range(n):
        whole = random.randint(0, 100)
        decimal = random.randint(0, 9)
        expected = f'{whole}.{decimal}0'
        test_input = f'{whole}.{decimal}' if decimal > 0 else str(whole)
        tests.append({'test': [test_input], 'expected': expected})
    return tests


def build_encode_tests(n, shift=None):
    random_shift = False
    if not shift:
        random_shift = True
    tests = []
    for i in range(n):
        words_in_sentence = random.randint(1, 7)
        s = make_random_sentence(words_in_sentence)
        sentence = ''
        for letter in s:
            sentence += chr(ord(letter) - 32)
        if random_shift:
            shift = random.randint(0, 100)
        expected = ''.join([chr(ord(l) + shift) for l in sentence])
        tests.append({'test': [sentence, str(shift)], 'expected': expected})
    return tests


def build_sphere_area_tests(n):
    test_name = 'sphere_area'
    tests = []

    def comp_func(actual, expected):
        return abs(actual - expected) < 0.0000000001

    def test_sphere_area(r):
        return hw6.sphere_area(r)

    radii = [random.randint(0, 100) for i in range(n)]
    radius = gen(radii)

    res = [4 * math.pi * r ** 2 for r in radii]
    results = gen(res)

    for i in range(n):
        tests.append(Test(f'{test_name} {i + 1}', lambda: test_sphere_area(next(radius)), next(results),
                          data=[f'radius: {next(radius)}'], comp_func=comp_func))
    section = Section(test_name)
    section.add_items(*tests)
    return section


def build_sphere_volume_tests(n):
    test_name = 'sphere_volume'
    tests = []

    def comp_func(actual, expected):
        return abs(actual - expected) < 0.000000001

    def test_sphere_volume(r):
        return hw6.sphere_volume(r)

    radii = [random.randint(0, 100) for i in range(n)]
    radius = gen(radii)

    res = [4 / 3 * math.pi * r ** 3 for r in radii]
    results = gen(res)

    for i in range(n):
        tests.append(Test(f'{test_name} {i + 1}', lambda: test_sphere_volume(next(radius)), next(results),
                          data=[f'radius: {next(radius)}'], comp_func=comp_func))
    section = Section(test_name)
    section.add_items(*tests)
    return section


def build_sum_n_tests(n):
    test_name = 'sum_n'
    tests = []

    def test_sum(num):
        return hw6.sum_n(num)

    numbers = [random.randint(0, 100) for i in range(n)]
    number = gen(numbers)

    res = [sum(list(range(1, num + 1))) for num in numbers]
    result = gen(res)

    for i in range(n):
        tests.append(Test(f'{test_name} {i + 1}', lambda: test_sum(next(number)), next(result),
                          data=[f'n: {next(number)}']))
    section = Section(test_name)
    section.add_items(*tests)
    return section


def build_sum_n_cubes_tests(n):
    test_name = 'sum_n_cubes'
    tests = []

    def test_sum(num):
        return hw6.sum_n_cubes(num)

    numbers = [random.randint(0, 100) for i in range(n)]
    number = gen(numbers)

    res = [sum([x ** 3 for x in range(1, num + 1)]) for num in numbers]
    result = gen(res)

    for i in range(n):
        tests.append(Test(f'{test_name} {i + 1}', lambda: test_sum(next(number)), next(result),
                          data=[f'n: {next(number)}']))
    section = Section(test_name)
    section.add_items(*tests)
    return section


def build_encode_better_tests(n, sentence=None, key=None):
    use_random_key = False
    use_random_sentence = False
    if not key:
        use_random_key = True
    if not sentence:
        use_random_sentence = True
    tests = []
    for i in range(n):
        words_in_sentence = random.randint(1, 7)
        if use_random_sentence:
            sentence = make_random_sentence(words_in_sentence)
        sentence_nums = [ord(l) - ord('A') for l in sentence]
        if use_random_key:
            key = get_random_string()
        test_key = key * len(sentence)
        key_nums = [ord(k) - ord('A') for k in test_key]
        new_numbers = [l + key_nums[i] for i, l in enumerate(sentence_nums)]
        new_letters = [x % (ord('z') - ord('A') + 1) for x in new_numbers]
        expected = ''.join([chr(x + ord('A')) for x in new_letters])
        tests.append({'test': [sentence, key], 'expected': expected})
    return tests


if __name__ == '__main__':
    main()
