# attrib
import attr


@attr.s
class Car(object):
    color = attr.ib(converter=str)
    speed = attr.ib(default=0)

    @speed.validator
    def speed_validator(self, attribute, value):
        if value < 0:
            raise ValueError("Value cannot be negative")


c = Car("red")
print(c.speed)
print(c.color)

# https://glyph.twistedmatrix.com/2016/08/attrs.html
# https://jackmckew.dev/dataclasses-vs-attrs-vs-pydantic.html
