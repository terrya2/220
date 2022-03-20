import math

from tests.test_framework import *

import hw10

try:
    from assignments.hw10.sphere import Sphere
except:
    Sphere = None


def main():
    test_suit = TestSuit('HW 10')

    builder = TestBuilder("hw10.py", 'hw10.py', linter_points=20, default_test_points=2)
    builder.add_to_blacklist({
        'for.*in.*:': 'for loops not allowed for this assignment. please remove it to continue',
    })
    builder.add_items(build_fibonacci_tests(10))
    builder.add_items(build_double_investment_tests(10))
    builder.add_items(build_syracuse_tests(10))
    builder.add_items(build_goldbach_tests(10))

    sphere_builder = TestBuilder("sphere", "sphere.py", linter_points=20, default_test_points=10)
    sphere_builder.add_items(build_sphere_tests())

    test_suit.add_test_builders(builder, sphere_builder)
    test_suit.run()


def build_sphere_tests():
    test_name = 'sphere'
    section = Section(test_name)

    SPHERE_RADIUS_INT = random.randint(1, 1000)
    SPHERE_RADIUS_FLOAT = random.uniform(1, 1000)
    NUMBER_OF_TESTS = 8
    DEFAULT_TEST_POINTS = 10

    # Test Constructor
    constructor_section = Section('Constructor')
    outcome, sales_person = run_safe(lambda: Sphere(SPHERE_RADIUS_INT))
    if not outcome:
        section.add_items(Test('initialize sphere', True, False, show_actual_expected=False,
                               exception_message='Could not construct Sphere, no more tests will run',
                               points=NUMBER_OF_TESTS * DEFAULT_TEST_POINTS))
        return section
    constructor_section.add_items(Test('initialize sphere', True, True))

    # test instance variables
    instance_variables_section = Section('Instance Variables')
    iv_sphere_int = Sphere(SPHERE_RADIUS_INT)
    iv_sphere_float = Sphere(SPHERE_RADIUS_FLOAT)
    radius_int_type_test = Test('radius int type', lambda: type(iv_sphere_int.radius), int)
    radius_int_value_test = Test('radius int value', lambda: iv_sphere_int.radius, SPHERE_RADIUS_INT)
    radius_float_type_test = Test('radius float type', lambda: type(iv_sphere_float.radius), float)
    radius_float_value_test = Test('radius float value', lambda: iv_sphere_float.radius, SPHERE_RADIUS_FLOAT)

    instance_variables_section.add_items(radius_int_type_test, radius_int_value_test, radius_float_type_test,
                                         radius_float_value_test)

    # test methods
    methods_section = Section('Methods')
    error = 0.0000000000001
    sphere_surface_area = random.uniform(1, 100)
    sa_radius = math.sqrt(sphere_surface_area / 4 / math.pi)
    sa_sphere = Sphere(sa_radius)

    volume = random.uniform(1, 100)
    v_radius = (volume * 3 / 4 / math.pi) ** (1 / 3)
    v_sphere = Sphere(v_radius)
    # get_radius
    methods_section.add_items(Test('get_radius', lambda: Sphere(SPHERE_RADIUS_FLOAT).get_radius(), SPHERE_RADIUS_FLOAT))
    # surface_area
    methods_section.add_items(
        Test('surface_area', lambda: sa_sphere.surface_area(), sphere_surface_area, comp_func=delta_comp_func(error),
             data=[f'radius: {sa_radius}']))
    # volume
    methods_section.add_items(
        Test('volume', lambda: v_sphere.volume(), volume, comp_func=delta_comp_func(error),
             data=[f'radius: {v_radius}']))

    section.add_items(constructor_section, instance_variables_section, methods_section)
    return section


def build_goldbach_tests(n):
    test_name = 'goldbach'
    none_test_count = 1
    section = Section(test_name)
    odds = [x for x in range(100000) if x % 2 != 0]
    evens = [x for x in range(10000) if x % 2 == 0]
    odd_test_values = random.choices(odds, k=none_test_count)
    even_test_values = random.choices(evens, k=n - none_test_count)
    odds_gen = gen(odd_test_values)
    evens_gen = gen(even_test_values)

    test_num = 1
    for value in odd_test_values:
        section.add_items(Test(f'{test_name}-Returns None-{test_num}', lambda: hw10.goldbach(next(odds_gen)), None,
                               data=[f'input: {value}']))
        test_num += 1
    for value in even_test_values:
        outcome, results = run_safe(lambda: hw10.goldbach(next(evens_gen)))
        if not outcome:
            section.add_items(
                Test(f'{test_name}-{test_num}', True, False, show_actual_expected=False, data=[f'input: {value}'],
                     exception_message=results))
        else:
            is_list = True
            list_length = 0
            try:
                list_length = len(results)
            except:
                is_list = False
            if not (is_list and list_length == 2):
                section.add_items(
                    Test(f'{test_name}-{test_num}', True, False, show_actual_expected=False,
                         data=[f'input: {value}', f'output: {results}'],
                         exception_message='Function did not return a list of two elements'))
            elif results[0] + results[1] != value:
                section.add_items(
                    Test(f'{test_name}-{test_num}', True, False, show_actual_expected=False,
                         data=[f'input: {value}', f'output: {results}'],
                         exception_message='Results do not sum to input value'))
            elif not (i_p(results[0]) and i_p(results[1])):
                section.add_items(
                    Test(f'{test_name}-{test_num}', True, False, show_actual_expected=False,
                         data=[f'input: {value}', f'output: {results}'],
                         exception_message='At least one output value is not prime'))
            else:
                section.add_items(
                    Test(f'{test_name}-{test_num}', True, True, show_actual_expected=False))
        test_num += 1
    return section


def i_p(n):
    sqrt = math.floor(math.sqrt(n))
    for i in range(2, sqrt + 1):
        if n % i == 0:
            return False
    return True


def build_syracuse_tests(n):
    test_name = 'syracuse'
    section = Section(test_name)
    test_values = [random.randint(1, 100) for _ in range(n)]
    test_val_gen = gen(test_values)
    for i in range(n):
        section.add_items(Test(f'{test_name}-{i + 1}', lambda: hw10.syracuse(next(test_val_gen)),
                               list(collatz_gen(next(test_val_gen))), data=[f'input: {test_values[i]}']))
    return section


def collatz_gen(n):
    yield n
    while n != 1:
        n = n / 2 if n % 2 == 0 else 3 * n + 1
        yield int(n)


def build_double_investment_tests(n):
    test_name = 'double_investment'
    section = Section(test_name)
    principal_inputs = []
    rate_inputs = []
    expected_values = []
    for i in range(n):
        principal = random.randint(1, 100000)
        a = principal * 2
        rate = round(random.uniform(0.01, 0.4), 2)
        time = math.log(a / principal) / math.log(1 + rate)
        principal_inputs.append(principal)
        rate_inputs.append(rate)
        expected_values.append(math.ceil(time))
    principal_gen = gen(principal_inputs)
    rate_gen = gen(rate_inputs)
    expected_gen = gen(expected_values)
    for i in range(n):
        section.add_items(
            Test(test_name, lambda: hw10.double_investment(next(principal_gen), next(rate_gen)), next(expected_gen),
                 data=[f'principal: {next(principal_gen)}, rate: {next(rate_gen)}']))
    return section


def build_fibonacci_tests(n):
    test_name = 'fibonacci'
    section = Section(test_name)
    i = []
    for _ in range(n):
        i.append(random.randint(1, 600))
    i_gen = gen(i)
    for index in range(1, n + 1):
        section.add_items(
            Test(f'{test_name}-{index}', lambda: hw10.fibonacci(next(i_gen)), next(gen_fib(next(i_gen))),
                 data=[f'input: {i[index - 1]}']))
    return section


def gen_fib(n):
    total = 1
    prev = 1
    for i in range(2, n):
        x = total
        total += prev
        prev = x
    yield total
