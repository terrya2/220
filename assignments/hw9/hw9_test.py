import random

from graphics import GraphWin, Point, Rectangle, Text

from hw9.button import Button
from tests.test_framework import *

win = GraphWin("Three Door Game", 600, 600)


def main():
    builder = TestBuilder('button', 'button.py', 12)
    builder.add_lint_test('three_door_game.py', 10)
    constructor_section, instance_vars_section, methods_section = build_sections()
    builder.add_items(constructor_section, instance_vars_section, methods_section)
    builder.run()


def build_sections():
    LABEL = "OK"
    rec_point_a = Point(1, 2)
    rec_point_b = Point(3, 4)
    rec = Rectangle(rec_point_a, rec_point_b)

    # Test Constructor
    constructor_section = Section("constructor")
    my_button = None
    try:
        my_button = Button(rec, LABEL)
        constructor_section.add_items(Test('initialize constructor', True, True))
    except Exception as e:
        print('\nFAILED: Could not initialize Button, no more test will run.')
        sys.exit(1)

    # test instance variables
    instance_vars_section = Section('instance variables')
    # shape
    instance_vars_section.add_items(
        Test("instance variable shape type", lambda: type(my_button.shape), Rectangle))

    instance_vars_section.add_items(Test("instance variable shape value", lambda: my_button.shape, rec))
    # text
    instance_vars_section.add_items(Test("instance variable text type", lambda: type(my_button.text), Text))
    instance_vars_section.add_items(Test("instance variable text value", lambda: my_button.text.getText(), LABEL))

    # test methods
    methods_section = Section('methods')
    # get_label
    label_test = Test("get_label", lambda: my_button.get_label(), LABEL)

    # draw

    def try_draw():
        my_button.draw(win)
        drawn_rect = None
        drawn_text = None
        for item in win.items:
            if type(item) == Rectangle: drawn_rect = item
            if type(item) == Text: drawn_text = item
        return rec == drawn_rect and drawn_text and drawn_text.getText() == LABEL

    draw_test = Test('draw rectangle and text', try_draw, True)

    # undraw
    def try_undraw():
        my_button.undraw()
        return len(win.items)

    undraw_test = Test('undraw', try_undraw, 0)

    methods_section.add_items(label_test, draw_test, undraw_test)

    # is_clicked
    click_check_one, click_check_two = build_is_clicked_tests()
    one_a_rect, one_b_rect, results_one = click_check_one
    two_a_rect, two_b_rect, results_two = click_check_two
    one_true_points, one_false_points = results_one[True], results_one[False]
    two_true_points, two_false_points = results_two[True], results_two[False]

    def try_click(rect, points, truth):
        # returns the value that is_clicked returns
        button = Button(rect, "test")
        for point in points:
            if not button.is_clicked(point) == truth:
                return not truth
        return truth

    is_clicked_subsection = Section('is_clicked()')

    def click_data(rect, points):
        return [f'click points: {points}', f'button dimensions: p1: {rect.getP1()}, p2: {rect.getP2()}']

    is_clicked_subsection.add_items(
        Test('click test true', lambda: try_click(one_a_rect, one_true_points, True), True,
             data=click_data(one_a_rect, one_true_points)),
        Test('click test true', lambda: try_click(one_b_rect, one_true_points, True), True,
             data=click_data(one_b_rect, one_true_points)),
        Test('click test false', lambda: try_click(one_a_rect, one_false_points, False), False,
             data=click_data(one_a_rect, one_false_points)),
        Test('click test false', lambda: try_click(one_b_rect, one_false_points, False), False,
             data=click_data(one_b_rect, one_false_points)),
        Test('click test true', lambda: try_click(two_a_rect, two_true_points, True), True,
             data=click_data(two_a_rect, two_true_points)),
        Test('click test true', lambda: try_click(two_b_rect, two_true_points, True), True,
             data=click_data(two_b_rect, two_true_points)),
        Test('click test false', lambda: try_click(two_a_rect, two_false_points, False), False,
             data=click_data(two_a_rect, two_false_points)),
        Test('click test false', lambda: try_click(two_b_rect, two_false_points, False), False,
             data=click_data(two_b_rect, two_false_points))
    )

    def try_color_button(button_color):
        button = Button(Rectangle(Point(1, 2), Point(3, 4)), 'test')
        button.color_button(button_color)
        return button.shape.config["fill"]

    # color_button
    color_button_subsection = Section('color_button()')
    colors = ["green", "red", "purple", "violet", "orange", "yellow", "thetimehascome", "blue"]
    color = gen(colors)
    for i in range(len(colors)):
        color_button_subsection.add_items(Test('color button', lambda: try_color_button(next(color)), next(color)))

    # set_label
    def try_set_label(label):
        button = Button(Rectangle(Point(1, 2), Point(3, 4)), 'test')
        button.set_label(label)
        return button.text.getText()

    set_label_subsection = Section('set_label()')
    label = gen(colors)
    for i in range(len(colors)):
        set_label_subsection.add_items(Test('set label', lambda: try_set_label(next(label)), next(label)))

    methods_section.add_items(is_clicked_subsection)
    methods_section.add_items(color_button_subsection)
    methods_section.add_items(set_label_subsection)

    return (constructor_section, instance_vars_section, methods_section)


def build_is_clicked_tests():
    """
    returns a tuple of two tuples
    ((rect, rect, {true: [click points], false: [click points]}), (rect, rect, {true: [click points], false: [click points]}))
    """
    # left top, right bottom
    lt_x, lt_y = random.randint(1, 10), random.randint(10, 20)
    rb_x, rb_y = random.randint(lt_x + 1, 20), random.randint(1, lt_y)
    ltrb_rect = Rectangle(Point(lt_x, lt_y), Point(rb_x, rb_y))
    ltrb_rect_2 = Rectangle(Point(rb_x, rb_y), Point(lt_x, lt_y))

    # outside - left, top, right, bottom
    ol, ot = Point(lt_x - 1, lt_y - 1), Point(lt_x + 1, lt_y + 1)
    ori, ob = Point(rb_x + 1, lt_y - 1), Point(lt_x, rb_y - 1)
    # on the line - left, top, right, bottom
    oll, olt = Point(lt_x, random.uniform(rb_y, lt_y)), Point(random.uniform(rb_x, lt_x), lt_y)
    olr, olb = Point(rb_x, random.uniform(rb_y, lt_y)), Point(random.uniform(lt_x, rb_x), rb_y)
    # inside
    inside_ltrb = Point(random.uniform(lt_x, rb_x), random.uniform(rb_y, lt_y))
    one = (ltrb_rect, ltrb_rect_2, {True: [oll, olt, olr, olb, inside_ltrb], False: [ol, ot, ori, ob]})

    # left bottom right top
    lb_x, lb_y = random.randint(1, 10), random.randint(1, 10)
    rt_x, rt_y = random.randint(lb_x + 1, 20), random.randint(lb_y + 1, 20)
    lbrt_rect = Rectangle(Point(lb_x, lb_y), Point(rt_x, rt_y))
    lbrt_rect_2 = Rectangle(Point(rt_x, rt_y), Point(lb_x, lb_y))

    # outside - left, top, right, bottom
    ol_lbrt, ot_lbrt = Point(lb_x - 1, rt_y - 1), Point(lb_x + 1, rt_y + 1)
    or_lbrt, ob_lbrt = Point(rt_x + 1, rt_y - 1), Point(lb_x + 1, lb_y - 1)
    # on the line - left, top, right, bottom
    oll_lbrt, olt_lbrt = Point(lb_x, random.uniform(lb_y, rt_y)), Point(random.uniform(lb_x, rt_x), rt_y)
    olr_lbrt, olb_lbrt = Point(rt_x, random.uniform(lb_y, rt_y)), Point(random.uniform(lb_x, rt_x), lb_y)
    # inside
    inside_lbrt = Point(random.uniform(lb_x, rt_x), random.uniform(lb_y, rt_y))
    two = (lbrt_rect, lbrt_rect_2,
           {True: [oll_lbrt, olt_lbrt, olr_lbrt, olb_lbrt, inside_lbrt], False: [ol_lbrt, ot_lbrt, or_lbrt, ob_lbrt]})

    return (one, two)


if __name__ == '__main__':
    main()
