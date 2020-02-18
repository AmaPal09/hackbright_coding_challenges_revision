def add_to_zero(nums):
    """Given list of ints, return True if any two nums sum to 0.

        I/P: List of nums 
        O/P: Binary(T/F)
        >>> add_to_zero([])
        False

        >>> add_to_zero([1])
        False

        >>> add_to_zero([1, 2, 3])
        False

        >>> add_to_zero([1, 2, 3, -2])
        True

        >>> add_to_zero([0])
        True
    """

    if len(nums)==0: 
        return False
    
    if len(nums)==1: 
        if nums[0]==0: 
            return True
        else: 
            return False

    nums_set = set(nums)
    if 0 in nums_set: 
        return True
    for n in nums: 
        if -n in nums_set: 
            return True

    return False 
#Runtime == O(n)


def add_to_zero_hb(nums):
    """Given list of ints, return True if any two nums sum to 0.

        I/P: List of nums 
        O/P: Binary(T/F)
        >>> add_to_zero_hb([])
        False

        >>> add_to_zero_hb([1])
        False

        >>> add_to_zero_hb([1, 2, 3])
        False

        >>> add_to_zero_hb([1, 2, 3, -2])
        True

        >>> add_to_zero_hb([0])
        True
    """

    set_nums = set(nums)

    for n in nums:
        if -n in set_nums:
            return True

    return False


def add_to_zero_hb2(nums):
    """Given list of ints, return True if any two nums sum to 0.

        I/P: List of nums 
        O/P: Binary(T/F)
        >>> add_to_zero_hb2([])
        False

        >>> add_to_zero_hb2([1])
        False

        >>> add_to_zero_hb2([1, 2, 3])
        False

        >>> add_to_zero_hb2([1, 2, 3, -2])
        True

        >>> add_to_zero_hb2([0])
        True
    """

    set_nums = set(nums)
    
    return any(-n in set_nums for n in nums)


if __name__ =='__main__':
    import doctest

    result = doctest.testmod()

    if result.failed==0: 
        print("ALL TEST PASSED")