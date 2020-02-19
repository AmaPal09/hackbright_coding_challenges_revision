# Given an integer n, return a list containing n unique random numbers between 
# 1-10, inclusive. (That is, do not repeat any numbers in the returned list.)
# You can trust that this function will never be called with n < 0 or n > 10.
from random import choice, randint 

def lucky_numbers(n): 
    """Return n unique random numbers from 1-10 (inclusive).
        
        I/P: Int 
        O/P: List 
    
    >>> lucky_numbers(0)
    []
    >>> sorted(lucky_numbers(10))
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    """

    nums = list(range(1,11))
    
    set_lucky_nums = set()

    if n == 0: 
        return list(set_lucky_nums) 

    while len(set_lucky_nums) < n: 
        set_lucky_nums.add(choice(nums))

    return list(set_lucky_nums)
#Runtime O(n)


def lucky_numbers_2(n): 
    """Return n unique random numbers from 1-10 (inclusive).
        
        I/P: Int 
        O/P: List 
    
    >>> lucky_numbers_2(0)
    []
    >>> sorted(lucky_numbers_2(10))
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    """
    set_lucky_nums = set()

    if n == 0: 
        return list(set_lucky_nums) 

    while len(set_lucky_nums) < n: 
        set_lucky_nums.add(randint(1,10))

    return list(set_lucky_nums)
#Runtime O(n)

def lucky_numbers_hb(n):
    """Return n unique random numbers from 1-10 (inclusive).
    
    >>> lucky_numbers_hb(0)
    []
    >>> sorted(lucky_numbers_hb(10))
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """

    # START SOLUTION

    nums = list(range(1, 11))
    lucky_nums = []

    for i in range(n):
        num = choice(nums)
        nums.remove(num)
        lucky_nums.append(num)

    return lucky_nums
#Runtime O(n)


if __name__ == "__main__": 
    import doctest

    results = doctest.testmod()

    if results.failed == 0: 
        print("ALL TEST PASSED")

