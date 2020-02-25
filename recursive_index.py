# Find the index of an item in a list using recursion.
# Given a list of items:
# You should have a function that returns the 0-based index of a sought item:
# If the item isn’t in the list, return None:

def recursive_search(needle, haystack):
    """Given list (haystack), return index (0-based) of needle in the list.

        Return None if needle is not in haystack.
        Do this with recursion. You MAY NOT USE A `for` OR `while` LOOP.

        I/P: string, list
        O/P: Int 

        >>> lst = ["hey", "there", "you"]
        >>> recursive_search("hey", lst)
        0
        >>> lst = ["hey", "there", "you"]
        >>> recursive_search("you", lst)
        2
        >>> lst = ["hey", "there", "you"]
        >>> recursive_search("porcupine", lst) is None
        True

    """
    # print("haystack", haystack)
    if haystack: 
        if haystack[-1] == needle: 
            # print("AAA")
            return len(haystack) - 1 
        else: 
            haystack.pop()
            return recursive_search(needle, haystack)
    else: 
        return None


def recursive_index_hb(needle, haystack):
    """Given list (haystack), return index (0-based) of needle in the list.
        Return None if needle is not in haystack.
        Do this with recursion. You MAY NOT USE A `for` OR `while` LOOP.

        I/P: string, list
        O/P: Int 

        >>> lst = ["hey", "there", "you"]
        >>> recursive_index_hb("hey", lst)
        0
        >>> recursive_index_hb("you", lst)
        2
        >>> recursive_index_hb("porcupine", lst) is None
        True

    """
    # START SOLUTION

    def _recursive_index(needle, haystack, start_at):

        # Check if not found (we've gone too far)
        if start_at == len(haystack): 
            return None 

        if haystack[start_at] == needle: 
            return start_at

        return _recursive_index(needle, haystack, start_at + 1)

    return _recursive_index(needle, haystack, 0 )


if __name__ == "__main__": 

    import doctest 

    results = doctest.testmod() 

    if results.failed == 0: 
        print("ALL TESTS PASSED ")

