# https://www.python.org/dev/peps/pep-0570/#logical-ordering
# Positional-only parameters also have the (minor) benefit of enforcing some logical order when
# calling interfaces that make use of them. For example, the range function takes all its
# parameters positionally and disallows forms like:

# range(stop=5, start=0, step=2)
# range(stop=5, step=2, start=0)
# range(step=2, start=0, stop=5)
# range(step=2, stop=5, start=0)

# at the price of disallowing the use of keyword arguments for the (unique) intended order:

# range(start=0, stop=5, step=2)
"""
Write a function that accept any sequence (list, string, tuple) of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""
import string
from typing import Union, List, Tuple


def custom_range(sequence, *args):
    sequence = list(sequence)
    # if stop isn't specified
    if len(args) == 1:
        start, stop, step = args[0], None, None
    elif len(args) == 2:
        start, stop, step = args[0], args[1], None
    else:
        start, stop, step = args[0], args[1], args[2]
    if step is None:
        step = 1
    if stop is None:
        stop = sequence.index(start)
        start = 0
    if type(stop) == str:
        stop = sequence.index(stop)
        start = sequence.index(start)
    if start > stop:
        sequence = sequence[stop + 1:start + 1]
        step = -step
        sequence.reverse()
        return sequence[::step]
    return sequence[start:stop:step]
