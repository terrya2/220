import os
import shutil
from pathlib import *

import hw7
from assignments.hw7 import encryption
from tests.hw6.test import build_encode_tests, build_encode_better_tests
from tests.test_framework import *

TEST_DIR = Path(os.path.dirname(__file__))
HW_DIR = Path(os.path.dirname(hw7.__file__)) / 'tests'
if not os.path.isdir(HW_DIR):
    os.mkdir(Path(os.path.dirname(hw7.__file__)) / 'tests')


def main():
    builder = TestBuilder("hw 7", 'hw7.py', linter_points=20, default_test_points=2)
    builder.add_to_blacklist({
        'if (?!__name__).*:': 'if statements not allowed for this assignment. please remove it to continue',
        'while.*:': 'while loops not allowed for this assignment. please remove it to continue',
        'round.*\(': 'no rounding with the round() function in this assignment'
    })
    builder.add_items(build_number_words_tests(10))
    builder.add_items(build_hourly_wages_tests(10))
    builder.add_items(build_check_sum_tests(10))
    builder.add_items(build_send_message_tests(10))
    builder.add_items(build_send_safe_message_tests(10))
    builder.add_items(build_send_uncrackable_message_tests(10))
    builder.run()


def build_send_uncrackable_message_tests(num):
    test_name = 'send_uncrackable_message'
    tests = []
    file_names = [(f'{test_name}_{i}_input.txt', f'{test_name}_{i}_pad.txt', f'{test_name}_{i}_expected.txt') for i in
                  range(1, num + 1)]
    create_test_files(file_names, send_uncrackable_message_generator)

    for i in range(1, num + 1):
        expected = open(HW_DIR / f'{test_name}_{i}_expected.txt', 'r').read()
        output_file_name_arg = HW_DIR / f'{test_name}_{i}_actual'
        output_file_name = HW_DIR / f'{test_name}_{i}_actual.txt'
        outcome, result = run_safe(
            lambda: hw7.send_uncrackable_message(HW_DIR / f'{test_name}_{i}_input.txt', str(output_file_name_arg),
                                                 HW_DIR / f'{test_name}_{i}_pad.txt'))
        if not outcome:
            tests.append(
                Test(f'{test_name} {i}', 'error', expected, exception_message=result, show_actual_expected=False))
        elif not os.path.isfile(output_file_name):
            tests.append(Test(f'{test_name} {i}', 'error', expected, exception_message='output file does not exist.',
                              show_actual_expected=False))
        else:
            actual = open(output_file_name, 'r').read()
            tests.append(Test(f'{test_name} {i}', actual, expected, show_actual_expected=False))
    section = Section(test_name)
    section.add_items(*tests)
    # check if encode function is in encryption.py
    section.add_items(
        Test(f'{test_name} - encode_better in encryption.py', 'encode_better' in dir(encryption), True,
             show_actual_expected=False,
             points=2))

    return section


def send_uncrackable_message_generator():
    input_file = []
    pad_file = ''
    number_of_lines = random.randint(1, 5)
    for i in range(number_of_lines):
        number_of_words = random.randint(1, 5)
        line = []
        for j in range(number_of_words):
            line.append(get_random_string())
        input_file.append(' '.join(line))
    input_string = '\n'.join(input_file) + '\n'
    for _ in input_string:
        pad_file += get_random_letter()
    results = build_encode_better_tests(1, input_string, pad_file)  # [{test: [sentence, key], expected: expected}]
    output = results[0]['expected']
    return ('\n'.join(input_file), pad_file, output)


def build_send_safe_message_tests(num):
    test_name = 'send_safe_message'
    tests = []
    file_names = [(f'{test_name}_{i}_input.txt', f'{test_name}_{i}_expected.txt') for i in range(1, num + 1)]
    keys = [random.randint(0, 25) for _ in range(len(file_names))]
    i = 0
    attempts = 0
    while i < len(file_names):
        attempts += 1
        files = file_names[i]
        try:
            create_test_files([files], send_safe_message_generator(keys[i]))
            i += 1
        except Exception as e:
            if attempts > 10000:
                print('an error occurred, please try running the tests again')
                sys.exit()

    for i in range(1, num + 1):
        expected = open(HW_DIR / f'{test_name}_{i}_expected.txt', 'r').read()
        output_file_name_arg = HW_DIR / f'{test_name}_{i}_actual'
        output_file_name = HW_DIR / f'{test_name}_{i}_actual.txt'
        outcome, result = run_safe(
            lambda: hw7.send_safe_message(HW_DIR / f'{test_name}_{i}_input.txt', str(output_file_name_arg),
                                          keys[i - 1]))
        if not outcome:
            tests.append(
                Test(f'{test_name} {i}', 'error', expected, exception_message=result, show_actual_expected=False))
        elif not os.path.isfile(output_file_name):
            tests.append(Test(f'{test_name} {i}', 'error', expected, exception_message='output file does not exist.',
                              show_actual_expected=False))
        else:
            actual = open(output_file_name, 'r').read()
            tests.append(Test(f'{test_name} {i}', actual, expected, show_actual_expected=False))
    section = Section(test_name)
    section.add_items(*tests)
    # check if encode function is in encryption.py
    section.add_items(
        Test(f'{test_name} - encode in encryption.py', 'encode' in dir(encryption), True, show_actual_expected=False,
             points=2))

    return section


def build_send_message_tests(num):
    test_name = 'send_message'
    tests = []
    file_names = [(f'{test_name}_{i}_input.txt', f'{test_name}_{i}_expected.txt') for i in range(1, num + 1)]
    create_test_files(file_names, send_message_generator)

    for i in range(1, num + 1):
        expected = open(HW_DIR / f'{test_name}_{i}_expected.txt', 'r').read()
        output_file_name_arg = HW_DIR / f'{test_name}_{i}_actual'
        output_file_name = HW_DIR / f'{test_name}_{i}_actual.txt'
        outcome, result = run_safe(
            lambda: hw7.send_message(HW_DIR / f'{test_name}_{i}_input.txt', str(output_file_name_arg)))
        if not outcome:
            tests.append(
                Test(f'{test_name} {i}', 'error', expected, exception_message=result, show_actual_expected=False))
        elif not os.path.isfile(output_file_name):
            tests.append(Test(f'{test_name} {i}', 'error', expected, exception_message='output file does not exist.',
                              show_actual_expected=False))
        else:
            actual = open(output_file_name, 'r').read()
            tests.append(Test(f'{test_name} {i}', actual, expected, show_actual_expected=False))
    section = Section(test_name)
    section.add_items(*tests)
    return section


def build_check_sum_tests(num):
    test_name = 'calc_check_sum'
    tests = []
    inout = create_check_sum_io(num - 1)
    inout.insert(0, ('0-072-94652-0', 187))
    inputs = [x[0] for x in inout]
    input_gen = gen(inputs)
    for i, res in enumerate(inout):
        inp, expected = res
        tests.append(
            Test(f'{test_name} {i + 1}', lambda: hw7.calc_check_sum(next(input_gen)), expected))
    section = Section(test_name)
    section.add_items(*tests)
    return section


def create_check_sum_io(num):
    results = []
    for i in range(num):
        options = [False, False, False, True]
        isbn = []
        isbn_mult = []
        for multiplier in range(10, 2, -1):
            num = random.randint(0, 9)
            isbn.append(num)
            isbn_mult.append(num * multiplier)
        isbn_temp_sum = sum(isbn_mult)
        off_by = 11 - isbn_temp_sum % 11  # this is what we need to add to the isbn to make sure it can % 11 evenly
        if off_by >= 10:
            second = random.randint(1, 5)
        elif off_by == 1:
            second = 0
        else:
            second = random.randint(1, off_by // 2)
        isbn.append(second)
        isbn_mult.append(second * 2)
        off_by -= second * 2
        isbn.append(off_by)
        isbn_mult.append(off_by)
        i = 1
        while i < len(isbn):
            res = random.choice(options)
            if res:
                isbn.insert(i, '-')
                i += 1
            i += 1
        isbn = [str(x) for x in isbn]
        results.append((''.join(isbn), sum(isbn_mult)))

    return results


def build_hourly_wages_tests(num):
    test_name = 'hourly_wages'
    tests = []
    file_names = [(f'{test_name}_{i}_input.txt', f'{test_name}_{i}_expected.txt') for i in range(2, num + 1)]
    create_test_files(file_names, hourly_wages_generator)

    shutil.copy(TEST_DIR / f'{test_name}_1_expected.txt', HW_DIR / f'{test_name}_1_expected.txt')
    shutil.copy(TEST_DIR / f'{test_name}_1_input.txt', HW_DIR / f'{test_name}_1_input.txt')

    for i in range(1, num + 1):
        expected = open(HW_DIR / f'{test_name}_{i}_expected.txt', 'r').read()
        output_file_name = HW_DIR / f'{test_name}_{i}_actual.txt'
        outcome, result = run_safe(lambda: hw7.hourly_wages(HW_DIR / f'{test_name}_{i}_input.txt', output_file_name))
        if not outcome:
            tests.append(
                Test(f'{test_name} {i}', 'error', expected, exception_message=result, show_actual_expected=False))
        elif not os.path.isfile(output_file_name):
            tests.append(Test(f'{test_name} {i}', 'error', expected, exception_message='output file does not exist.',
                              show_actual_expected=False))
        else:
            actual = open(output_file_name, 'r').read()
            tests.append(Test(f'{test_name} {i}', actual, expected, show_actual_expected=False))
    section = Section(test_name)
    section.add_items(*tests)
    return section


def send_safe_message_generator(shift):
    def a():
        input_file = []
        output_file = []
        # returns [{'test': [sentence, shift], 'expected': expected}]
        number_of_lines = random.randint(1, 7)
        results = build_encode_tests(number_of_lines, shift)
        for res in results:
            sentence = res['test'][0]
            input_file.append(sentence)
            output_file.append(res['expected'])
        return ('\n'.join(input_file), '\n'.join(output_file))

    return a


def send_message_generator():
    input_file = []
    output_file = []
    number_of_lines = random.randint(1, 100)
    for i in range(number_of_lines):
        number_of_words = random.randint(1, 100)
        line = []
        for j in range(number_of_words):
            line.append(get_random_string())
        input_file.append(' '.join(line))
        output_file.append(' '.join(line))
    return ('\n'.join(input_file), '\n'.join(output_file))


def hourly_wages_generator():
    input_file = []
    output_file = []
    number_of_names = random.randint(1, 7)
    for i in range(number_of_names):
        name = get_random_string() + ' ' + get_random_string()
        wage = round(random.uniform(15, 50), 2)
        hours = random.randint(10, 50)
        total = round((wage + 1.65) * hours, 2)
        input_file.append(f'{name} {wage:.2f} {hours}')
        output_file.append(f'{name} {total:.2f}')
    return ('\n'.join(input_file), '\n'.join(output_file))


def number_words_generator():
    input_file = []
    output_file = []
    lines = random.randint(1, 7)
    count = 1
    for i in range(lines):
        word_count = random.randint(1, 5)
        sentence = make_random_sentence(word_count)
        words = sentence.split()
        for word in words:
            output_file.append(f'{count} {word}')
            count += 1
        input_file.append(sentence)
    return ('\n'.join(input_file), '\n'.join(output_file))


def build_number_words_tests(num):
    test_name = 'number_words'
    tests = []
    file_names = [(f'{test_name}_{i}_input.txt', f'{test_name}_{i}_expected.txt') for i in range(3, num + 1)]
    create_test_files(file_names, number_words_generator)

    shutil.copy(TEST_DIR / 'number_words_1_expected.txt', HW_DIR / 'number_words_1_expected.txt')
    shutil.copy(TEST_DIR / 'number_words_2_expected.txt', HW_DIR / 'number_words_2_expected.txt')
    shutil.copy(TEST_DIR / 'number_words_1_input.txt', HW_DIR / 'number_words_1_input.txt')
    shutil.copy(TEST_DIR / 'number_words_2_input.txt', HW_DIR / 'number_words_2_input.txt')

    for i in range(1, num + 1):
        expected = open(HW_DIR / f'{test_name}_{i}_expected.txt', 'r').read()
        output_file_name = HW_DIR / f'{test_name}_{i}_actual.txt'
        outcome, result = run_safe(lambda: hw7.number_words(HW_DIR / f'{test_name}_{i}_input.txt', output_file_name))
        if not outcome:
            tests.append(
                Test(f'{test_name} {i}', 'error', expected, exception_message=result, show_actual_expected=False))
        elif not os.path.isfile(output_file_name):
            tests.append(Test(f'{test_name} {i}', 'error', expected, exception_message='output file does not exist.',
                              show_actual_expected=False))
        else:
            actual = open(output_file_name, 'r').read()
            tests.append(Test(f'{test_name} {i}', actual, expected, show_actual_expected=False))
    section = Section(test_name)
    section.add_items(*tests)
    return section


def create_test_files(file_names, generator):
    '''
    file_names - list of tuples (in_file_name, out_file_name, ...)
    generator - function that returns a tuple
                    (contents of file one, contents file two, ...)
    '''
    for files in file_names:
        file_contents = generator()
        for i, file_name in enumerate(files):
            with open(HW_DIR / file_name, 'w') as file:
                print(file_contents[i], file=file)


def clean_up_files(file_names):
    for file_name in file_names:
        os.remove(file_name)
