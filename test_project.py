"""
A module of unittests for combinatorial functions:
repeat, count, combinations_with_replacement, cycle, product, combinations, permutations.
"""

import unittest
from project import repeat, count, combinations_with_replacement, cycle, product, combinations, permutations, permutations_repetitions


class TestFunctions(unittest.TestCase):
    def test_repeat(self):
        self.assertEqual(list(map(lambda x: x * 2, repeat(10, 6))),
                         [20, 20, 20, 20, 20, 20])
        self.assertEqual(list(zip(range(4), repeat('text'))), [(0, 'text'),
                                                               (1, 'text'),
                                                               (2, 'text'),
                                                               (3, 'text')])
        self.assertEqual(list(repeat(8, -1)), [])
        self.assertEqual(str(repeat(5))[1:10], 'generator')
        self.assertEqual(
            tuple(map(lambda x: x[0], repeat([['1', '2'], '3'], 6))),
            (['1', '2'], ['1', '2'], ['1', '2'], ['1', '2'], ['1', '2'
                                                              ], ['1', '2']))
        self.assertTrue('__iter__' in dir(repeat(1, 3)))

    def test_count(self):
        self.assertEqual(list(count(1, 1, 5)), [1, 2, 3, 4, 5])
        self.assertEqual(tuple(count(0.5, 0.5, 1.5)), (0.5, 1.0, 1.5))
        self.assertEqual(str(count(1, 1))[1:26], 'generator object count at')
        self.assertRaises(TypeError, count("abc", 3))
        self.assertEqual(list(zip(range(3), count(10, 10))), [(0, 10), (1, 20),
                                                              (2, 30)])
        self.assertTrue('__iter__' in dir(repeat(1, 3)))

    def test_combinations_with_replacement(self):
        self.assertEqual(list(combinations_with_replacement('ABC', 2)),
                         [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'),
                          ('B', 'C'), ('C', 'C')])
        self.assertEqual(
            tuple(zip(combinations_with_replacement(["a", "b"], 2), range(3))),
            ((('a', 'a'), 0), (('a', 'b'), 1), (('b', 'b'), 2)))
        self.assertEqual(
            list(map(lambda x: x * 2, combinations_with_replacement([1, 2],
                                                                    2))),
            [(1, 1, 1, 1), (1, 2, 1, 2), (2, 2, 2, 2)])
        self.assertRaises(TypeError, combinations_with_replacement("math", 7))

    def test_cycle(self):
        self.assertCountEqual(list(cycle("abc",6)), list(cycle("bca", 6)))
        self.assertEqual(list(cycle("abc", 9)),
                         ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c'])
        self.assertEqual(tuple(cycle([1], 2)),
                         tuple(list(map(int, (cycle("1", 2))))))
        self.assertEqual(list(zip(cycle(range(5), 10), range(10))), [(0, 0),
                                                                    (1, 1),
                                                                    (2, 2),
                                                                    (3, 3),
                                                                    (4, 4),
                                                                    (0, 5),
                                                                    (1, 6),
                                                                    (2, 7),
                                                                    (3, 8),
                                                                    (4, 9)])

    def test_product(self):
        self.assertEqual(list(product("ab", "c", repeat=2)),
                         [('a', 'c', 'a', 'c'), ('a', 'c', 'b', 'c'),
                          ('b', 'c', 'a', 'c'), ('b', 'c', 'b', 'c')])
        self.assertEqual(list(product([1, 2], [4, 5])), [(1, 4), (1, 5),
                                                         (2, 4), (2, 5)])
        self.assertEqual(
            tuple(
                map(lambda x: list(map(ord, x)), product(['a', 'b'],
                                                         ['c', 'd']))),
            ([97, 99], [97, 100], [98, 99], [98, 100]))
        self.assertEqual(
            list(map(lambda x: x[0] * x[1], product([12, 16], [15, 20]))),
            [180, 240, 240, 320])
        self.assertRaises(TypeError, product("1", 2, repeat=1))
        
    def test_permutations(self):
        self.assertEqual(list(permutations("abc")), [('a', 'b', 'c'),
                                                     ('a', 'c', 'b'),
                                                     ('b', 'a', 'c'),
                                                     ('b', 'c', 'a'),
                                                     ('c', 'a', 'b'),
                                                     ('c', 'b', 'a')])
        self.assertEqual(tuple(permutations([1, 2, 3])),
                         ((1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1),
                          (3, 1, 2), (3, 2, 1)))
        self.assertEqual(list(permutations(("i", "we", "us"), 2)),
                         [('i', 'we'), ('i', 'us'), ('we', 'i'), ('we', 'us'),
                          ('us', 'i'), ('us', 'we')])
        self.assertEqual(
            list(map(lambda x: sum(x), permutations([1, 2, 4], 2))),
            [3, 5, 3, 6, 5, 6])

    def test_combinations(self):
        self.assertEqual(list(combinations("abc", 2)), [('a', 'b'), ('a', 'c'),
                                                        ('b', 'c')])
        self.assertEqual(tuple(combinations([0, 1, 2], 2)),
                         ((0, 1), (0, 2), (1, 2)))
        self.assertEqual(len(list(combinations([1, 2, 3, 4, 5], 3))), 10)
        self.assertEqual(
            len(
                list(
                    filter(lambda x: len(set(x)) == 1, combinations("mttt",
                                                                    2)))), 3)


    def test_permutations_repetitions(self):
        self.assertEqual(list(permutations_repetitions([1, 2, 3], 2)),
                         [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3],
                          [3, 1], [3, 2], [3, 3]])
        self.assertEqual(list(permutations_repetitions([1, 2, 3], 1)),
                         [[1], [2], [3]])
        self.assertEqual(
            tuple(zip(permutations_repetitions(["a", "b"], 2), range(4))),
            ((['a', 'a'], 0), (['a', 'b'], 1), (['b', 'a'], 2),
             (['b', 'b'], 3)))
        self.assertEqual(
            list(map(lambda x: x * 2, permutations_repetitions([1, 2], 2))),
            [[1, 1, 1, 1], [1, 2, 1, 2], [2, 1, 2, 1], [2, 2, 2, 2]])


if __name__ == '__main__':
    unittest.main()
