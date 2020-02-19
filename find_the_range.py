# Given a list of numbers, return the smallest and the largest number.

def find_range(nums):
    """Given list of numbers, return smallest & largest number as a tuple.

    I/P: List of numbers
    O/P: Tuple of range 

    >>> find_range([3, 4, 2, 5, 10])
    (2, 10)
    >>> find_range([43, 3, 44, 20, 2, 1, 100])
    (1, 100)
    >>> find_range([])
    (None, None)
    >>> find_range([7])
    (7, 7)

    """

    if len(nums) == 0: 
        return (None, None)

    if len(nums) == 1: 
        return (nums[0], nums[0])

    return (min(nums), max(nums))


def find_range_hb(nums):
    """Given list of numbers, return smallest & largest number as a tuple.

    I/P: List of numbers
    O/P: Tuple of range 

    >>> find_range_hb([3, 4, 2, 5, 10])
    (2, 10)
    >>> find_range_hb([43, 3, 44, 20, 2, 1, 100])
    (1, 100)
    >>> find_range_hb([])
    (None, None)
    >>> find_range_hb([7])
    (7, 7)

    """

    # START SOLUTION

    if len(nums) == 0:
        return (None, None)

    smallest = nums[0]
    largest = nums[0]

    for num in nums:
        if num < smallest:
            smallest = num
        elif num > largest:
            largest = num

    return (smallest, largest) 


if __name__ == "__main__": 

    import doctest 

    results = doctest.testmod()

    if results.failed == 0: 
        print("ALL TEST PASSED")
