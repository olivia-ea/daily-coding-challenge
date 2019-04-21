import unittest

def return_majority(lst):

    majority = len(lst) / 2
    num_dict = {}
    
    for num in lst:
        num_dict[num] = num_dict.get(num, 0) + 1

    
    for key, value in num_dict.items():
        if value > majority:
            return key

class Test(unittest.TestCase):
    data = [
        ([4, 3, 13, 3, 3], 3)
    ]

    def test_is_anagram(self):
        for [lst, expected] in self.data:
            result = return_majority(lst)
            self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
            