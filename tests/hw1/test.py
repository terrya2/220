from hw1 import hello
from tests.test_framework import *


def main():
    builder = TestBuilder("Hello World!", 'hello.py', linter_points=20, default_test_points=70)
    output, result, error = get_IO(hello.main)
    expected = "hello, world!"
    if error:
        test = Test('print hello, world!', f'error: {error}', expected)
    else:
        actual = output[0]
        test = Test('print hello, world!', actual, expected)
    builder.add_items(test)

    builder.run()


if __name__ == '__main__':
    main()
