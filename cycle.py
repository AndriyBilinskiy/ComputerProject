def cycle(iterable, endpoint=None):
    """
    Function for itertools.cycle()
    Makes an iterable cycle of every element.
    Returns a generator of a cycle
    :param iterable: str
    :param endpoint: optional
    for _ in cycle(iterable): print("x")
    """
    try:
        # processing exceptions
        if endpoint is not None:
            # making an endpoint
            ans: list = []
            # an empty list for an answer
            for letters in iterable:
                yield letters
                # a generated object for iterable var
                ans.append(letters)
                # appending the generator in the empty list
            while ans:
                # excluding the None and negative cases
                for letters in ans:
                    yield letters
                    # returning a generator of the ans list

    except TypeError:
        # preventing the Type error
        print("Type error")
