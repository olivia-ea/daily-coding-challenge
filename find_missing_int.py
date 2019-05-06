
def find_missing_int(lst):
    """Given an array of integers, find the first missing positive 
    integer in linear time and constant space. In other words, 
    find the lowest positive integer that does not exist in the 
    array. The array can contain duplicates and negative numbers 
    as well.

    For example, the input [3, 4, -1, 1] should give 2. 
    The input [1, 2, 0] should give 3.

    You can modify the input array in-place.
    """
    for num in lst:
        if num < 0:
            lst.remove(num)

    lst = sorted(lst)

    compare_dict = {}

    for i in range(lst[0], lst[-1]):
        if i in lst:
            compare_dict[i] = i
        elif:
            return i
        else:
            return i + 1




