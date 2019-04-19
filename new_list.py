import unittest

def new_list(lst, i=1):

    if lst[-i] == 9:
        lst[-i] = 0 
        return new_list(lst, i+1) 

    else:
        lst[-i] = lst[-i] + 1
        return lst

class Test(unittest.TestCase):
    data = [
        ([1, 2, 3], [1, 2, 4]),
        ([1, 2, 9], [1, 3, 0]),
        ([1, 9, 9], [2, 0, 0])
    ]

    def test_new_list(self):
        for [lst, expected] in self.data:
            result = new_list(lst)
            self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
