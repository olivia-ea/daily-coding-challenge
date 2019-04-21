import unittest

def find_target_nums(lst, target):

    dict = {}
    
    i = 0 
    for num in lst:
        dict[num] = i 
        i += 1 
        
    value1 = 0 
    value2 = 0 

    for key, value in dict.items():
        if key <= target:
            diff = target - key  
            value1 = key
            if diff in dict.keys():
                value2 = diff
                return value1, value2


class Test(unittest.TestCase):
    data = [
        ([15, 11, 7, 1, 2], 9, (7, 2))
    ]

    def test_find_target_nums(self):
        for [lst, target, expected] in self.data:
            result = find_target_nums(lst, target)
            self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
