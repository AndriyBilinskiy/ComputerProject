def repeat(value, stop_point=None):
    """
    The following function mirrors the behaviour of eponymous
    itertools repeat function.
    It takes two arguments:
    --- "value" argument (a required one)
        takes a value that is to be repeated by function
    --- "stop_point" argument (an optional one)
        defines a number at which repeating should stop;
        if not passed: function repeats the value infinetely;
        by default is None
    Function either repeats the value infinitely,
    or repeats the value up until reaching the stop point.
    The function can save time and effort 
    in writing long complicated tasks.
    The function is useful for "zip" and "map" usage.
    >>> for _ in repeat(8,3): print (_)
    8
    8
    8
    """
    if stop_point is not None:
        for _ in range(stop_point):
            yield value
    else:
        while True:
            yield value


from typing import Union
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


   
def cycle(iterable, endpoint=None):
    """
    Function for itertools.cycle()
    Makes an iterable cycle of every element.
    Returns a generator of a cycle
    :param iterable: any iterable type
    :param endpoint: optional
    for _ in cycle(iterable): print("x")
    """
    list_to_save = []
    for element in iterable:
        yield element
        if not endpoint is None:
            endpoint -= 1
            if endpoint <=0 :
                return
        list_to_save.append(element)
    while True:
        for element in list_to_save:
            yield element
            if not endpoint is None:
                endpoint -= 1
                if endpoint <=0 :
                    return

   
def product(*iterables, repeat=1):
    """
    Function for itertools.product()
    Makes a generated tuple of mixed elements.
    :param iterables: optional
    :param repeat: int >= 1
    """
    try:
        # processing exceptions
        pools = [tuple(pool) for pool in iterables] * repeat
        # making a list of tuples a repeat number of times
        lst = [[]]
        # making an empty list for answers
        for pool in pools:
            lst = [x + [y] for x in lst for y in pool]
            # appending the mixed iterable objects in the list
        for ans in lst:
            yield tuple(ans)
            # returning a generator of the ans list

    except TypeError:
        # preventing the Type error
        print("Type error")

def permutations(iterable, length=None):
    elems = tuple(iterable)
    lennn = len(iterable)
    length = lennn if not length else length
    if length > lennn:
        return
    indx = list(range(lennn))
    cycle = list(range(lennn, lennn - length, -1))
    yield tuple(elems[i] for i in indx[:length])
    while lennn:
        for ind in reversed(range(length)):
            cycle[ind] -= 1
            if cycle[ind] == 0:
                indx[ind:] = indx[ind+1:] + indx[ind:ind+1]
                cycle[ind] = lennn - ind
            else:
                j = cycle[ind]
                indx[ind], indx[-j] = indx[-j], indx[ind]
                yield tuple(elems[i] for i in indx[:length])
                break
        else:
            return

def combinations(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)
def combinations_order_matters(iterable, r: int):
    """
    This function returns r length combinations with replacrment(Order does metter)
    """
    if r > len(iterable): # ensures that the length of combinations is 
        #less than the lenth of a iterable object
        raise ValueError

    def create_coombinations(current_coombination, r, iterable):
        for element in iterable:
            current_coombination_copy = copy.copy(current_coombination)
            current_coombination_copy.append(element)
            if len(current_coombination_copy) == r:
                yield current_coombination_copy
            else:
                yield from create_coombinations(current_coombination_copy, r, iterable)
    yield from create_coombinations([], r, iterable)
    
