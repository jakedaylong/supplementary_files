import pysnooper
import math


#@pysnooper.snoop(depth=3)
def messy_function(x: int, y: int, z: int) -> int:
    x = y + z
    n = math.sqrt(x)
    y = n / 10
    return 7

messy_function(9,3,7)
