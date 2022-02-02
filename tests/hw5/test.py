import hw5
from tests.test_framework import *


def main():
    builder = TestBuilder("hw 5", 'hw5.py', linter_points=20, default_test_points=2)
    builder.add_to_blacklist({
        'if (?!__name__).*:': 'if statements not allowed for this assignment. please remove it to continue',
        'while.*:': 'while loops not allowed for this assignment. please remove it to continue'
    })
    builder.add_items(build_name_reverse_tests(10))
    builder.add_items(build_company_name_tests(10))
    builder.add_items(build_initials_tests(10))
    builder.add_items(build_names_tests(10))
    builder.add_items(build_thirds_tests(10))
    builder.add_items(
        build_IO_section('word_average', [['the quick brown fox jumps over the lazy dog']], ["3.888888888888889"],
                         build_word_average_tests(9), hw5.word_average, error_range=0.000001))
    builder.add_items(build_pig_latin_tests(10))
    builder.run()


def build_name_reverse_tests(n):
    test_name = 'name_reverse'
    tests = []
    for i in range(n):
        first_name = get_random_string()
        last_name = get_random_string()
        output, return_value, error = get_IO(hw5.name_reverse, [f"{first_name} {last_name}"])
        if error:
            tests.append(Test(f'{test_name} {i + 1}', True, False, data=[f"{first_name} {last_name}"],
                              show_actual_expected=False, exception_message=f'error: {error}'))
        elif len(output) == 0:
            tests.append(
                Test(f'{test_name} {i + 1}', True, False, exception_message='No output', show_actual_expected=False))
        else:
            actual = output[-1]
            expected = f'{last_name}, {first_name}'
            tests.append(Test(f'{test_name} {i + 1}', actual, expected, data=[f"{first_name} {last_name}"]))
    section = Section(test_name)
    section.add_items(*tests)
    return section


def build_company_name_tests(n):
    test_name = 'company_name'
    tests = []
    for i in range(n):
        url = get_random_string()
        input_data = f"www.{url}.com"
        output, return_value, error = get_IO(hw5.company_name, [input_data])
        if error:
            tests.append(Test(f'{test_name} {i + 1}', True, False, data=[input_data], show_actual_expected=False,
                              exception_message=f'error: {error}'))
        elif len(output) == 0:
            tests.append(
                Test(f'{test_name} {i + 1}', True, False, exception_message='No output', show_actual_expected=False))
        else:
            actual = output[-1]
            expected = url
            tests.append(Test(f'{test_name} {i + 1}', actual, expected, data=[input_data]))
    section = Section(test_name)
    section.add_items(*tests)
    return section


def build_initials_tests(n):
    test_name = 'initials'
    tests = []
    for i in range(n):
        number_of_students = random.randint(1, 4)
        input_data = [str(number_of_students)]
        names = []
        for _ in range(number_of_students):
            first_name = get_random_string()
            last_name = get_random_string()
            names.append((first_name, last_name, f'{first_name[0]}{last_name[0]}'))
            input_data.append(f'{first_name} {last_name}')
        output, return_value, error = get_IO(hw5.initials, input_data)
        if error:
            tests.append(Test(f'{test_name} {i + 1}', True, False, data=[input_data], show_actual_expected=False,
                              exception_message=f'error: {error}'))
        elif len(output) == 0:
            tests.append(
                Test(f'{test_name} {i + 1}', True, False, exception_message='No output', show_actual_expected=False))
        else:
            actual = []
            for j, out in enumerate(output[2:]):
                if j % 2 == 0:
                    actual.append(out)
            all_good = True
            for j, name in enumerate(names):
                expected = name[2]
                try:
                    act = actual[j]
                    if act != expected:
                        tests.append(Test(f'{test_name} {i + 1}', act, expected,
                                          data=[f'first name: {name[0]}, last name: {name[1]}']))
                        all_good = False
                        break
                except:
                    tests.append(Test(f'{test_name} {i + 1}', True, False, show_actual_expected=False,
                                      exception_message=f'error: this is likely due to an input/output issue. check that you have the correct number of inputs and outputs.'))
                    all_good = False
                    break
            if all_good:
                tests.append(Test(f'{test_name} {i + 1}', True, True))
    section = Section(test_name)
    section.add_items(*tests)
    return section


def build_names_tests(n):
    test_name = 'names'
    tests = []
    for i in range(n):
        number_of_names = random.randint(1, 10)
        names = []
        initials = []
        initials_regex = ''
        for _ in range(number_of_names):
            first_name = get_random_string()
            last_name = get_random_string()
            names.append(f'{first_name} {last_name}')
            initials.append(f'{first_name[0]}{last_name[0]}')
            initials_regex += f'{first_name[0]}{last_name[0]}.*'

        input_data = ", ".join(names)
        output, return_value, error = get_IO(hw5.names, [input_data])
        if error:
            tests.append(Test(f'{test_name} {i + 1}', True, False, data=[input_data], show_actual_expected=False,
                              exception_message=f'error: {error}'))
        elif len(output) == 0:
            tests.append(
                Test(f'{test_name} {i + 1}', True, False, exception_message='No output', show_actual_expected=False))
        else:
            output = output[1:]
            full_output = ''.join(output)
            res = re.search(initials_regex, full_output)
            if res:
                tests.append(Test(f'{test_name} {i + 1}', True, True))
            else:
                tests.append(Test(f'{test_name} {i + 1}', full_output, ' '.join(initials), data=[input_data]))
    section = Section(test_name)
    section.add_items(*tests)
    return section


def build_thirds_tests(n):
    test_name = 'thirds'
    tests = []
    for i in range(n):
        number_of_sentences = random.randint(1, 4)
        input_data = [str(number_of_sentences)]
        expected_output_data = []
        for _ in range(number_of_sentences):
            sentence = make_random_sentence(random.randint(1, 7))
            input_data.append(sentence)
            expected_output_data.append(sentence[::3])
        output, return_value, error = get_IO(hw5.thirds, input_data)
        if error:
            tests.append(Test(f'{test_name} {i + 1}', True, False, data=[f'sentences: {expected_output_data}'],
                              show_actual_expected=False,
                              exception_message=f'error: {error}'))
        elif len(output) == 0:
            tests.append(Test(test_name, True, False, exception_message='No output', show_actual_expected=False))
        else:
            full_output = ''.join(output[number_of_sentences + 1:])
            full_expected = ''.join(expected_output_data)
            tests.append(
                Test(f'{test_name} {i + 1}', full_output, full_expected, data=[f'sentences: {input_data[1:]}'],
                     exception_message=f'At least one output did not match. expected output for each sentence: {expected_output_data}',
                     show_actual_expected=False))

    section = Section(test_name)
    section.add_items(*tests)
    return section


def build_word_average_tests(n):
    tests = []
    for i in range(n):
        word_count = random.randint(1, 7)
        sentence = make_random_sentence(word_count)
        # complicated way of getting the letter counts
        total = 0
        for l in sentence:
            if l != ' ':
                total += 1
        expected = total / word_count
        tests.append({'test': [sentence], 'expected': str(expected)})
    return tests


def build_pig_latin_tests(n):
    test_name = 'pig_latin'
    tests = []
    for i in range(n):
        word_count = random.randint(1, 7)
        sentence_list = []
        pig_sentence_list = []
        for _ in range(word_count):
            word = get_random_string(0, 7)
            letter = get_random_letter()
            sentence_list.append(letter + word)
            pig_sentence_list.append(word + letter + 'ay')
        sentence = ' '.join(sentence_list)
        pig_sentence = ' '.join(pig_sentence_list)
        output, return_value, error = get_IO(hw5.pig_latin, [sentence])
        if error:
            tests.append(Test(f'{test_name} {i + 1}', True, False, data=[sentence], show_actual_expected=False,
                              exception_message=f'error: {error}'))
        elif len(output) == 0:
            tests.append(
                Test(f'{test_name} {i + 1}', True, False, exception_message='No output', show_actual_expected=False))
        else:
            full_output = output[-1]
            tests.append(Test(f'{test_name} {i + 1}', full_output, pig_sentence.lower(), data=[sentence]))

    section = Section(test_name)
    section.add_items(*tests)
    return section


if __name__ == '__main__':
    main()
