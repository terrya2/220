"""
a lump sum of points are awarded per test.
you cannot lose more points for a test than the max points per test
"""

import random

import pytest

from hw3 import traffic
from tests.code_style import code_style
from tests.hw3.TestCase import TestCase, Road

total = 0
points_per_test = 5
sub_points = 1
code_style_points = 10


def input_map(sentence):
    return float(sentence.split(':')[1].strip())


class TestClass:

    def test_output(self, monkeypatch, capfd):
        road11 = Road(1, [20, 30, 15, 45])
        road12 = Road(2, [40, 30, 50])
        road13 = Road(3, [30, 60, 15, 55, 20])
        test1 = TestCase([road11, road12, road13])
        road21 = Road(1, [1])
        test2 = TestCase([road21])

        inputs = [test1, test2]
        self.run_test(inputs, 'static tests', monkeypatch, capfd)

    def test_random(self, monkeypatch, capfd):
        data = self.make_test_data(14)
        self.run_test(data, 'random tests', monkeypatch, capfd)

    @staticmethod
    def run_test(test_cases, test_type, monkeypatch, capfd):
        global total
        global points_per_test
        global sub_points
        failed = 0

        # get all of the outputs for each test [[test 1 outputs], [test 2 outputs], ...]
        for test_case in test_cases:
            user_in = test_case.get_user_input()
            i = iter(user_in)
            monkeypatch.setattr('builtins.input', lambda input_message: next(i))
            traffic.main()
            captured = capfd.readouterr()
            output = captured.out.strip().split('\n')
            test_case.set_actual_values(list(map(input_map, output)))

        print(f'\n\n============================== {test_type} start ===============================\n')

        for test_case in test_cases:
            num_failed = test_case.num_failed()
            if num_failed == 0:
                print(f'PASSED {test_case.total_tests}/{test_case.total_tests} tests  +{str(points_per_test)}')
                total += points_per_test
            else:
                points_off = sub_points * num_failed if sub_points * num_failed < points_per_test else points_per_test
                print(f'FAILED {num_failed}/{test_case.total_tests} tests -{str(points_off)}')
                print(f'\tdata:')
                print(f'\t\tnumber of roads: {len(test_case.roads)}')
                for road in test_case.roads:
                    print(f'\t\troad {road.id}:')
                    print(f'\t\t\tdays: {road.days}')
                    print(f'\t\t\tcars per day: {road.cars_per_day}')
                if test_case.expected_total_cars == test_case.actual_total_cars:
                    print(f'\ttotal cars: PASSED | +{sub_points}')
                else:
                    print(f'\ttotal cars: FAILED | -{sub_points}')
                    print(f'\t\texpected {test_case.expected_total_cars} but got {test_case.actual_total_cars}')
                if test_case.expected_avg_cars == test_case.actual_avg_cars:
                    print(f'\taverage cars: PASSED | +{sub_points}')
                else:
                    print(f'\taverage cars: FAILED | -{sub_points}')
                    print(f'\t\texpected {test_case.expected_avg_cars} but got {test_case.actual_avg_cars}')
                for road in test_case.roads:
                    if road.expected_output == road.actual_output:
                        print(f'\troad {road.id} average cars: PASSED | +{sub_points}')
                    else:
                        print(f'\troad {road.id} average cars: FAILED | -{sub_points}')
                        print(f'\t\texpected {road.expected_output} but got {road.actual_output}')

                total += points_per_test - points_off

        noun = 'test' if num_failed == 1 else 'tests'
        print(f'\n============================== {failed} {noun} failed ===============================\n')

    @staticmethod
    def make_test_data(num):
        data = []
        for i in range(num):
            roads = []
            number_of_roads = random.randint(1, 10)
            for road in range(number_of_roads):
                cars_per_day = []
                number_of_days = random.randint(1, 20)
                for day in range(number_of_days):
                    cars_per_day.append(random.randint(1, 20))
                id = road + 1
                roads.append(Road(id, cars_per_day))
            data.append(TestCase(roads))

        return data

    def test_linting(self):
        global code_style_points
        global total
        points = code_style('traffic.py', code_style_points)
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
