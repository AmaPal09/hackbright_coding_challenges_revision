# Write a function, find_longest_word, that takes a list of words and returns the 
# length of the longest one.

def find_longest_word(words):
    """Return longest word in list of words. 

        I/P: List of strings
        O/P: Int

        >>> find_longest_word(["hi", "hello"])
        5

        >>> find_longest_word(["Balloonicorn", "Hackbright"])
        12

        >>> find_longest_word([""])
        0

        >>> find_longest_word([])
        0

        >>> find_longest_word(["temp", "care"])
        4

        >>> find_longest_word(["single"])
        6

    """

    if len(words) == 0: 
        return 0 

    max_length = 0 

    for word in words: 
        if len(word) > max_length: 
            max_length = len(word)

    return max_length


def find_longest_word_hb(words):
    """Return longest word in list of words. 

        I/P: List of strings
        O/P: Int

        >>> find_longest_word_hb(["hi", "hello"])
        5

        >>> find_longest_word_hb(["Balloonicorn", "Hackbright"])
        12

        >>> find_longest_word_hb([""])
        0

        >>> find_longest_word_hb([])
        0

        >>> find_longest_word_hb(["temp", "care"])
        4

        >>> find_longest_word_hb(["single"])
        6

    """ 

    if len(words) == 0: 
        return 0 

    return max(len(w) for w in words)


def find_longest_word_hb_2(words):
    """Return longest word in list of words. 

        I/P: List of strings
        O/P: Int

        >>> find_longest_word_hb_2(["hi", "hello"])
        5

        >>> find_longest_word_hb_2(["Balloonicorn", "Hackbright"])
        12

        >>> find_longest_word_hb_2([""])
        0

        >>> find_longest_word_hb_2([])
        0

        >>> find_longest_word_hb_2(["temp", "care"])
        4

        >>> find_longest_word_hb_2(["single"])
        6

    """ 

    if len(words) == 0: 
        return 0 
        
    return max(len(w) for w in words)


if __name__ == "__main__": 

    import doctest 

    results = doctest.testmod()

    if results.failed == 0: 
        print("ALL TESTS PASSED")


