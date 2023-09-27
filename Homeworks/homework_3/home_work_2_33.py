"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.
def func(a, b):
    return (a ** b) ** 2
cache_func = cache(func)
some = 100, 200
val_1 = cache_func(*some)
val_2 = cache_func(*some)
assert val_1 is val_2
"""
from collections.abc import Callable


def cache(func: Callable) -> Callable:
    cashe = {}
    def inner_cashe_func(a, b):
        key = frozenset([a, b])
        if key in cashe:
            return cashe[key]
        else: 
            result = func(a, b)
            cashe[key] = result
            return result
    return inner_cashe_func