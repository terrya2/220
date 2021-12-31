from hw3 import hw3
from tests.hw3 import random_tests
from tests.test_framework import *


def main():
    outline = TestBuilder('mean', 'hw3.py', 12, 2)
    outline.rc_file = '../../tests/hw3/.pylintrc'
    outline.add_to_blacklist({
        'importstatistics': 'statistics library not allowed - please write your program to calculate the averages and do not rely on outside libraries to do so for you.',
        'fromstatistics': 'statistics library not allowed - please write your program to calculate the averages and do not rely on outside libraries to do so for you.'
    })
    static_tests = static_test_builder()
    dynamic_tests = dynamic_test_builder()
    outline.add_items(static_tests, dynamic_tests)
    outline.run()


def static_test_builder():
    inputs = [
        (['4', '10', '5', '2', '5'], {'rms_average': 6.205, 'harmonic_mean': 4.0, 'geometric_mean': 4.729}),
        (['1', '1'], {'rms_average': 1.0, 'harmonic_mean': 1.0, 'geometric_mean': 1.0}),
        (['10', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
         {'rms_average': 6.205, 'harmonic_mean': 3.414, 'geometric_mean': 4.529}),
        (['5', '5', '5', '5', '5', '5'], {'rms_average': 5.0, 'harmonic_mean': 5.0, 'geometric_mean': 5.0})
    ]
    return run_test(inputs, 'static tests')


def dynamic_test_builder():
    data = random_tests.create(9)
    input = data['data']
    answers = data['answers']
    test_data = convert_test_data(input, answers)
    return run_test(test_data, 'dynamic tests')


def run_test(data, test_type):
    outputs = []
    for inp in data:
        userIn = inp[0]
        output, res, error = get_IO(hw3.main, userIn)
        output = output[-3:]  # get the last 3 outputs
        outputs.append({'rms_average': float(output[0]), 'harmonic_mean': float(output[1]),
                        'geometric_mean': float(output[2]), 'data': userIn})

    section = Section(test_type)
    for index, actual in enumerate(outputs):
        expected = data[index][1]
        test_results = [
            {'name': 'rms_average', 'actual': actual['rms_average'], 'expected': expected['rms_average']},
            {'name': 'harmonic_mean', 'actual': actual['harmonic_mean'],
             'expected': expected['harmonic_mean']},
            {'name': 'geometric_mean', 'actual': actual['geometric_mean'],
             'expected': expected['geometric_mean']},
        ]
        sub_section = Section(f'test {index + 1}', group_data=[" ".join(map(str, actual['data']))])
        for i in test_results:
            sub_section.add_items(Test(i['name'], i['actual'], i['expected']))
        section.add_items(sub_section)
    return section


def convert_test_data(data, response):
    inputs = []
    for index, test in enumerate(response):
        input_values = list(map(str, data[index]))
        input_values.insert(0, str(len(data[index])))
        output_values = {
            'rms_average': test['rmsAvg'],
            'harmonic_mean': test['harmonicMean'],
            'geometric_mean': test['geometricMean']
        }
        inputs.append((input_values, output_values))
    return inputs


if __name__ == '__main__':
    main()
