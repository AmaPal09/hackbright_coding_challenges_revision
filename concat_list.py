# Given two lists. concatenate them (that is, combine them into a single list).
def concat_lists(list1, list2):
    """Combine lists.

        I/P: 2 lists 
        O/P 1 list 

        >>> concat_lists([1, 2], [3, 4])
        [1, 2, 3, 4]
        >>> concat_lists([], [1, 2])
        [1, 2]
        >>> concat_lists([1, 2], [])
        [1, 2]
        >>> concat_lists([], [])
        []
    """

    list_result = []
    list_result.extend(list1)
    list_result.extend(list2)
    return list_result
# Runtime O(n)
# Space O(n) [Can be done O(1)]


def concat_lists_2(list1, list2):
    """Combine lists.

        I/P: 2 lists 
        O/P 1 list 

        >>> concat_lists_2([1, 2], [3, 4])
        [1, 2, 3, 4]
        >>> concat_lists_2([], [1, 2])
        [1, 2]
        >>> concat_lists_2([1, 2], [])
        [1, 2]
        >>> concat_lists_2([], [])
        []
    """

    list1.extend(list2)

    return list1

# Runtime O(n)
# Space O(1)


def concat_lists_hb(list1, list2):
    """Combine lists.

        I/P: 2 lists 
        O/P 1 list 

        >>> concat_lists_hb([1, 2], [3, 4])
        [1, 2, 3, 4]
        >>> concat_lists_hb([], [1, 2])
        [1, 2]
        >>> concat_lists_hb([1, 2], [])
        [1, 2]
        >>> concat_lists_hb([], [])
        []
    """

    for item in list2: 
        list1.append(item)

    return list1

# Runtime O(n)
# Space O(1)


if __name__ == '__main__': 
    import doctest 

    result = doctest.testmod()

    if result.failed == 0: 
        print("ALL TEST PASSED")