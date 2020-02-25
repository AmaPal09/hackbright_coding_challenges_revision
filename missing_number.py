# Imagine a list of numbers from 1 to max_num, inclusive – except that one of 
# these numbers will be missing from the list.
# You should write a function that takes this list of numbers, as well as the 
# max_num, and it should return the missing number.
# For example, given a list of numbers, in random order, of 1..10, 8 was 
# removed. Your function would be given the list and the max_num (10), and it 
# should find 8:

def missing_number(nums, max_num):
    """Given a list of numbers 1...max_num, find which one is missing.

        I/P: List, Int 
        O/P: Int 

        >>> missing_number([1, 2, 3, 4, 5, 6, 7, 9, 10], 10)
        8
    """
    nums_set = set(nums)

    for num in range(1, max_num+1): 
        if num not in nums_set: 
            return num


def missing_number_hb(nums, max_num):
    """Given a list of numbers 1...max_num, find which one is missing.

    *nums*: list of numbers 1..[max_num]; exactly one digit will be missing.
    *max_num*: Largest potential number in list

    >>> missing_number_hb([1, 2, 3, 4, 5, 6, 7, 9, 10], 10)
    8
    """
    # Initial solution: keep track of what you've
    #                      seen in a separate list

    seen = [False] * max_num

    for n in nums: 
        seen[n-1] = True 

    # The False value is the one we haven't seen 

    return seen.index(False) + 1 


def missing_number_hb_2(nums, max_num):
    """Given a list of numbers 1...max_num, find which one is missing.
    
    For a simple O(n log n) solution, you could sort the numbers first, 
    then scan them to see which one is missing:
    *nums*: list of numbers 1..[max_num]; exactly one digit will be missing.
    *max_num*: Largest potential number in list

    >>> missing_number_hb_2([1, 2, 3, 4, 5, 6, 7, 9, 10], 10)
    8
    """ 
    # 2nd solution: if we can't create another data structure
    #               sort and scan for missing number

    nums.append(max_num + 1 )
    nums.sort()
    last = 0 

    for i in nums: 
        if i != last + 1: 
            return last + 1 
        last += 1 

    raise Exception("None are missing!") 


def missing_number_hb_3(nums, max_num):
    """Given a list of numbers 1...max_num, find which one is missing.
    
    For a simple O(n log n) solution, you could sort the numbers first, 
    then scan them to see which one is missing:
    *nums*: list of numbers 1..[max_num]; exactly one digit will be missing.
    *max_num*: Largest potential number in list

    >>> missing_number_hb_3([1, 2, 3, 4, 5, 6, 7, 9, 10], 10)
    8
    """ 
    # 3rd solution: find missing number by comparing expected sum vs actual

    expected = sum(range(max_num+1))

    # expected = ( n + 1 ) * ( n / 2 )
    
    return expected - sum(nums)


if __name__ == "__main__": 

    import doctest 

    results = doctest.testmod() 

    if results.failed == 0: 
        print("ALL TESTS PASSED ")
