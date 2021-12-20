""" task """

def permutations(iterable, length=None):
    """ Return successive r length permutations of elements in the iterable. """
    elems = tuple(iterable)
    lennn = len(iterable)
    length = lennn if not length else length
    if length > lennn:
        return
    indx = list(range(lennn))
    cycle = list(range(lennn, lennn - length, -1))
    # print(elems, lennn, length, indx, cycle)
    yield tuple(elems[ind] for ind in indx[:length])
    while lennn:
        for ind in reversed(range(length)):
            cycle[ind] -= 1
            if cycle[ind] == 0:
                indx[ind:] = indx[ind+1:] + indx[ind:ind+1]
                cycle[ind] = lennn - ind
            else:
                j = cycle[ind]
                indx[ind], indx[-j] = indx[-j], indx[ind]
                yield tuple(elems[ind] for ind in indx[:length])
                break
        else:
            return


def combinations(iterable, r):
    """ Return r length subsequences of elements from the input iterable """
    pool = tuple(iterable)
    lennn = len(pool)
    if r > lennn:
        return
    indices = list(range(r))
    yield tuple(pool[ind] for ind in indices)
    while True:
        for ind in range(r-1, -1, -1):
            if indices[ind] != ind + lennn - r:
                break
        else:
            return
        indices[ind] += 1
        for j in range(ind+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[ind] for ind in indices)
