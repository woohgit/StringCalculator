from unittest import TestCase
from string_calculator import add


class TestStringCalculator(TestCase):
    def test_empty_string_should_return_0(self):
        assert add("") == 0

    def test_print_numbers(self):
        assert add("1") == 1
        assert add("2") == 2

    def test_add_numbers(self):
        assert add("1,1") == 2
        assert add("2,2") == 4

    def test_newline_as_a_delimiter(self):
        assert add("1\n1") == 2
        assert add("1\n2") == 3