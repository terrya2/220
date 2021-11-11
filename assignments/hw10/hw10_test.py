import os
import random
import sys

import pytest

from hw10.sales_person import SalesPerson
from hw10.sales_force import SalesForce
from tests.test_framework import Test_Framework as Tester

tester = Tester(sub_points=1)


class TestClass:

    def test_sales_person(self):
        global tester
        tester.area_start("Sales Person Tests")
        SALES_PERSON_ID = random.randint(0, 1000)
        SALES_PERSON_NAME = get_random_full_name()

        # Test Constructor
        tester.section("constructor")
        sales_person = None
        try:
            sales_person = SalesPerson(SALES_PERSON_ID, SALES_PERSON_NAME)
            tester.run_test(True, True, "initialize constructor")
        except Exception as e:
            print('\nFAILED: Could not initialize SalesPerson, no more test will run.')
            tester.section_end()
            tester.area_end("Sales Person Tests")
            sys.exit(1)
        tester.section_end()

        # test instance variables
        tester.section("instance variables")
        # employee_id
        tester.run_test(type(sales_person.employee_id), int, "instance variable employee_id")
        # name
        tester.run_test(type(sales_person.name), str, "instance variable name")
        # sales
        tester.run_test(type(sales_person.sales), list, "instance variable sales")
        tester.section_end()

        # test methods
        tester.section("methods")
        # get_id
        tester.run_test(sales_person.get_id(), SALES_PERSON_ID, "get_id")
        # get_name
        tester.run_test(sales_person.get_name(), SALES_PERSON_NAME, "get_name")
        # set_name
        new_name = 'New Name'
        sales_person.set_name(new_name)
        tester.run_test(sales_person.name, new_name, "set_name")
        # enter_sale
        sale_amount = random.uniform(0, 100.00)
        sales_person.enter_sale(sale_amount)
        tester.run_test(sales_person.sales[0], sale_amount, "enter_sale")
        # total_sales
        tester.run_test(sales_person.total_sales(), sale_amount, 'total_sales')
        # get_sales
        sales = sales_person.get_sales()
        tester.run_test(sales, [sale_amount], 'get_sales')
        # met_quota
        quota = random.uniform(0, sale_amount)
        tester.run_test(sales_person.met_quota(quota), True, 'met_quota',
                        data={'quota': quota, 'sales amount': sale_amount})
        quota = random.uniform(sale_amount + 1, sale_amount + 1000)
        tester.run_test(sales_person.met_quota(quota), False, 'met_quota',
                        data={'quota': quota, 'sales amount': sale_amount})
        tester.run_test(sales_person.met_quota(sale_amount), True, 'met_quota',
                        data={'quota': quota, 'sales amount': sale_amount})
        # compare_to
        other_person = SalesPerson(sales_person.employee_id, sales_person.name)
        other_person.sales = sales_person.sales
        tester.run_test(sales_person.compare_to(other_person), 0, "compare_to",
                        data={'this_sales': sales_person.sales, 'other_sales': other_person.sales})
        other_person.sales = [sum(sales_person.get_sales()) - 1]
        tester.run_test(sales_person.compare_to(other_person), 1, "compare_to",
                        data={'this_sales': sales_person.sales, 'other_sales': other_person.sales})
        other_person.sales = [sum(sales_person.get_sales()) + 1]
        tester.run_test(sales_person.compare_to(other_person), -1, "compare_to",
                        data={'this_sales': sales_person.sales, 'other_sales': other_person.sales})
        # __str__
        to_string = sales_person.__str__()
        id, rest = to_string.split('-')
        name, total_sales = rest.split(':')
        tester.run_test(id, str(sales_person.get_id()), '__str__ employee_id')
        tester.run_test(name, sales_person.get_name(), '__str__ name')
        tester.run_test(float(total_sales.strip()), sales_person.total_sales(), '__str__ total sales')

        tester.section_end()
        tester.area_end("Sales Person Tests")

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

        # top_seller
        expected_top_seller = SalesPerson(701, get_random_full_name())
        expected_top_seller.enter_sale(random.randint(7000, 80000))
        sales_force.sales_people.append(expected_top_seller)
        actual_top_seller: SalesPerson = sales_force.top_seller()
        expected_data = get_seller_data(expected_top_seller)
        data = {'actual': get_list_seller_data(actual_top_seller), 'expected': [expected_data]}
        tester.run_test(actual_top_seller, [expected_top_seller], 'top_seller - one', data)
        sales_force.sales_people.append(expected_top_seller)
        actual_top_seller: SalesPerson = sales_force.top_seller()
        data = {'actual': get_list_seller_data(actual_top_seller), 'expected': [expected_data, expected_data]}
        tester.run_test(actual_top_seller, [expected_top_seller, expected_top_seller], 'top_seller - multiple', data)

        # individual_sales
        sales_person = sales_force.individual_sales(701)
        data = {'expected': expected_data, 'actual': get_seller_data(sales_person)}
        tester.run_test(sales_person, expected_top_seller, 'individual_sales - exists', data)
        sales_person = sales_force.individual_sales(702)
        data = {'expected': None, 'actual': get_seller_data(sales_person)}
        tester.run_test(sales_person, None, 'individual_sales - does not exist', data)
        tester.section_end()
        tester.area_end("Sales Person Tests")

    def test_linter_sales_person(self):
        global tester
        tester.area_start("code style | sales person")
        tester.lint('sales_person.py', 15)
        tester.area_end("code style | sales person")

    def test_linter_sales_force(self):
        global tester
        tester.area_start("code style | sales force")
        tester.lint('sales_force.py', 15)
        tester.area_end("code style | sales force")

    @pytest.fixture(scope='session', autouse=True)
    def summary(self):
        yield
        tester.end_test(90)


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
