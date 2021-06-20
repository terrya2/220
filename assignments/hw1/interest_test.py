import json
import pytest
import random
import requests
from tests import code_style
from hw1 import interest
from tests import api_service

total = 0
global_points = 5
code_style_points = 20


class TestClass:

    def test_input(self, monkeypatch, capfd):
        global total
        global global_points
        failed = 0
        inputs = [
            (['15.84', '31', '850', '400', '20'], '9.35'),
            (['7.07', '30', '700', '100', '1'], '3.55'),
            (['0', '29', '0', '100', '29'], '0.0'),
            (['99', '31', '1234', '1234', '31'], '101.81')
        ]
        outputs = []
        for inp in inputs:
            userIn = inp[0]
            i = iter(userIn)
            monkeypatch.setattr('builtins.input', lambda inputMessage: next(i))
            interest.main()
            captured = capfd.readouterr()
            outputs.append(captured.out.strip())

        print('\n\n============================== static tests start ===============================\n')
        for index, actual in enumerate(outputs):
            expected = inputs[index][1]
            test_result = actual == expected
            if not test_result:
                print(f'FAILED -{str(global_points)}')
                print(f'\texpected {expected} but got {actual}')
                data = inputs[index][0]
                a = {'rate': float(data[0]),
                     'days': float(data[1]),
                     'previous_balance': float(data[2]),
                     'payment': float(data[3]),
                     'payment_day': float(data[4])
                     }
                print(f'\tdata: {a}')
                failed += 1
            else:
                print(f'PASSED +{str(global_points)}')
                total = total + global_points
        noun = 'tests'
        if failed == 1:
            noun = 'test'
        print(f'\n============================== {failed} {noun} failed ===============================\n')

    def test_api(self, monkeypatch, capfd):
        global total
        global global_points
        failed = 0
        data = self.makeTestData(10)
        response = api_service.test(data, 'hw1')
        expected_answer_list = json.loads(response.text)
        actual_answer_list = []
        for attempt in data:
            actual_answer_list.append(self.getOutput(attempt, monkeypatch, capfd))
            # actual_answer_list.append(1)
        print('\n\n============================== random tests start ===============================\n')
        for index, attempt in enumerate(data):
            test_result = actual_answer_list[index] == expected_answer_list[index]
            if not test_result:
                print(f'FAILED -{str(global_points)}')
                print(f'\texpected {str(expected_answer_list[index])} but got {str(actual_answer_list[index])}')
                print(f'\tdata: {attempt}')
                failed += 1
            else:
                print(f'PASSED +{str(global_points)}')
                total = total + global_points
        noun = 'tests'
        if failed == 1:
            noun = 'test'
        print(f'\n============================== {failed} {noun} failed ===============================\n')

    @staticmethod
    def getOutput(attempt, monkeypatch, capfd):
        a = iter(
            [attempt['rate'], attempt['days'], attempt['previousBalance'], attempt['payment'], attempt['paymentDay']])
        monkeypatch.setattr('builtins.input', lambda inputMessage: next(a))
        interest.main()
        captured = capfd.readouterr()
        return float(captured.out.strip())

    @staticmethod
    def makeTestData(num):
        output = []
        for i in range(num):
            rate = random.randint(0, 100)
            days = random.randint(1, 31)
            previous_balance = random.randint(500, 1000)
            payment = random.randint(0, 500)
            payment_day = random.randint(0, 31)
            output.append({'rate': rate, 'days': days, 'previousBalance': previous_balance, 'payment': payment,
                           'paymentDay': payment_day})
        return output

    def test_linting(self):
        global code_style_points
        points = code_style.code_style('interest.py', code_style_points)
        if not points == code_style_points:
            code_style_points = points
            pytest.xfail(reason="Failed Code Style")

    @pytest.fixture(scope='session', autouse=True)
    def summary(self):
        global total
        global code_style_points
        # Will be executed before the first test
        yield
        # Will be executed after the last test
        print(f'\nTotal: {total + code_style_points} / 90')
