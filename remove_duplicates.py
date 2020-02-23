# In this challenge, you’ll write a function that is given a list of items and 
# returns a new list of those items, in the same order, but with duplicate removed.

# Keep items in the order where they first appeared:
# A list with no duplicates would return the same:
# This should return a new list, not mutate the existing list:
# An empty list should return an empty list:

def deduped(items):
    """Return new list from items with duplicates removed.

        I/P: List 
        O/P: List 

        >>> deduped([1, 1, 1])
        [1]
        >>> deduped([1, 2, 1, 1, 3])
        [1, 2, 3]
        >>> deduped([1, 2, 3])
        [1, 2, 3]
        >>> a = [1, 2, 3]
        >>> b = deduped(a)
        >>> a == b
        True
        >>> a is b
        False
        >>> deduped([])
        []
    """

    items_set = set(items)
    deduped_list = []

    for item in items: 
        if item in items_set: 
            deduped_list.append(item)
            items_set.remove(item)

    return deduped_list


def deduped_hb(items):
    """Return new list from items with duplicates removed.

        I/P: List 
        O/P: List 

        >>> deduped_hb([1, 1, 1])
        [1]
        >>> deduped_hb([1, 2, 1, 1, 3])
        [1, 2, 3]
        >>> deduped_hb([1, 2, 3])
        [1, 2, 3]
        >>> a = [1, 2, 3]
        >>> b = deduped_hb(a)
        >>> a == b
        True
        >>> a is b
        False
        >>> deduped_hb([])
        []
    """

    seen = set()

    results_list = [] 

    for item in items: 
        if item not in results_list: 
            results_list.append(item)
            seen.add(item)

    return results_list


if __name__ == '__main__': 

    import doctest

    results = doctest.testmod()

    if results.failed == 0: 
        print("ALL TESTS PASSED")
