import pytest
from tests import code_style
from hw2 import mean

code_style_points = 20

class TestClass:

    def test_one(self):
        pass

    def test_linting(self):
        global code_style_points
        points = code_style.code_style('mean.py', code_style_points)
        if not points == code_style_points:
            code_style_points = points
            pytest.xfail(reason="Failed Code Style")