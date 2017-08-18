from functools import reduce
from fractions import gcd
import random


def lcm(*numbers):
    """ Returns the Least Common Multiple of specified numbers """
    def lcm(a, b):
        return (a * b) // gcd(a, b)
    return reduce(lcm, numbers, 1)


def rows_of_random_numbers(rows=1000, count=3, minimum=1, maximum=1000):
    """
    Generate <rows> of lists with <count> random ints between minimum & maximum
    """
    for i in range(rows):
        this_row = list()
        for i in range(count):
            this_row.append(random.randint(minimum, maximum))
        yield this_row


def generate_lcm_rows(iterable):
    """ Generates lists where each list begins with the LCM of the items """
    for row in iterable:
        yield [lcm(*[int(i) for i in row]), *row]
