from typing import Union
"""
Realization of analogs for some functions forom itertools library.
"""

def count(start: Union[int, float] = 0, step: Union[int, float] = 1, endpoint = None):
    """
    Returns an generator of the infinite sequence of nuberes spaced by step
    starting with start
    """
    if type(start) in (int, float) and type(step) in (int, float):
            number = start
            while True:
                yield number
                number += step
                if not endpoint is None and number > endpoint:
                    return
    raise TypeError


def combinations_with_replacement(iterable, r: int):
    """
    This function returns r length combinations with replacrment(Order doesn't metter)
    """
    iterable = tuple(iterable)
    lenth = len(iterable)
    if r > lenth :
        raise ValueError
    indices = [0] * r
    yield tuple(iterable[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != lenth - 1:
                break
        else:
            return
        indices[i:] = [indices[i] + 1] * (r - i)
        yield tuple(iterable[i] for i in indices)
    
#print(list (i for i in (combinations_with_replacement('ABC', 2))))

# for i in count(start=2, step=2, endpoint = 400):
#     print(i)
