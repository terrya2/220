import json

import pytest

from hw6.weighted_average import weighted_average
from tests import api_service
from tests import code_style

total = 0
global_points = 5
sub_points = 1
code_style_points = 15


class TestClass:

    def test_output(self):
        file_prefix = 'static_test'
        inputs = [
            [
                "Billy Bother's average: 87.0",
                "Oh No's average: Error: The weights are less than 100.",
                "Hermione Heffalump's average: 95.4",
                "Too Bad's average: Error: The weights are more than 100.",
                "Kurt Kidd's average: 82.5",
                "Class average: 88.3"
            ],
            [
                "James Hook's average: 97.0",
                "Class average: 97.0"
            ],
            [
                "Doll R. Bill's average: 80.0",
                "Frank N. Stein's average: 50.0",
                "Howe D. Pardner's average: 30.3",
                "Mary Thonn's average: Error: The weights are more than 100.",
                "Nadia Seymour's average: 100.0",
                "Phil Down's average: 0.0",
                "Class average: 52.1"
            ]

        ]
        self.run_test(inputs, file_prefix, 'static tests')

    def test_api(self):
        file_prefix = 'api_test'
        response = api_service.test('hw6', 'GET', params={'number': 12})
        answers = json.loads(response.text)
        expected_values = []
        for i, test in enumerate(answers):
            with open(f'../../tests/hw6/{file_prefix}{i}', 'w') as f:
                f.writelines('\n'.join(test['testData']))
            expected_values.append(test['expectedValues'])
        self.run_test(expected_values, file_prefix, 'api tests')

    @staticmethod
    def run_test(data, file_prefix, test_type):
        global total
        global global_points
        global sub_points
        number_failed = 0

        print(f'\n\n============================== {test_type} start ===============================\n')
        for test_number, test in enumerate(data):
            failed = 0
            weighted_average(f'../../tests/hw6/{file_prefix}{test_number}',
                             f'../../tests/hw6/{file_prefix}_output{test_number}')
            expected_lines = test
            actual_lines = []
            with open(f'../../tests/hw6/{file_prefix}_output{test_number}') as f:
                for index, line in enumerate(f):
                    actual_line = line.strip()
                    actual_lines.append(actual_line)
                    if not actual_line == expected_lines[index]:
                        failed += 1
            points_off = failed * sub_points
            number_failed += failed
            test_points = global_points - points_off if points_off < global_points else 0
            total += test_points
            print(f'Test {test_number} | +{test_points}')
            for index, actual_line in enumerate(actual_lines):
                if actual_line == expected_lines[index]:
                    print(f'\tPASSED +{sub_points}')
                else:
                    print(f'\tFAILED -{sub_points}')
                    print(f'\t\tactual: {actual_line}')
                    print(f'\t\texpected: {expected_lines[index]}')

        noun = 'test' if number_failed == 1 else 'test'
        print(f'\n============================== {failed} {noun} failed ===============================\n')

    def test_linting(self):
        global code_style_points
        global total
        points = code_style.code_style('mean.py', code_style_points, rcfile='../../tests/hw5/.pylintrc')
        total += points
        if not points == code_style_points:
            pytest.xfail(reason="Failed Code Style")

    @pytest.fixture(scope='session', autouse=True)
    def summary(self):
        global total
        global code_style_points
        # Will be executed before the first test
        yield
        # Will be executed after the last test
        print(f'\nTotal: {total} / 90')
