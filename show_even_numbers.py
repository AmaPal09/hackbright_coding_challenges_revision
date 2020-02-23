# You will be given a list of integers, some even and some odd:
# Write a function that returns the indices (0-based, as usual in Python) of all 
# the numbers which are even.

def show_evens(nums):
    """Given list of ints, return list of *indices* of even numbers in list.

        I/P: List 
        O/P: List 

        >>> lst = [1, 2, 3, 4, 6, 8]
        >>> show_evens(lst)
        [1, 3, 4, 5]

        >>> show_evens([])
        []
    """

    evens = [] 

    for i, num in enumerate(nums): 
        if num % 2 == 0: 
            evens.append(i)

    return evens


def show_evens_hb(nums):
    """Given list of ints, return list of *indices* of even numbers in list.

        I/P: List 
        O/P: List 

        >>> lst = [1, 2, 3, 4, 6, 8]
        >>> show_evens_hb(lst)
        [1, 3, 4, 5]

        >>> show_evens_hb([])
        []
    """

    evens = [] 

    for i in range(len(nums)): 
        if nums[i] % 2 == 0: 
            evens.append(i)

    return evens


if __name__ == "__main__": 

    import doctest 

    results = doctest.testmod()

    if results.failed == 0: 
        print("ALL TESTS PASSED")