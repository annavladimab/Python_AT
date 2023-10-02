"""
Write a function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so one.
You may assume that that every list contain at least one element
Example:
assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]
"""
import itertools
from typing import Any, List
from itertools import product


def combinations(*args: List[Any]) -> List[List]:
    # decar = itertools.product(*args)
    # result = list()
    # for pair in decar:
    #     result.append(list(pair))
    # return result

    return [list(pair) for pair in itertools.product(*args)]
