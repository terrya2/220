import os
import random
import sys

import pytest

from hw10.sales_person import SalesPerson
from hw10.sales_force import SalesForce
from tests.test_framework import *


class TestClass:

    def test_stuff(self):
        test_suit = TestSuit('HW 10')
        sales_person_builder = TestBuilder('Sales Person', 'sales_person.py', 10)
        sales_force_builder = TestBuilder('Sales Force', 'sales_force.py', 10)
        constructor_section, instance_vars_section, methods_section = sales_person_test()

        sales_person_builder.add_items(constructor_section, instance_vars_section, methods_section)
        sales_person_builder.run()
        # test_suit.add_test_builders(sales_person_builder, sales_force_builder)
        # test_suit.run()


def make_sales_person_with_sales(sp_id, sp_name, sale_1, sale_2):
    sales_person = SalesPerson(sp_id, sp_name)
    sales_person.enter_sale(sale_1)
    sales_person.enter_sale(sale_2)
    return sales_person


def sales_person_test():
    SALES_PERSON_ID = random.randint(0, 1000)
    SALES_PERSON_NAME = get_random_full_name()

    # Test Constructor
    constructor_section = Section('Constructor')
    outcome, sales_person = run_safe(lambda: SalesPerson(SALES_PERSON_ID, SALES_PERSON_NAME))
    if not outcome:
        print('\nFAILED: Could not construct SalesPerson, no more test will run.')
        sys.exit(1)
    constructor_section.add_items(Test('initialize constructor', True, True, show_actual_expected=False))

    # test instance variables
    iv_person = SalesPerson(SALES_PERSON_ID, SALES_PERSON_NAME)
    instance_variables_section = Section('Instance Variables')
    employee_id_test = Test('instance variable employee_id', type(iv_person.employee_id), int)
    name_test = Test('instance variable name', type(iv_person.name), str)
    sales_test = Test('instance variable sales', type(iv_person.sales), list)
    instance_variables_section.add_items(employee_id_test, name_test, sales_test)

    # test methods
    methods_section = Section('Methods')
    # get_id
    methods_person = SalesPerson(SALES_PERSON_ID, SALES_PERSON_NAME)
    methods_section.add_items(Test('get_id', lambda: methods_person.get_id(), SALES_PERSON_ID))
    # get_name
    methods_section.add_items(Test('get_name', lambda: methods_person.get_name(), SALES_PERSON_NAME))
    # set_name
    new_name = 'New Name'

    set_name_person = SalesPerson(SALES_PERSON_ID, SALES_PERSON_NAME)

    def set_name_test():
        set_name_person.set_name(new_name)
        return set_name_person.name

    methods_section.add_items(Test('set_name', set_name_test, new_name))
    # enter_sale
    enter_sale_person = SalesPerson(SALES_PERSON_ID, SALES_PERSON_NAME)
    sale_amount_1 = random.uniform(0, 100.00)
    sale_amount_2 = random.uniform(0, 100.00)
    total_sales = sale_amount_1 + sale_amount_2

    def sale_test():
        enter_sale_person.enter_sale(sale_amount_1)
        enter_sale_person.enter_sale(sale_amount_2)
        return enter_sale_person.sales[0], enter_sale_person.sales[1]

    methods_section.add_items(Test('enter_sale', sale_test, (sale_amount_1, sale_amount_2)))

    # total_sales
    methods_section.add_items(Test('total_sales', lambda: enter_sale_person.total_sales(), total_sales))

    # get_sales
    methods_section.add_items(Test('get_sales', lambda: enter_sale_person.get_sales(), [sale_amount_1, sale_amount_2]))

    # met_quota
    try:
        quota_sales_person = make_sales_person_with_sales(SALES_PERSON_ID, SALES_PERSON_NAME, sale_amount_1,
                                                          sale_amount_2)
        quota_hit = random.uniform(0, total_sales)
        quota_miss = random.uniform(total_sales + 1, total_sales + 1000)
        a = lambda: quota_sales_person.met_quota(quota_hit)
        b = lambda: quota_sales_person.met_quota(quota_miss)

        quota_tests = [(a, True, quota_hit), (b, False, quota_miss)]
        for lambda_func, expected, quota in quota_tests:
            methods_section.add_items(
                Test('met_quota', lambda_func, expected,
                     data=[f'quota: {quota}', f'sales amount: {total_sales}']))
        # methods_section.add_items(
        #     Test('met_quota - miss', lambda: sales_person.met_quota(quota_tests[1][0]), quota_tests[1][1],
        #          data=[f'quota: {quota_tests[1][0]}', f'sales amount: {total_sales}']))
    except Exception as e:
        methods_section.add_items(
            Test('met_quota - hit', True, False, show_actual_expected=False,
                 data=['Test could not run due to an exception', e]))
        methods_section.add_items(
            Test('met_quota - miss', True, False, show_actual_expected=False,
                 data=['Test could not run due to an exception', e]))

    # compare_to
    try:
        compare_to_person = make_sales_person_with_sales(SALES_PERSON_ID, SALES_PERSON_NAME, sale_amount_1,
                                                         sale_amount_2)
        other_person_equal = SalesPerson(compare_to_person.employee_id, compare_to_person.name)
        other_person_equal.sales = compare_to_person.sales
        lambda_equal = compare_to_person.compare_to(other_person_equal)

        other_person_greater = SalesPerson(compare_to_person.employee_id, compare_to_person.name)
        other_person_greater.sales = [sum(compare_to_person.sales) + 1]
        lambda_less_than = compare_to_person.compare_to(other_person_greater)

        other_person_less = SalesPerson(compare_to_person.employee_id, compare_to_person.name)
        other_person_less.sales = [sum(compare_to_person.sales) - 1]
        lambda_greater_than = compare_to_person.compare_to(other_person_less)

        for lambda_func, expected, other in (
                (lambda_equal, 0, other_person_equal), (lambda_less_than, -1, other_person_greater),
                (lambda_greater_than, 1, other_person_less)):
            methods_section.add_items(Test('compare_to', lambda_func, expected,
                                           data=[f'this_sales: {compare_to_person.sales}',
                                                 f'other_sales: {other.sales}']))
    except Exception as e:
        methods_section.add_items(
            Test('compare_to - equal', True, False, show_actual_expected=False,
                 data=['Test could not run due to an exception', e]),
            Test('compare_to - less than', True, False, show_actual_expected=False,
                 data=['Test could not run due to an exception', e]),
            Test('compare_to - greater than', True, False, show_actual_expected=False,
                 data=['Test could not run due to an exception', e])
        )

    # # __str__
    string_sale_person = make_sales_person_with_sales(SALES_PERSON_ID, SALES_PERSON_NAME, sale_amount_1, sale_amount_2)

    def string_id_test():
        to_string = string_sale_person.__str__()
        emp_id, rest = to_string.split('-')
        return int(emp_id)

    def string_name_test():
        to_string = string_sale_person.__str__()
        emp_id, rest = to_string.split('-')
        name, total_sales = rest.split(':')
        return name

    def string_total_sales_test():
        to_string = string_sale_person.__str__()
        emp_id, rest = to_string.split('-')
        name, total_sales = rest.split(':')
        return float(total_sales.strip())

    methods_section.add_items(Test('__str__ (id)', string_id_test, SALES_PERSON_ID))
    methods_section.add_items(Test('__str__ (name)', string_name_test, SALES_PERSON_NAME))
    methods_section.add_items(Test('__str__ (total sales)', string_total_sales_test, sale_amount_1 + sale_amount_2))

    return constructor_section, instance_variables_section, methods_section

    def test_sales_force(self):
        global tester
        tester.area_start("Sales Force Tests")

        # Test Constructor
        tester.section("constructor")
        sales_force = None
        try:
            sales_force = SalesForce()
            tester.run_test(True, True, "initialize constructor")
        except Exception as e:
            print('\nFAILED: Could not initialize SalesForce, no more test will run.')
            tester.section_end()
            tester.area_end("Sales Force Tests")
            sys.exit(1)
        tester.section_end()

        # test instance variables
        tester.section("instance variables")
        # employee_id
        tester.run_test(type(sales_force.sales_people), list, "instance variable sales_people")
        tester.section_end()

        # test methods
        tester.section("methods")
        # add_data
        sales_data = build_sales_data()
        file_name = 'test_hw10_data_b02fce0e'
        write_sales_data(sales_data, file_name)
        sales_force.add_data(file_name)
        for index, seller in enumerate(sales_force.sales_people):
            tester.run_test(seller.employee_id, sales_data[index][0], "add_data - employee_id")
            tester.run_test(seller.name, sales_data[index][1], "add_data - name")
            tester.run_test(seller.sales, sales_data[index][2], "add_data - sales")
        os.remove(file_name)

        # quota_report
        quota = random.randint(200, 700)
        quota_report = sales_force.quota_report(quota)
        for index, seller in enumerate(quota_report):
            data = {'actual data': seller, 'expected data': sales_data[index], 'quota': quota}
            tester.run_test(seller[0], sales_data[index][0], "quota_report - employee_id", data)
            tester.run_test(seller[1], sales_data[index][1], "quota_report - name", data)
            total_sales = sum(sales_data[index][2])
            tester.run_test(seller[2], total_sales, "quota_report - total sales", data)
            tester.run_test(seller[3], total_sales >= quota, "quota_report - hit quota", data)

        # # top_seller
        # expected_top_seller = SalesPerson(701, get_random_full_name())
        # expected_top_seller.enter_sale(random.randint(7000, 80000))
        # sales_force.sales_people.append(expected_top_seller)
        # actual_top_seller: SalesPerson = sales_force.top_seller()
        # expected_data = get_seller_data(expected_top_seller)
        # data = {'actual': get_list_seller_data(actual_top_seller), 'expected': [expected_data]}
        # tester.run_test(actual_top_seller, [expected_top_seller], 'top_seller - one', data)
        # sales_force.sales_people.append(expected_top_seller)
        # actual_top_seller: SalesPerson = sales_force.top_seller()
        # data = {'actual': get_list_seller_data(actual_top_seller), 'expected': [expected_data, expected_data]}
        # tester.run_test(actual_top_seller, [expected_top_seller, expected_top_seller], 'top_seller - multiple', data)
        #
        # # individual_sales
        # sales_person = sales_force.individual_sales(701)
        # data = {'expected': expected_data, 'actual': get_seller_data(sales_person)}
        # tester.run_test(sales_person, expected_top_seller, 'individual_sales - exists', data)
        # sales_person = sales_force.individual_sales(702)
        # data = {'expected': None, 'actual': get_seller_data(sales_person)}
        # tester.run_test(sales_person, None, 'individual_sales - does not exist', data)
        # tester.section_end()
        # tester.area_end("Sales Person Tests")


def get_seller_data(seller: SalesPerson):
    if seller:
        return {
            'employee_id': seller.employee_id,
            'name': seller.name,
            'sales': seller.sales
        }
    return None


def get_list_seller_data(sellers: list[SalesPerson]):
    data = []
    for seller in sellers:
        data.append(get_seller_data(seller))
    return data


def get_random_name():
    name_letters = random.randint(3, 10)
    name = ''
    for i in range(name_letters):
        letter_index = random.randint(0, 25)
        letter = chr(ord('a') + letter_index)
        name += letter
    return name


def get_random_full_name():
    return get_random_name() + ' ' + get_random_name()


def build_sales_data():
    count = 5
    data = []
    for i in range(1, count + 1):
        id = random.randint(i * 100 + 1, i * 100 + 100)
        name = get_random_full_name()
        sales_count = random.randint(1, 5)
        sales = []
        for j in range(sales_count):
            sales.append(round(random.uniform(100, 500), 2))
        data.append([id, name, sales])
    return data


def write_sales_data(data, file_name):
    with open(file_name, 'w') as test_data_file:
        for person in data:
            id = str(person[0])
            name = person[1]
            sales = ' '.join(map(str, person[2]))
            test_data_file.write(f'{id}, {name}, {sales}\n')
