import json

import pytest

from hw2 import interest
from tests import api_service
from tests import code_style

total = 0
global_points = 5
code_style_points = 20


class TestClass:
    # static tests
    def test_input(self, monkeypatch, capfd):
        inputs = [
            (['15.84', '31', '850', '400', '20'], '9.35'),
            (['7.07', '30', '700', '100', '1'], '3.55'),
            (['0', '29', '0', '100', '29'], '0.0'),
            (['99', '31', '1234', '1234', '31'], '101.81')
        ]
        self.run_test(inputs, 'static tests', monkeypatch, capfd)

    # dynamic tests
    def test_api(self, monkeypatch, capfd):
        response = api_service.test('hw1', 'GET', params={'number': 10})
        data = json.loads(response.text)
        input = data['data']
        answers = data['answers']
        test_data = self.convert_test_data(input, answers)
        self.run_test(test_data, 'api tests', monkeypatch, capfd)

    # linting tests
    def test_linting(self):
        global code_style_points
        global total
        points = code_style.code_style('interest.py', code_style_points)
        total += points
        if not points == code_style_points:
            pytest.xfail(reason="Failed Code Style")

    @staticmethod
    def run_test(data, test_type, monkeypatch, capfd):
        global total
        global global_points
        failed = 0
        outputs = []
        for inp in data:
            userIn = inp[0]
            i = iter(userIn)
            monkeypatch.setattr('builtins.input', lambda inputMessage: next(i))
            interest.main()
            captured = capfd.readouterr()
            outputs.append(captured.out.strip())

        print(f'\n\n============================== {test_type} start ===============================\n')
        for index, actual in enumerate(outputs):
            expected = data[index][1]
            test_result = actual == expected
            if not test_result:
                print(f'FAILED -{str(global_points)}')
                print(f'\texpected {expected} but got {actual}')
                used_data = {'rate': float(data[index][0][0]),
                             'days': float(data[index][0][1]),
                             'previous_balance': float(data[index][0][2]),
                             'payment': float(data[index][0][3]),
                             'payment_day': float(data[index][0][4])
                             }
                print(f'\tdata: {used_data}')
                failed += 1
            else:
                print(f'PASSED +{str(global_points)}')
                total = total + global_points
        noun = 'tests'
        if failed == 1:
            noun = 'test'
        print(f'\n============================== {failed} {noun} failed ===============================\n')

    @staticmethod
    def convert_test_data(data, response):
        inputs = []
        for index, values in enumerate(data):
            input = list(map(str, [values['rate'], values['days'], values['previousBalance'], values['payment'],
                                   values['paymentDay']]))
            inputs.append((input, str(response[index])))
        return inputs

    @staticmethod
    def getOutput(attempt, monkeypatch, capfd):
        a = iter(
            [attempt['rate'], attempt['days'], attempt['previousBalance'], attempt['payment'], attempt['paymentDay']])
        monkeypatch.setattr('builtins.input', lambda inputMessage: next(a))
        interest.main()
        captured = capfd.readouterr()
        return float(captured.out.strip())

    @pytest.fixture(scope='session', autouse=True)
    def summary(self):
        global total
        global code_style_points
        # Will be executed before the first test
        yield
        # Will be executed after the last test
        print(f'\nTotal: {total} / 90')
