# our metaclass
class MultiBases(type):
    # overriding __new__ method
    def __new__(cls, clsname, bases, clsdict):
        # if no of base classes is greater than 1
        # raise error
        if len(bases) > 1:
            raise TypeError("\nInherited multiple base classes!!!\n")

        # else execute __new__ method of super class, ie.
        # call __init__ of type class
        return super().__new__(cls, clsname, bases, clsdict)


# metaclass can be specified by 'metaclass' keyword argument
# now MultiBase class is used for creating classes
# this will be propagated to all subclasses of Base
class Base(metaclass=MultiBases):
    pass


# no error is raised
class A(Base):
    pass


# no error is raised
class B(Base):
    pass


# This will raise an error!
 class C(A, B):
    pass


# This metaclass adds a 'hello' method to classes that use the metaclass
# Such classes get a 'hello' method with no extra effort
# The metaclass takes care of that for us


class HelloMeta(type):
    # A hello method
    def hello(cls):
        print("greetings from %s, a HelloMeta type class" % (type(cls())))

    # Call the metaclass
    def __call__(self, *args, **kwargs):
        # create the new class as normal
        cls = type.__call__(self, *args)

        # define a new hello method for each of these classes
        setattr(cls, "hello", self.hello)

        # return the class
        return cls


# Try out the metaclass
class TryHello(object, metaclass=HelloMeta):
    def greet(self):
        self.hello()


# Create an instance of the metaclass. It should automatically have a
# hello method
# even though one is not defined manually in the class
# in other words, it is added for us by the metaclass
greeter = TryHello()
greeter.greet()
