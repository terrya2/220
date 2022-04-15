"""
Autumn Terry
sales_person.py
Create programs using objects and lists.
I certify that this assignment is entirely my own work.
"""

class SalesPerson:

    def __init__(self, employee_id, name, sales):
        self.employee_id = employee_id
        self.name = name
        self.sales = sales
    def get_id(self):
        return int(self.employee_id)

    def get_name(self):
        return self.name

    def set_name(self):
        name = eval(self.name)

    def _enter_sale(self, sale):
        first_sale = sale + self.sales
        return first_sale

    def total_sales(self, sale):
        sale = 0
        for i in self.sales:
            sale = sale + sale
            return sale

    def get_sales(self):
        sales_list = [self.sales]
        return sales_list

    def met_quota(self, quota):
        if self.total_sales >= quota:
            return True
        else:
            return False

    def compare_to(self, SalesPerson):
        if SalesPerson > self.total_sales:
            return -1
        elif self.total_sales < self:
            return 1
        elif self.total_sales == self:
            return 0

    def __str__(self):
        return self.employee_id, self.name, self.sales


