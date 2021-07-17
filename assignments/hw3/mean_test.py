import json
import pytest
import random
import requests
from tests import code_style
from hw3 import mean
from tests import api_service

total = 0
global_points = 6
sub_points = 2
code_style_points = 12


class TestClass:

    def test_output(self, monkeypatch, capfd):
        inputs = [
            (['4', '10', '5', '2', '5'], {'rms_average': 6.205, 'harmonic_mean': 4.0, 'geometric_mean': 4.729}),
            (['1', '1'], {'rms_average': 1.0, 'harmonic_mean': 1.0, 'geometric_mean': 1.0}),
            (['10', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
             {'rms_average': 6.205, 'harmonic_mean': 3.414, 'geometric_mean': 4.529}),
            (['5', '5', '5', '5', '5', '5'], {'rms_average': 5.0, 'harmonic_mean': 5.0, 'geometric_mean': 5.0})
        ]
        self.run_test(inputs, 'static tests', monkeypatch, capfd)

    def test_api(self, monkeypatch, capfd):
        response = api_service.test('hw2', 'GET', params={'number': 9})
        data = json.loads(response.text)
        input = data['data']
        answers = data['answers']
        test_data = self.convert_test_data(input, answers)
        self.run_test(test_data, 'api tests', monkeypatch, capfd)

    @staticmethod
    def run_test(data, test_type, monkeypatch, capfd):
        global total
        global global_points
        global sub_points
        failed = 0

        outputs = []
        for inp in data:
            userIn = inp[0]
            i = iter(userIn)
            monkeypatch.setattr('builtins.input', lambda inputMessage: next(i))
            mean.main()
            captured = capfd.readouterr()
            output = captured.out.strip().split('\n')
            outputs.append({'rms_average': float(output[0]), 'harmonic_mean': float(output[1]),
                            'geometric_mean': float(output[2])})

        print(f'\n\n============================== {test_type} start ===============================\n')
        for index, actual in enumerate(outputs):
            expected = data[index][1]
            test_results = {'rms_average': actual['rms_average'] == expected['rms_average'],
                            'harmonic_mean': actual['harmonic_mean'] == expected['harmonic_mean'],
                            'geometric_mean': actual['geometric_mean'] == expected['geometric_mean']
                            }
            num_failed = 0
            for i in test_results:
                if not test_results[i]:
                    num_failed += 1

            if num_failed > 0:
                points_off = sub_points * num_failed
                print(f'{num_failed} FAILED -{str(points_off)}')
                print(f'\tdata: {data[index][0]}')
                for index in test_results:
                    if test_results[index]:
                        print(f'\t{index}: PASSED | +{sub_points}')
                    else:
                        print(f'\t{index}: FAILED | -{sub_points}')
                        print(f'\t\texpected {expected[index]} but got {actual[index]}')
                failed += 1
                total += global_points - points_off
            else:
                print(f'PASSED +{str(global_points)}')
                total += global_points
        noun = 'tests'
        if failed == 1:
            noun = 'test'
        print(f'\n============================== {failed} {noun} failed ===============================\n')

    @staticmethod
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

    def test_linting(self):
        global code_style_points
        global total
        points = code_style.code_style('mean.py', code_style_points)
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
