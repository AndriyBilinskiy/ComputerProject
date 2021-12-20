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
