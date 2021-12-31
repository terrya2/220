from hw4 import hw4
from tests.hw4 import random_tests
from tests.hw4.test_case import TestCase, Road
from tests.test_framework import *


def main():
    builder = TestBuilder('traffic', 'hw4.py', 10, 1)
    static_tests = build_static_test_section()
    dynamic_tests = build_dynamic_test_section()
    builder.add_items(static_tests, dynamic_tests)
    builder.run()


def build_static_test_section():
    road11 = Road(1, [20, 30, 15, 45])
    road12 = Road(2, [40, 30, 50])
    road13 = Road(3, [30, 60, 15, 55, 20])
    test1 = TestCase([road11, road12, road13])
    road21 = Road(1, [1])
    test2 = TestCase([road21])

    inputs = [test1, test2]
    return run_test(inputs, 'static tests')


# dynamic tests
def build_dynamic_test_section():
    data = random_tests.create(7, 55)
    return run_test(data, 'dynamic tests')


def run_test(test_cases: list[TestCase], test_type):
    # get all the outputs for each test [[test 1 outputs], [test 2 outputs], ...]
    for test_case in test_cases:
        user_in = test_case.get_user_input()
        output, result, error = get_IO(hw4.main, user_in)
        if not error:
            test_case.set_actual_values(output)
        else:
            print(error)
            sys.exit(1)

    section = Section(test_type)
    for index, test_case in enumerate(test_cases):
        sub_section = Section(f'test {index + 1}', group_data=[f'user inputs: {test_case.get_user_input()}'])

        expected_total = str(test_case.expected_total_cars).strip()
        expected_avg = str(test_case.expected_avg_cars).strip()
        actual_total = test_case.actual_total_cars[-len(expected_total):].strip()
        actual_avg = test_case.actual_avg_cars[-len(expected_avg):].strip()
        sub_section.add_items(
            Test('Total Cars', actual_total, expected_total),
            Test('Average Cars', actual_avg, expected_avg)
        )
        for road_index, road in enumerate(test_case.roads):
            expected_road_avg = str(road.expected_output)
            actual_road_avg = road.actual_output[-len(expected_road_avg):].strip()
            sub_section.add_items(Test(f'Roads {road_index + 1}', actual_road_avg, expected_road_avg))
        section.add_items(sub_section)
    return section
