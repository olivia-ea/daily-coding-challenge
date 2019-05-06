import unittest

def find_decoded_combos(str):
    """
    Given the mapping a = 1, b = 2, ... z = 26, and an encoded 
    message, count the number of ways it can be decoded.

    For example, the message '111' would give 3, since it 
    could be decoded as 'aaa', 'ka', and 'ak'.

    You can assume that the messages are decodable. 
    For example, '001' is not allowed.
    """

    

class Test(unittest.TestCase):
    data = [
        ('111', 3)
    ]

    def test_find_decoded_combos(self):
        for [str, expected] in self.data:
            result = find_decoded_combos(str)
            self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()