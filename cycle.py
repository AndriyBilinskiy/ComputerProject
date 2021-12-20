def cycle(iterable):
    """
    Function for itertools.cycle()
    Makes an iterable cycle of every element.
    Returns a generator of a cycle
    :param iterable: optional
    """
    ans: list = []
    for i in iterable:
        yield i
        ans.append(i)
    while ans:
        for i in ans:
            yield i
