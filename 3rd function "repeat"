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
    >>> for _ in repeat(8,-1): print (_)
    >>> list(zip(range(4), repeat('text')))
    [(0, 'text'), (1, 'text'), (2, 'text'), (3, 'text')]
    >>> for _ in repeat(['a','b','c'],2): print(_[2])
    c
    c
    >>> list(map(lambda x: x*2,repeat(10,6)))
    [20, 20, 20, 20, 20, 20]
    >>> tuple(map(lambda x: x[0],repeat([['1','2'],'3'],6)))
    (['1', '2'], ['1', '2'], ['1', '2'], ['1', '2'], ['1', '2'], ['1', '2'])
    >>> if '__iter__' in dir(repeat(1,3)): print('function returned an iterator')
    function returned an iterator
    """
    if stop_point is not None:
        for _ in range(stop_point):
            yield value
    else:
        while True:
            yield value
