# Given an integer, print each digit in reverse order, starting with the ones 
# place.
# For example, if you were given 1 you should simply print 1, if given 314 you 
# should print 4, 1, 3, and if given 12 you should print 2, 1:

def print_digits(num):
    """Given int, print digits in reverse order, starting with the ones place.
       
        I/P: Int 
        O/P: Ints 

        >>> print_digits(1)
        1
        >>> print_digits(314)
        4
        1
        3
        >>> print_digits(12)
        2
        1
    """
    
    while num != 0: 
        print(num % 10)
        num = int((num - (num % 10)) / 10 ) 


if __name__ == "__main__": 

    import doctest 

    results = doctest.testmod() 

    if results.failed == 0: 
        print("ALL TESTS PASSED ")
