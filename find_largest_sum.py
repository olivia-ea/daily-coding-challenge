import unittest

def find_largest_sum(lst):
    """
    Given a list of integers, write a function that returns the 
    largest sum of non-adjacent numbers. Numbers can be 0 or 
    negative.

    ******COME BACK TO PROBLEM******

    
    """

    new_lst = sorted(lst)

    return new_lst[-2]+new_lst[-1]



class Test(unittest.TestCase):
    data = [
        ([2, 4, 6, 2, 5], 13),
        ([5, 1, 1, 5], 10)
    ]

    def test_find_largest_sum(self):
        for [lst, expected] in self.data:
            result = find_largest_sum(lst)
            self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
