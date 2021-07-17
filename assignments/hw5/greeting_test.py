"""
a lump sum of points are awarded per test.
you cannot lose more points for a test than the max points per test
"""

import pytest

from tests.code_style import code_style

total = 0
code_style_points = 20


class TestClass:

    def test_linting(self):
        global code_style_points
        global total
        points = code_style('greeting.py', code_style_points)
        total += points
        if not points == code_style_points:
            pytest.xfail(reason="Failed Code Style")

    @pytest.fixture(scope='session', autouse=True)
    def summary(self):
        global total
        global code_style_points
        # Will be executed before the first test
        yield
        # Will be executed after the last test
        print(f'\nTotal: {total} / {code_style_points}')
