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
        self.area_questions_correct += 1
        self.section_questions_correct += 1
        self.test_questions_correct += 1

        self.area_score += self.sub_points
        self.section_score += self.sub_points
        self.test_total_score += self.sub_points

        print(f"\tPASSED: +{self.sub_points} - {test_name}")


    def FAILED(self, actual, expected, test_name, data):
        print(f'\tFAILED -{self.sub_points}: {test_name}')
        print(f'\t\tactual: {actual} | expected: {expected}')
        print(f'\t\tdata: {data}')


    def run_test(self, actual, expected, test_name="", data=""):
        self.area_questions_total += 1
        self.section_questions_total += 1
        self.test_questions_total += 1
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
        print(f'\n============================== {name} end - {self.area_questions_correct}/{self.area_questions_total} +{self.area_score} ===============================\n')

    def section(self, name):
        self.section_score = 0
        self.section_questions_correct = 0
        self.section_questions_total = 0
        print(f'{name}')

    def section_end(self):
        print(f'\t{self.section_questions_correct}/{self.section_questions_total} +{self.section_score}')

    def end_test(self):
        print(f'\nDONE: {self.test_total_score}/{self.test_total_possible_score}')


