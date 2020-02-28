# Given a string, return a new string that is the original string, reversed. 
# Do this with recursion, not a for loop.
# For example, as “porcupine” would reverse to “enipucrop”:

def rev_string(astring):
    """Return reverse of string using recursion.

        You may NOT use the reversed() function!

        >>> rev_string("porcupine")
        'enipucrop'
    """

    if len(astring) == 0: 
        return astring
    else: 
        return rev_string(astring[1:]) + astring[0]


if __name__ == "__main__": 

    import doctest 

    results = doctest.testmod()

    if results.failed == 0: 
        print("ALL TESTS PASSED")

