"""
Autumn Terry
sales_force.py
Create programs using objects and lists.
I certify that this assignment is entirely my own work.
"""

from hw11.sales_person import SalesPerson


class SalesForce:

    def __init__(self, sales_people):
        self.sales_list = [SalesPerson]
        self.sales_people = self.sales_list

    def add_data(self, sales_person, filename):
        sales_file = open(filename, "r")
        info = sales_file.readlines()
        for sales_person in info:
            employee = self.employee_id + "/n"
            name = self.name + "/n"
            sale_amount = self.sales + "/n"
        sales_person.insert(self.sales_list)

    def quota_report(self, quota):
        employee = self.employee_id
        name = self.name
        sale_amount = self.sales
        tot_sales = SalesPerson.self.total_sales
        if tot_sales >= quota:
            return True
        else:
            return False

        return [employee, name, sale_amount, tot_sales]


    def top_seller(self):
        pass

    def individual_sales(self, employee_id):
        if SalesPerson == employee_id:
            return [SalesPerson, employee_id]
        else:
            return [SalesPerson, "None"]

    def get_sale_frequencies(self):
        pass