import json
import time

import pytest
from graphics import GraphWin, Circle, Point

from hw8 import bumper
from tests import api_service
from tests import code_style
from tests.hw7.test_case import TestCase, Result, Results

total = 0
global_points = 5
sub_points = 1
code_style_points = 15
win = GraphWin("test", 600, 400)


class TestClass:

    # static tests
    def test_output(self):
        test_cases = TestCase()
        test_cases.did_collide_tests = [
            {'x1': 71, 'y1': 74, 'r1': 7, 'x2': 51, 'y2': 185, 'r2': 7, 'expected': False},
            {'x1': 36, 'y1': 54, 'r1': 29, 'x2': 10, 'y2': 47, 'r2': 29, 'expected': True},
            {'x1': 7, 'y1': 8, 'r1': 9, 'x2': 10, 'y2': 11, 'r2': 12, 'expected': True},
            {"x1": 87, "y1": 58, "r1": 20, "x2": 54, "y2": 100, "r2": 20, "expected": False},
            {"x1": 59, "y1": 97, "r1": 38, "x2": 75, "y2": 82, "r2": 38, "expected": True},
            {"x1": 97, "y1": 97, "r1": 42, "x2": 100, "y2": 1, "r2": 42, "expected": False}
        ]
        test_cases.get_random_tests = [10, 50, 100]
        test_cases.hit_vertical_tests = [
            {'x': 120, 'y': 116, 'radius': 35, 'expected': False},
            {'x': 19, 'y': 50, 'radius': 20, 'expected': True},
            {'x': 20, 'y': 50, 'radius': 20, 'expected': True},
            {'x': 21, 'y': 50, 'radius': 20, 'expected': False},
            {'x': 59, 'y': 50, 'radius': 40, 'expected': False},
            {'x': 560, 'y': 50, 'radius': 40, 'expected': True},
            {'x': 561, 'y': 50, 'radius': 40, 'expected': True}
        ]
        test_cases.hit_horizontal_tests = [
            {'x': 200, 'y': 40, 'radius': 10, 'expected': False},
            {'x': 50, 'y': 19, 'radius': 20, 'expected': True},
            {'x': 50, 'y': 20, 'radius': 20, 'expected': True},
            {'x': 50, 'y': 21, 'radius': 20, 'expected': False},
            {'x': 50, 'y': 59, 'radius': 40, 'expected': False},
            {'x': 50, 'y': 360, 'radius': 40, 'expected': True},
            {'x': 50, 'y': 361, 'radius': 40, 'expected': True}
        ]
        self.run_test(test_cases, 'static tests')

    # dynamic tests
    def test_api(self):
        response = api_service.test('hw7', 'GET',
                                    params={'number': 13, 'width': win.getWidth(), 'height': win.getHeight()})
        api_tests = json.loads(response.text)
        test_cases = TestCase()
        test_cases.hit_vertical_tests = api_tests['hitVerticalTests']
        test_cases.hit_horizontal_tests = api_tests['hitHorizontalTests']
        test_cases.get_random_tests = api_tests['getRandomTests']
        test_cases.did_collide_tests = api_tests['didCollideTests']

        self.run_test(test_cases, 'api tests')

    # linting tests
    def test_linting(self):
        global code_style_points
        global total
        points = code_style.code_style('bumper.py', code_style_points, rcfile='../../.pylintrc')
        total += points
        if not points == code_style_points:
            pytest.xfail(reason="Failed Code Style")

    @staticmethod
    def run_test(test_cases, test_type):
        global total
        global global_points
        global sub_points

        print(f'\n\n============================== {test_type} start ===============================\n')

        # DID COLLIDE TESTS
        collide_results = Results(points=None)
        for test in test_cases.did_collide_tests:
            result = Result(points=sub_points)
            result.expected = test['expected']
            c1 = Circle(Point(test['x1'], test['y1']), test['r1'])
            c2 = Circle(Point(test['x2'], test['y2']), test['r2'])
            result.data = (c1, c2)
            result.actual = bumper.did_collide(c1, c2)
            result.passed = result.expected == result.actual
            collide_results.add(result)

        print('Test did_collide Method:')
        if collide_results.number_failed == 0:
            print(f'\tPASSED {collide_results.number_passed} tests | +{collide_results.get_total_points()}')
        else:
            print(
                f'\tFAILED {collide_results.number_failed}/{len(test_cases.did_collide_tests)} tests | +{collide_results.get_total_points()}')
            for index, res in enumerate(collide_results.failed_tests):
                print(f'\t\ttest {index} | +{0}')
                print(f'\t\t\tdata: {res.data}')
                print(f'\t\t\tactual: {res.actual}')
                print(f'\t\t\texpected: {res.expected}')
        total += collide_results.get_total_points()

        # GET RANDOM TESTS
        get_random_results = Results(points=None)
        for test in test_cases.get_random_tests:
            result = Result(points=sub_points)
            result.data = test
            temp_actual = 0
            in_range = True
            fail_range_value = 0
            positive_in = False
            negative_in = False
            for i in range(700):
                temp_actual = bumper.get_random(test)
                if not (test * -1 <= temp_actual <= test):
                    in_range = False
                    fail_range_value = temp_actual
                if temp_actual == test:
                    positive_in = True
                if temp_actual == test * -1:
                    negative_in = True

            if not in_range:
                result.actual = fail_range_value
                result.expected = f'-{test} <= {result.actual} <= {test}'
                result.passed = False
            elif not positive_in:
                result.actual = temp_actual
                result.expected = f'value {test} never returned'
                result.passed = False
            elif not negative_in:
                result.actual = temp_actual
                result.expected = f'value -{test} never returned'
                result.passed = False
            else:
                result.actual = temp_actual
                result.expected = f'-{test} <= {result.actual} <= {test}'
                result.passed = True
            get_random_results.add(result)

        print('Test get_random Method:')
        if get_random_results.number_failed == 0:
            print(f'\tPASSED {get_random_results.number_passed} tests | +{get_random_results.get_total_points()}')
        else:
            print(
                f'\tFAILED {get_random_results.number_failed}/{len(test_cases.get_random_tests)} tests | +{get_random_results.get_total_points()}')
            for index, res in enumerate(get_random_results.failed_tests):
                print(f'\t\ttest {index} | +{0}')
                print(f'\t\t\tdata: {res.data}')
                print(f'\t\t\tactual: {res.actual}')
                print(f'\t\t\texpected: {res.expected}')
        total += get_random_results.get_total_points()

        # HIT VERTICAL TESTS
        vertical_results = Results(points=None)
        for test in test_cases.hit_vertical_tests:
            result = Result(points=sub_points)
            result.expected = test['expected']
            circle = Circle(Point(test['x'], test['y']), test['radius'])
            result.data = (circle, win)
            result.actual = bumper.hit_vertical(circle, win)
            result.passed = result.expected == result.actual
            vertical_results.add(result)

        print('Test hit_vertical Method:')
        if vertical_results.number_failed == 0:
            print(f'\tPASSED {vertical_results.number_passed} tests | +{vertical_results.get_total_points()}')
        else:
            print(
                f'\tFAILED {vertical_results.number_failed}/{len(test_cases.hit_vertical_tests)} tests | +{vertical_results.get_total_points()}')
            for index, res in enumerate(vertical_results.failed_tests):
                print(f'\t\ttest {index} | +{0}')
                print(f'\t\t\tdata: {res.data}')
                print(f'\t\t\tactual: {res.actual}')
                print(f'\t\t\texpected: {res.expected}')
        total += vertical_results.get_total_points()

        # HIT HORIZONTAL TESTS
        horizontal_results = Results(points=None)
        for test in test_cases.hit_horizontal_tests:
            result = Result(points=sub_points)
            result.expected = test['expected']
            circle = Circle(Point(test['x'], test['y']), test['radius'])
            result.data = (circle, win)
            result.actual = bumper.hit_horizontal(circle, win)
            result.passed = result.expected == result.actual
            horizontal_results.add(result)

        print('Test hit_horizontal Method:')
        if horizontal_results.number_failed == 0:
            print(f'\tPASSED {horizontal_results.number_passed} tests | +{horizontal_results.get_total_points()}')
        else:
            print(
                f'\tFAILED {horizontal_results.number_failed}/{len(test_cases.hit_horizontal_tests)} tests | +{horizontal_results.get_total_points()}')
            for index, res in enumerate(horizontal_results.failed_tests):
                print(f'\t\ttest {index} | +{0}')
                print(f'\t\t\tdata: {res.data}')
                print(f'\t\t\tactual: {res.actual}')
                print(f'\t\t\texpected: {res.expected}')
        total += horizontal_results.get_total_points()

        print(f'\n============================== {test_type} end ===============================\n')

    @pytest.fixture(scope='session', autouse=True)
    def summary(self):
        global total
        global code_style_points
        # Will be executed before the first test
        yield
        # Will be executed after the last test
        print(f'\nTotal: {total} / 90')
