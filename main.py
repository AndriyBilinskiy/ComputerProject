from typing import Union
"""
Realization of analogs for some functions forom itertools library.
"""

def count(start: Union[int, float] = 0, step: Union[int, float] = 1):
    """
    Returns an generator of the infinite sequence of nuberes spaced by step
    starting with start
    """
    number = start
    while True:
        yield number
        number += step


def combinations_with_replacement(iterable, r):
    pass
