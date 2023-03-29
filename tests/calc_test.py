import pytest

from app.calc import Calculator


class TestCalc():
    def setup(self):
        self.calc = Calculator

    def test_sub_calculate_correctly(self):
        assert self.calc.sub(self, 78, 12) == 66

    def test_add_calculate_correctly(self):
        assert self.calc.add(self, 256, 256) == 512

    def test_mult_calculate_correctly(self):
        assert self.calc.mult(self, 2, 2) == 4

    def test_div_calculate_correctly(self):
        assert self.calc.div(self, 10, 2) == 5





