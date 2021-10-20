import sys

from pylint import epylint as lint


class TestItem:
    def __init__(self, name: str, default_points: int):
        # default points are how much an individual test is worth
        #   this is so a section can have a default for all of the questions in the section
        # total points are the sum of the total possible points.
        self.default_points = default_points
        self.total_points = 0
        self.earned_points = 0
        self.name = name
        self.level = 1

    def run(self):
        pass


class Test(TestItem):
    def __init__(self, name, actual=None, expected=None, data=None, points=None, fail_fast=False):
        super().__init__(name, points)
        self.actual = actual
        self.expected = expected
        self.data = data
        self.fail_fast = fail_fast

    def PASSED(self):
        self.earned_points += self.default_points
        self.total_points += self.default_points
        tabs = '\t' * self.level
        print(f"{tabs}PASSED: +{self.total_points} - {self.name}")

    def FAILED(self):
        self.total_points += self.default_points
        tabs = '\t' * self.level
        print(f'{tabs}FAILED -{self.default_points}: {self.name}')
        if not self.actual is None:
            print(f'{tabs}\tactual: {self.actual} | expected: {self.expected}')
        if self.data:
            print(f'{tabs}\tdata: {self.data}')
        if self.fail_fast:
            sys.exit()

    def run(self, level=1):
        self.level = level
        if self.actual == self.expected:
            self.PASSED()
        else:
            self.FAILED()


class Section(TestItem):
    def __init__(self, name, points=None, custom_total_points=None):
        super().__init__(name, points)
        self.outline: list[TestItem] = []
        self.custom_total_points = custom_total_points
        # case where points are assigned up front and subtracted for wrong answers
        if not custom_total_points is None:
            self.total_points = custom_total_points
            self.earned_points = custom_total_points

    def add_items(self, *items: TestItem):
        for item in items:
            self.outline.append(item)

    def run(self, level=1):
        tabs = '\t' * level
        start_label = f' {self.name} start '
        print()
        print('{0}{1:-^70}'.format(tabs, start_label))
        for item in self.outline:
            if item.default_points is None:
                item.default_points = self.default_points
            item.run(level + 1)
            if self.custom_total_points is None:
                self.total_points += item.total_points
                self.earned_points += item.earned_points
            # case where points are assigned up front and subtracted for wrong answers
            else:
                self.earned_points -= item.total_points
        end_label = f' {self.name} end {self.earned_points}/{self.total_points} '
        print('{0}{1:-^70}'.format(tabs, end_label))


class TestBuilder:
    def __init__(self, name, default_test_points=1):
        self.outline: list[TestItem] = []
        self.total_points = 0
        self.earned_points = 0
        self.default_test_points = default_test_points
        self.name = name

    def add_items(self, *items: TestItem):
        for item in items:
            self.outline.append(item)
        return self

    def run(self):
        print()
        print()
        test_intro = f' Starting test {self.name} '
        print('{0:=^80}'.format(test_intro))
        print()
        for item in self.outline:
            if item.default_points is None:
                item.default_points = self.default_test_points
            item.run()
            self.total_points += item.total_points
            self.earned_points += item.earned_points
        print()
        test_outro = f' Test {self.name} complete: {self.earned_points}/{self.total_points} '
        print('{0:=^80}'.format(test_outro))


def create_lint_test(test_file, points, rc_file='../../.pylintrc') -> Section:
    linting = Section('Linting', custom_total_points=points)
    (pylint_stdout, pylint_stderr) = lint.py_run(f'{test_file} --rcfile {rc_file}', return_std=True)
    output = pylint_stdout.getvalue()
    error_list = output.split("\n")[1:-1]
    # case when the errors exceeds the possible points
    error_range = range(len(error_list))
    if points < len(error_list):
        error_range = range(points)
    for i in error_range:
        linting.add_items(Test(error_list[i], None, 1, points=1))
    if points < len(error_list):
        linting.add_items(Test(f'...and {len(error_list) - points} more errors', None, 1, points=0))
    return linting


class Test_Framework:
    def __init__(self, global_points=5, sub_points=2, code_style_points=15):
        self.global_points = global_points
        self.sub_points = sub_points
        self.code_style_points = code_style_points
        self.test_total_score = 0
        self.test_total_possible_score = 0
        self.test_questions_correct = 0
        self.test_questions_total = 0
        self.area_score = 0
        self.area_questions_correct = 0
        self.area_questions_total = 0
        self.section_score = 0
        self.section_questions_correct = 0
        self.section_questions_total = 0

    def PASSED(self, test_name):
        self.section_questions_correct += 1
        self.section_score += self.sub_points

        print(f"\tPASSED: +{self.sub_points} - {test_name}")

    def FAILED(self, actual, expected, test_name, data):
        print(f'\tFAILED -{self.sub_points}: {test_name}')
        print(f'\t\tactual: {actual} | expected: {expected}')
        if data:
            print(f'\t\tdata: {data}')

    def run_test(self, actual, expected, test_name="", data=""):
        self.section_questions_total += 1
        self.test_total_possible_score += self.sub_points

        if actual == expected:
            self.PASSED(test_name)
        else:
            self.FAILED(actual, expected, test_name, data)

    def area_start(self, name):
        self.area_score = 0
        self.area_questions_correct = 0
        self.area_questions_total = 0
        print(f'\n\n============================== {name} start ===============================\n')

    def area_end(self, name):
        self.test_total_score += self.area_score
        self.test_questions_correct += self.area_questions_correct
        self.test_questions_total += self.area_questions_total

        print(
            f'\n============================== {name} end - {self.area_questions_correct}/{self.area_questions_total} +{self.area_score} ===============================\n')

    def section(self, name):
        self.section_score = 0
        self.section_questions_correct = 0
        self.section_questions_total = 0
        print(f'{name}')

    def section_end(self):
        self.area_score += self.section_score
        self.area_questions_correct += self.section_questions_correct
        self.area_questions_total += self.section_questions_total
        print(f'\t{self.section_questions_correct}/{self.section_questions_total} +{self.section_score}')

    def end_test(self, total_possible):
        total = self.test_total_possible_score if total_possible is None else total_possible
        print(f'\nDONE: {self.test_total_score}/{total}')

    def lint(self, filename, points, rcfile='../../.pylintrc'):
        self.area_questions_total = points
        (pylint_stdout, pylint_stderr) = lint.py_run(f'{filename} --rcfile {rcfile}', return_std=True)
        output = pylint_stdout.getvalue()
        points_off = len(output.split("\n")) - 2
        points_off = 0 if points_off < 0 else points_off

        self.area_questions_correct = 0 if points_off > points else points - points_off
        self.area_score = self.area_questions_correct
        self.test_total_possible_score += points

        passed = points_off <= 0
        if passed:
            print("\nPASSED", f"+{points}")
        else:
            print("\nFAILED")
            print(output)
            print('-' + str(points_off))
