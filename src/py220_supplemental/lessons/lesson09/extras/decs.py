# decorators
"""A decorator is a function that takes another function as an argument and
replaces it with a new, modified function. The primary use case for decorators
is in factoring common code that needs to be called before, after, or
around multiple functions. IMHO they are like aspects in Java (cross cutting concerns)
They are quite different to Java annotations, but the syntax is obviously
similar"""


def check_is_admin(f):
    def wrapper(*args, **kwargs):
        if kwargs.get("username") != "admin":
            raise Exception("This user is not allowed to get or put food")
        return f(*args, **kwargs)

    return wrapper


class Store:
    @check_is_admin
    def get_food(self, username, food):
        return self.storage.get(food)

    @check_is_admin
    def put_food(self, username, food):
        self.storage.put(food)


s = Store()
s.get_food("admin", "curry")
