# Compute the sum of a list of numbers.

def sum_list(num_list):
    """Return the sum of all numbers in list.
        
        I/P: List 
        O/P: Int 

        >>> sum_list([5, 3, 6, 2, 1])
        17
    """

    sum_out = 0 

    for num in num_list: 
        sum_out += num

    return sum_out


def sum_list_2(num_list):
    """Return the sum of all numbers in list.
        
        I/P: List 
        O/P: Int 

        >>> sum_list_2([5, 3, 6, 2, 1])
        17
    """

    return sum(num_list)


def sum_list_3(num_list):
    """Return the sum of all numbers in list.
        
        I/P: List 
        O/P: Int 

        >>> sum_list_3([5, 3, 6, 2, 1])
        17
    """

    return sum(num for num in num_list) 


if __name__ == "__main__": 

    import doctest 

    results = doctest.testmod()

    if results.failed == 0: 
        print("ALL TESTS PASSED")

