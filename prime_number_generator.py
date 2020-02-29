# A prime number is a number >= 2 that is only evenly divisible by itself and 1.
# So, for example, 3 is a prime number but 4 (divisible by 2) is not. The first 
# few primes are: 2, 3, 5, 7, 11.

# Write a function that produces count prime numbers, where count is a value 
# passed into the function.

def is_prime(number): 
    """ Is the number a prime number """

    if number <=1 : 
        return False 
    elif number == 2 : 
        return True 
    elif number % 2 == 0 :
        return False 

    for n in range(3, number, 2) :
        if number % n == 0: 
            return False 

    return True 


def primes(count):
    """Return count number of prime numbers, starting at 2.
    
        I/P: Int 
        O/P: List 
        >>> primes(1)
        [2]

        >>> primes(5)
        [2, 3, 5, 7, 11]

    """
    prime_list = []
    number = 2 

    if count < 1: 
        return prime_list

    while len(prime_list) < count : 
        print(number)
        if is_prime(number) : 
            prime_list.append(number)
            print(prime_list)
        #     number += 1 
        # else: 
        number += 1 

    return prime_list


def primes_hb(count):
    """Return count number of prime numbers, starting at 2.
    
        I/P: Int 
        O/P: List 
        >>> primes_hb(1)
        [2]

        >>> primes_hb(5)
        [2, 3, 5, 7, 11]
    """

    primes = [] 
    num = 2 

    while count > 0: 
        if is_prime_hb(num): 
            primes.append(num)
            count -= 1 
        num += 1 

    return primes 


def is_prime_hb(num):
    """Is num a prime number?

    num will always be a positive integer.

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

    >>> is_prime_hb(7)
    True

    >>> is_prime_hb(25)
    False
    """ 
    assert num >= 0 

    if num < 2 : 
        return False 

    if num == 2 : 
        return True 

    if num % 2 == 0 : 
        return False 

    n = 3 

    while n * n <= num : 
        if num % n == 0: 
            return False 
        n += 2 

    return True 


# if __name__ == "__main__" : 
    
#     import doctest 

#     results = doctest.testmod()

#     if results.failed == 0 : 
#         print("ALL TESTS PASSED")
