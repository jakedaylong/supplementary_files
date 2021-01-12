def proc_nums(func, parm1, parm2):
    return func(parm1, parm2)


def adder(lhs, rhs):
    return lhs + rhs


def suber(lhs, rhs):
    return lhs - rhs


assert proc_nums(adder, 3, 4) == 7
assert proc_nums(suber, 100, 98) == 2

