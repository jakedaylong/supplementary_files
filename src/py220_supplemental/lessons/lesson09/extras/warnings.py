# Robust code
# python -W module.py - use in tests

import warnings


class Car:
    def turn_left(self):
        warnings.warn("turn_left is deprecated; use turn instead", DeprecationWarning)
        self.turn(direction="left")

    def turn(self, direction):
        """Turn the car in some direction.
        :param direction: The direction to turn to.
        :type direction: str
        """
        # Write actual code for the turn function here instead
        pass


c = Car()
c.turn_left()
