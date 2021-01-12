from unittest.mock import patch
import time


def complex_function():
    time.sleep(99999)
    return "abc"


def function_a():
    return complex_function().upper()


def test_function_a():
    with patch("show_mock.complex_function") as complex_function_mock:
        complex_function_mock.return_value = "foo"
        assert function_a() == "FOO"
