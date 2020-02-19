# Given a word, return True if that word contains only unique characters. 
# Return False otherwise.
# Uppercase and lowercase letters should be considered separately:

def has_unique_chars(word):
    """Does word contains unique set of characters?
    
        I/P: String
        O/P: Binary 

        >>> has_unique_chars("Monday")
        True

        >>> has_unique_chars("Moonday")
        False

        >>> has_unique_chars("")
        True
        
        >>> has_unique_chars("Bob")
        True

    """

    set_char = set()

    for char in word: 
        if char in set_char: 
            return False 
        else: 
            set_char.add(char)

    return True
#Runtime O(n)


def has_unique_chars_hb(word): 
    """Does word contains unique set of characters?
    
        I/P: String
        O/P: Binary 

        >>> has_unique_chars_hb("Monday")
        True

        >>> has_unique_chars_hb("Moonday")
        False

        >>> has_unique_chars_hb("")
        True
        
        >>> has_unique_chars_hb("Bob")
        True

    """

    set_word = set(word)

    return len(set_word) == len(word)
# Runtime O(n)


if __name__ == '__main__': 
    import doctest 

    results = doctest.testmod()

    if results.failed == 0: 
        print("ALL TESTS PASSED")

