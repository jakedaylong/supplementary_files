def proc_nums(func, parm1, parm2):
    return func(parm1, parm2)


def adder(lhs, rhs):
    return lhs + rhs


def suber(lhs, rhs):
    return lhs - rhs


assert proc_nums(adder, 3, 4) == 7
assert proc_nums(suber, 100, 98) == 2
# -------

options = {"1": adder, "2": suber}

selected = ''
while True:
    selected = input("enter 1 to add, 2 to subtract or x to quit : ")
    if selected.upper() == "X":
        break
    result = options[selected](23, 12)
    print(f"result : {result}")
