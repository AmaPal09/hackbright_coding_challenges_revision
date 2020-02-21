# Find the largest integer in a list of integers.

def max_num(num_list):
    """Returns largest integer from given list
        
        I/P: List of ints 
        O/P: Int 

        >>> max_num([5, 3, 6, 2, 1])
        6
        
        >>> max_num([]) is None
        True
    """

    if len(num_list) == 0: 
        return None

    max_n = 0
    for n in num_list: 
        if max_n < n: 
            max_n = n 

    return max_n


def max_num(num_list):
    """Returns largest integer from given list
        
        I/P: List of ints 
        O/P: Int 

        >>> max_num([5, 3, 6, 2, 1])
        6
        
        >>> max_num([]) is None
        True
    """

    if len(num_list) == 0: 
        return None

    return max(num_list)




if __name__ == "__main__": 
    
    import doctest 

    results = doctest.testmod()

    if results.failed == 0: 
        print("ALL TESTS PASSED")

