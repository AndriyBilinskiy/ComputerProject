import itertools
def count(start=0, step=1):
    # count(10) --> 10 11 12 13 14 ...
    # count(2.5, 0.5) -> 2.5 3.0 3.5 ...
    n = start
    while True:
        yield n
        n += step
a = count(4)
b = itertools.count(4)
print(next(a),next( b))
print(next(a), next(b))