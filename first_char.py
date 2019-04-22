import unittest

def first_char(str):
    dict = {}
    
    for letter in str:
        dict[letter] = dict.get(letter, 0) + 1
        
    for letter in str:
        if dict.get(letter) == 1:
            return letter

class Test(unittest.TestCase):
    data = [
        ('hello', 'h'), 
        ('teeter', 'r')
    ]

    def test_rev_int(self):
        for [str, expected] in self.data:
            result = first_char(str)
            self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
            