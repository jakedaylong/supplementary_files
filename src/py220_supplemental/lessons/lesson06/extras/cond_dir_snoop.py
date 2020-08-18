# notice how the dummy need to return a function
import pysnooper

snoop = True


def do_not_decorate():
    def a(b):
        return b

    return a


if snoop is False:
    pysnooper.snoop = do_not_decorate


@pysnooper.snoop()
def coreFunction():
    print("snoop or not")


coreFunction()
