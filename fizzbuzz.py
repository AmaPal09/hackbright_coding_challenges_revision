# Write a program that counts from 1 to 20 in fizzbuzz fashion.

# To do so, loop from 1 to 20 (inclusive). Each time through, if the number is 
# evenly divisible by 3, say ‘fizz’. If the number is evenly divisible by 5, 
# say ‘buzz’. If the number is evenly divisible by both 3 and 5, say ‘fizzbuzz’. 
# Otherwise, say the number.


def fizzbuzz():
    """Count from 1 to 20 in fizzbuzz fashion.

    I/P: No inpot 
    O/P: ints and strings
        >>> fizzbuzz()
        1
        2
        fizz
        4
        buzz
        fizz
        7
        8
        fizz
        buzz
        11
        fizz
        13
        14
        fizzbuzz
        16
        17
        fizz
        19
        buzz

    """

    for i in range(1,21): 
        if i%15 == 0: 
            print('fizzbuzz')
            continue
        if i%5 == 0: 
            print('buzz')
            continue
        if i%3 == 0: 
            print('fizz')
            continue
        print(i)


if __name__ == "__main__": 

    import doctest 

    results = doctest.testmod()

    if results.failed == 0: 
        print("ALL TEST PASSED")