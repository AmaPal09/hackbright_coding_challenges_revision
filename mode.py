# The “mode” of a list is the set of item(s) that occur the most often. 
# For example, in [1, 2, 2, 3], 2 is the most commonly-occurring item.

# Where there is a tie, the mode is all items that are tied for most 
# common: in [1, 1, 2, 2, 3], the mode is both 1 and 2.

# In this challenge, you should write a function that returns the mode.
# It should always return a set, even if there’s only one item in the set:

def mode(nums):
    """Find the most frequent num(s) in nums.

        I/P: List 
        O/P: Set 
        >>> mode([1]) == {1}
        True
        >>> mode([1, 2, 2, 2]) == {2}
        True
        >>> mode([1, 1, 2, 2]) == {1, 2}
        True
    """

    mode_dict = {} 

    for n in nums: 
        mode_dict[n] = mode_dict.get(n, 0) + 1 

    max_cnt = max(mode_dict.values())

    mode_set = set()

    for num, cnt in mode_dict.items(): 
        if cnt == max_cnt: 
            mode_set.add(num)

    return mode_set


def mode_hb(nums):
    """Find the most frequent num(s) in nums.

        I/P: List 
        O/P: Set 
        >>> mode([1]) == {1}
        True
        >>> mode([1, 2, 2, 2]) == {2}
        True
        >>> mode([1, 1, 2, 2]) == {1, 2}
        True
    """
    # Make dictionary of {num:frequency}

    num_count = {} 

    for num in nums: 
        num_count[num] = num_count.get(num, 0) + 1 

    # Find the *count* of highest letter

    highest_count = max(num_count.values())

    # For every number with that count, add to set of mode

    mode = set()

    for num, count in num_count.items(): 
        if count == highest_count: 
            mode.add(num)

    return mode


if __name__ == "__main__": 

    import doctest 

    results = doctest.testmod() 

    if results.failed == 0: 
        print("ALL TESTS PASSED ")
