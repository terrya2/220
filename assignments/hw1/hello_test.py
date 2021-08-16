import pytest

from hw1 import hello
from tests import code_style

total = 0
global_points = 80
code_style_points = 10


class TestClass:

    # static tests
    def test_input(self, capfd):
        test_type = 'static tests'
        global total
        global global_points
        failed = 0
        hello.main()
        captured = capfd.readouterr()
        actual = captured.out.strip()

        print(f'\n\n============================== {test_type} start ===============================\n')
        expected = "hello, world!"
        test_result = actual == expected
        if not test_result:
            print(f'FAILED -{str(global_points)}')
            print(f'\texpected {expected} but got {actual}')
            failed += 1
        else:
            print(f'PASSED +{str(global_points)}')
            total = total + global_points
        print(f'\n\n============================== {test_type} end ===============================\n')

    # linting tests
    def test_linting(self):
        global code_style_points
        global total
        points = code_style.code_style('hello.py', code_style_points)
        total += points
        if not points == code_style_points:
            pytest.xfail(reason="Failed Code Style")

    @pytest.fixture(scope='session', autouse=True)
    def summary(self):
        global total
        # Will be executed before the first test
        yield
        # Will be executed after the last test
        print(f'\nTotal: {total} / 90')
