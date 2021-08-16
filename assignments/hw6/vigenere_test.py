import json

import pytest

from hw6 import vigenere
from tests import api_service
from tests import code_style

total = 0
global_points = 5
code_style_points = 10


class TestClass:

    # static tests
    def test_output(self):
        inputs = [
            (('this program will be great', 'python'), 'IFBZDEDEKHAJXJEISTGCTA'),
            (('the time has come the walrus said', 'oyster'), 'HFWMMDSFSLGFACLAINOJJNWJOGV'),
            (('float like a butterfly', 'champ'), 'HSOMINPKQPDBTFTTMLK')
        ]
        self.run_test(inputs, 'static tests')

    # dynamic tests
    def test_api(self):
        response = api_service.test('hw5', 'GET', params={'number': 13})
        answers = json.loads(response.text)
        a = 1
        test_data = self.convert_test_data(answers)
        self.run_test(test_data, 'api tests')

    # linting tests
    def test_linting(self):
        global code_style_points
        global total
        points = code_style.code_style('mean.py', code_style_points, rcfile='../../tests/hw5/.pylintrc')
        total += points
        if not points == code_style_points:
            pytest.xfail(reason="Failed Code Style")

    @staticmethod
    def run_test(data, test_type):
        global total
        global global_points
        failed = 0
        print(f'\n\n============================== {test_type} start ===============================\n')
        for inp in data:
            message = inp[0][0]
            key = inp[0][1]
            expected = inp[1]
            actual = vigenere.code(message, key)
            if actual == expected:
                print(f'PASSED +{global_points}')
                print(f'\tmessage: "{message}" | key: "{key}" | cipher text: "{expected}"')
                total += global_points
            else:
                print(f'FAILED | -{global_points}')
                print(f'\tmessage: {message}, key: {key}')
                print(f'\texpected {expected} but got {actual}')
                failed += 1
        noun = 'tests'
        if failed == 1:
            noun = 'test'
        print(f'\n============================== {failed} {noun} failed ===============================\n')

    @staticmethod
    def convert_test_data(data):
        inputs = []
        for test in data:
            inputs.append(((test['message'], test['key']), test['cipherText']))
        return inputs

    @pytest.fixture(scope='session', autouse=True)
    def summary(self):
        global total
        global code_style_points
        # Will be executed before the first test
        yield
        # Will be executed after the last test
        print(f'\nTotal: {total} / 90')
