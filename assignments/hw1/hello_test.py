from hw1 import hello
from tests.test_framework import *


class TestClass:

    def test_input(self, capfd):
        builder = TestBuilder("Hello World!", 70)

        hello.main()
        captured = capfd.readouterr()
        actual = captured.out.strip()
        expected = "hello, world!"

        test = Test('print hello, world!', actual, expected)
        linting = create_lint_test('hello.py', 20)

        builder.add_items(test, linting)
        builder.run()
