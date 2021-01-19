"""
recursion
"""


def my_fun(n):
    if n <= 1:
        return True
    return my_fun(n / 2)


if __name__ == '__main__':
    n = 100
    print(my_fun(n))


"""
        ---^|v
    ---^|v
---^|v

"""
