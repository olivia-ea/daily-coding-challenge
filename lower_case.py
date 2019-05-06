"""
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.
65 = A
97 = a

diff = 32

A => # + 32 => a

65-91 = all upper

check all letters if in range of 65-91
if so, change to # and add 32
then change back to letter

"""

def lower_case(word):

    word_lst = []

    for letter in word:
        if ord(letter) < 91:
            letter = chr(ord(letter) + 32)
            word_lst.append(letter)
        else:
            word_lst.append(letter)
    return "".join(word_lst)





