import time 
import math 

# Write a function the returns True or False, depending on whether the integer 
# passed into it is a prime number.
# Only numbers >1 can be prime numbers:
# Any number >1 that has no divisors other than 1 and itself is a prime number:

def is_prime(num):
    """Is a number a prime number?
        
        I/P: Int 
        O/P: Binary 

        >>> is_prime(0)
        False
        >>> is_prime(1)
        False
        >>> is_prime(2)
        True
        >>> is_prime(3)
        True
        >>> is_prime(4)
        False
        >>> is_prime(11)
        True
        >>> is_prime(999)
        False
        >>> is_prime(-44)
        False
    """

    if num < 2: 
        return False 

    test_divisor = 2

    while test_divisor < num: 
        if ((num % test_divisor == 0) and 
            (test_divisor != num)): 
            return False 
        test_divisor += 1 

    return True

def is_prime_hb(num):
    """Is a number a prime number?
        
        I/P: Int 
        O/P: Binary 

        >>> is_prime_hb(0)
        False
        >>> is_prime_hb(1)
        False
        >>> is_prime_hb(2)
        True
        >>> is_prime_hb(3)
        True
        >>> is_prime_hb(4)
        False
        >>> is_prime_hb(11)
        True
        >>> is_prime_hb(999)
        False
        >>> is_prime_hb(-44)
        False
    """

    if num < 2: 
        return False 

    for n in range(2, num): 
        if num % n == 0: 
            return False

    return True


def is_prime_2(num):
    """Is a number a prime number?
        
        I/P: Int 
        O/P: Binary 

        >>> is_prime_2(0)
        False
        >>> is_prime_2(1)
        False
        >>> is_prime_2(2)
        True
        >>> is_prime_2(3)
        True
        >>> is_prime_2(4)
        False
        >>> is_prime_2(11)
        True
        >>> is_prime_2(999)
        False
        >>> is_prime_2(-44)
        False
    """
    if num <= 1: 
        return False 
    if num == 2: 
        return True
    if num % 2 == 0: 
        return False 

    #We will check only for odd numbers as all even numbers other than 2 are 
    # not prime and this will reduce the execution time 
    for n in range(3, num, +2):
        if num % n == 0: 
            return False 

    return True


def is_prime_3(num):
    """Is a number a prime number?
        
        I/P: Int 
        O/P: Binary 

        >>> is_prime_3(0)
        False
        >>> is_prime_3(1)
        False
        >>> is_prime_3(2)
        True
        >>> is_prime_3(3)
        True
        >>> is_prime_3(4)
        False
        >>> is_prime_3(11)
        True
        >>> is_prime_3(999)
        False
        >>> is_prime_3(-44)
        False
    """

    if num <= 1: 
        return False
    if num == 2: 
        return True
    if num % 2 == 0: 
        return False 

    # Reduce the number of divisors we need to check by checking for divisibility
    # only upto the square root/square root +1 (when not a perfect square) of the 
    # number. 
    # Using math function sqrt to get the square root 
    # Using math function floor to consider only the interger part of the square
    # root 
    max_divisor = math.floor(math.sqrt(num))

    for n in range(3, max_divisor +1 , +2):
        if num % n == 0: 
            return False

    return True


def main(): 
    """ Main function used to call and time all above functions """ 

    t0 = time.time()
    c = 0 
    for n in range(1,1000): 
        x = is_prime(n)
        c += x
    print("Total prime numbers in the range [with func 1]:", c)
            t1 = time.time()
    print("Time required: ", t1 - t0)

    t0 = time.time()
    c = 0 
    for n in range(1,1000): 
        x = is_prime_hb(n)
        c += x
    print("Total prime numbers in the range [with func 2]:", c)
    t1 = time.time()
    print("Time required: ", t1 - t0)

    t0 = time.time()
    c = 0 
    for n in range(1,1000): 
        x = is_prime_2(n)
        c += x
    print("Total prime numbers in the range [with func 3]:", c)
    t1 = time.time()
    print("Time required: ", t1 - t0)

    t0 = time.time()
    c = 0 
    for n in range(1,1000): 
        x = is_prime_3(n)
        c += x
    print("Total prime numbers in the range [with func 4]:", c)
    t1 = time.time()
    print("Time required: ", t1 - t0)


if __name__ == '__main__': 
    import doctest 

    results = doctest.testmod()

    if results.failed == 0: 
        print("ALL TESTS PASSED")

    main() 