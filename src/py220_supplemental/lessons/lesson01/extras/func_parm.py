from typing import Callable


def proc_nums(func: Callable, parm1: int, parm2: int) -> Callable:
    # todo Name this better?
    return func(parm1, parm2)


def adder(lhs, rhs):
    return lhs + rhs


def suber(lhs, rhs):
    return lhs - rhs


assert proc_nums(adder, 3, 4) == 7
assert proc_nums(suber, 100, 98) == 2
