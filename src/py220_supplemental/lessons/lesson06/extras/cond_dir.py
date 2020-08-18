
use_decorator = True


class DevDecorator(object):
    def __init__(self, f):
        self.f = f

    def __call__(self):
        print("We are in the decorator...")
        print("Entering wrapped func now", self.f.__name__)
        self.f()
        print("Exited wrapped func", self.f.__name__)


def do_not_decorate(a):
    return a


if use_decorator is False:
    DevDecorator = do_not_decorate


@DevDecorator
def coreFunction():
    print("CoreFunction runs with conditional decoration")


coreFunction()
