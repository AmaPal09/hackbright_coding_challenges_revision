# A pangram is a sentence that contains all the letters of the English alphabet at 
# least once, like “The quick brown fox jumps over the lazy dog.”
# Write a function to check a sentence to see if it is a pangram or not.

def is_pangram(sentence):
    """Given a string, return True if it is a pangram, False otherwise.

        I/P: String 
        O/P: Binary 

        >>> is_pangram("The quick brown fox jumps over the lazy dog!")
        True

        >>> is_pangram("I like cats, but not mice")
        False

    """

    char_set = set()

    for char in sentence: 
        if char.isalpha(): 
            char_set.add(char.lower())

    return len(char_set) == 26


def is_pangram_hb(sentence):
    """Given a string, return True if it is a pangram, False otherwise.

        I/P: String 
        O/P: Binary 

        >>> is_pangram_hb("The quick brown fox jumps over the lazy dog!")
        True

        >>> is_pangram_hb("I like cats, but not mice")
        False

    """

    used = {char.lower() for char in sentence if char.isalpha()}

    return len(used) == 26


if __name__ == '__main__': 

    import doctest 

    results = doctest.testmod()

    if results.failed == 0: 
        print("ALL TESTS PASSED")


