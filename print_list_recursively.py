# Print items from a list using recursion.

def print_recursively(lst):
    """Print items in the list, using recursion.
        
        I/P: List 
        O/P: Printed items
        >>> print_recursively([1, 2, 3])
        1
        2
        3
    """
    if lst:
        print(lst[0])
        print_recursively(lst[1:])


if __name__ == "__main__": 

    import doctest 

    results = doctest.testmod() 

    if results.failed == 0: 
        print("ALL TESTS PASSED ")




