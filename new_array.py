import unittest
from functools import reduce

def new_array(lst):
    """
    Given an array of integers, return a new array such that each 
    element at index i of the new array is the product of all the 
    numbers in the original array except the one at i.
    """

    new_arr = []
    lst_prod = reduce((lambda x, y: x * y), lst)
    i = 0

    while i < len(lst):
        new = lst_prod // lst[i]
        new_arr.append(new)
        i += 1

    return new_arr
 
class Test(unittest.TestCase):
    data = [
        ([1, 2, 3, 4, 5], [120, 60, 40, 30, 24]),
        ([3, 2, 1], [2, 3, 6])
    ]

    def test_new_array(self):
        for [lst, expected] in self.data:
            result = new_array(lst)
            self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
