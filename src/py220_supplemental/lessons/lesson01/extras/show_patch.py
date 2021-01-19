from mock import patch


# pretend I am an external function; I am problematic to test
def calculate():
    return 'y'


# I'm developing this; I use external function
def my_function():
    x = calculate()  # <- how to mock calculate() ?
    return x


def mytest():
    with patch('__main__.calculate') as calculate_mock:
        calculate_mock.return_value = 'blah'
        assert my_function() == 'blah'


if __name__ == "__main__":
    mytest()
