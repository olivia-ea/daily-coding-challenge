import unittest

def rev_int(num):
    
    rev = 0
    
    while num != 0:
        val = (num % 10) 
        rev = rev * 10 + val 
        num = num//10 
    return rev
        
class Test(unittest.TestCase):
    data = [
        (5432, 2345)
    ]

    def test_rev_int(self):
        for [num, expected] in self.data:
            result = rev_int(num)
            self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
            