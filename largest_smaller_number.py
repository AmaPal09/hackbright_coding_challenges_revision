# Given an ordered list of numbers and a number, return the index of the largest 
# number in the list that is smaller than that number.
# Never find xnumber — it’s not smaller than itself!
# If no such number exists, return None:

def find_largest_smaller_than(nums, xnumber):
    """Find largest number in sorted list that is smaller than given number.
        
        I/P1: List 
        I/P: int 
        O/P: int or None 

        >>> find_largest_smaller_than([-5, -2, 8, 12, 32], 10)
        2

        >>> find_largest_smaller_than([-5, -2, 8, 12, 32], 33)
        4

        >>> find_largest_smaller_than([-5, -2, 8, 12, 32], -1)
        1
        
        >>> find_largest_smaller_than([-5, -2, 8, 12, 32], 8)
        1
        
        >>> find_largest_smaller_than([-5, -2, 8, 12, 32], -10) is None
        True

    """

    i = len(nums) -1 

    for num in nums[-1::-1]: 
        if num < xnumber: 
            return i 
        i -= 1 

    return None 


def find_largest_smaller_than_hb(nums, xnumber):
    """Find largest number in sorted list that is smaller than given number.
    
        I/P1: List 
        I/P: int 
        O/P: int or None 

        >>> find_largest_smaller_than([-5, -2, 8, 12, 32], 10)
        2

        >>> find_largest_smaller_than([-5, -2, 8, 12, 32], 33)
        4

        >>> find_largest_smaller_than([-5, -2, 8, 12, 32], -1)
        1
        
        >>> find_largest_smaller_than([-5, -2, 8, 12, 32], 8)
        1
        
        >>> find_largest_smaller_than([-5, -2, 8, 12, 32], -10) is None
        True

    """

    # START SOLUTION

    # Fail-fast optimization: since our list is sorted, if the first number
    # is bigger, a smaller number isn't in our list

    if nums[0] >= xnumber:
        return None

    # Optimization: if the last number isn't too big, it's the answer

    if nums[-1] < xnumber:
        return len(nums) - 1

    # Else, loop through and return the index right before the first number
    # that is too big

    for i, num in enumerate(nums):
        if num >= xnumber:
            return i-1


if __name__ == "__main__": 
    
    import doctest 

    results = doctest.testmod()

    if results.failed == 0: 
        print("ALL TESTS PASSED")