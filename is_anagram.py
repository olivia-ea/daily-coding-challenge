import unittest

def is_anagram(str1, str2):
    
    dict_str1 = {}
    
    dict_str2 = {}
    
    for letter in str1:
        dict_str1[letter] = dict_str1.get(letter, 0) + 1
        
    for letter in str2:
        dict_str2[letter] = dict_str2.get(letter, 0) + 1
        
    if dict_str1 == dict_str2:
        return True
    return False 


class Test(unittest.TestCase):
    data = [
        ('iceman', 'cinema', True)
    ]

    def test_is_anagram(self):
        for [st1, str2, expected] in self.data:
            result = is_anagram(st1, str2)
            self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
