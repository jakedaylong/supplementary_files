# pip install loguru

from loguru import logger


class Memoize:

    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
            logger.info(f"memoizing {args}")
            self.memo[args] = self.fn(*args)
        else:
            logger.info(f"not memoizing {args} - done already")
        return self.memo[args]


@Memoize
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def main():
    fib(10)
    fib(20)
    fib(10)


if __name__ == "__main__":
    main()

