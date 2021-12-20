def product(*iterables, repeat=1):
    """
    Function for itertools.product()
    Makes a generated tuple of mixed elements.
    :param iterables: optional
    :param repeat: int >= 1
    """
    pools = [tuple(pool) for pool in iterables] * repeat
    lst = [[]]
    for pool in pools:
        lst = [x + [y] for x in lst for y in pool]
    for ans in lst:
        yield tuple(ans)
