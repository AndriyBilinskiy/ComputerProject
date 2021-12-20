from typing import Union
"""
Realization of analogs for some functions forom itertools library.
"""

def count(start: Union[int, float] = 0, step: Union[int, float] = 1):
    """
    Returns an generator of the infinite sequence of nuberes spaced by step
    starting with start
    """
    if (not isinstance(start, int) or not isinstance(step, int)
        or not isinstance(start, float) or not isinstance(step, float)):
        raise TypeError
    number = start
    while True:
        yield number
        number += step


def combinations_with_replacement(iterable, r):
    pass
