import unittest


def add_up_to_k(lst, k):
    """
    Given a list of numbers and a number k, 
    return whether any two numbers from the 
    list add up to k.
    """

    diff_set = set()

    for num in lst:
        diff = k - num
        diff_set.add(diff)

    for num in lst:
        if num in diff_set:
            return True
    return False

class Test(unittest.TestCase):
    data = [
        ([10, 15, 3, 7], 17, True),
        ([10, 3 , 3, 12], 6, True),
        ([30, 10, 20, 14], 15, False),
        ([1, 2, 3, 4], 3, True)
    ]

    def test_add_up_to_k(self):
        for [lst, k, expected] in self.data:
            result = add_up_to_k(lst, k)
            self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
