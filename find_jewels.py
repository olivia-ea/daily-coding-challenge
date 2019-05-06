"""
You're given strings J representing the types of stones that are jewels, 
and S representing the stones you have.  Each character in S is a type 
of stone you have.  You want to know how many of the stones you have 
are also jewels.

The letters in J are guaranteed distinct, and all characters in J and 
S are letters. Letters are case sensitive, so "a" is considered a 
different type of stone from "A".

Input: J = "aA", S = "aAAbbbb"
Output: 3

Input: J = "z", S = "ZZ"
Output: 0
"""

def find_jewels(jewels, stones):
    jewels = list(jewels)
    stones = list(stones)

    jewels_dict = {}

    for jewel in jewels:
        for stone in stones:
            if stone == jewel:
                jewels_dict[jewel] = jewels_dict.get(jewel, 0) + 1
    return sum(jewels_dict.values())




