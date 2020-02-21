# Define a function max_of_three that takes in three numbers as arguments and 
# returns the largest of them.

def max_of_three(num1, num2, num3):
    """Returns the largest of three integers

        I/P: 3 Ints 
        O/P: Int 
        >>> max_of_three(1, 5, 2)
        5

        >>> max_of_three(10, 1, 11)
        11

        >>> max_of_three(-19, -55, -300)
        -19

        >>> max_of_three(3, 3, 3)
        3

"""
    
    if (num1 >= num2 and num1 >= num3): 
        return num1 
    elif (num2 >= num1 and num2 >= num3): 
        return num2 
    else: 
        return num3 


def max_of_three_hb(num1, num2, num3):
    """Returns the largest of three integers

        I/P: 3 Ints 
        O/P: Int 
        >>> max_of_three_hb(1, 5, 2)
        5

        >>> max_of_three_hb(10, 1, 11)
        11

        >>> max_of_three_hb(-19, -55, -300)
        -19

        >>> max_of_three_hb(3, 3, 3)
        3

"""
    if num1 >= num2 and num1 >= num3: 
        return num1
    elif num2 >= num1 and num2 >= num3: 
        return num2 
    elif num3 >= num1 and num3 >= num2: 
        return num3 
    else: 
        print("something went wrong")


if __name__ == "__main__": 
    
    import doctest 

    results = doctest.testmod()

    if results.failed == 0: 
        print("ALL TESTS PASSED")

