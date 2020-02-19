# Given a word in English, return True if that word contains more vowels than 
# non-vowels; otherwise, return False. The word will always be a single word, 
# without any punctuation or spaces. It will contain only uppercase and 
# lowercase letters.

# If the phrase is over half vowels, it should return True:

def has_more_vowels(word):
    """Does word contain more vowels than non-vowels?
    
        I/P: String
        O/P: Binary

        >>> has_more_vowels("mice")
        False
        >>> has_more_vowels("graph")
        False
        >>> has_more_vowels("moose")
        True
        >>> has_more_vowels("yay")
        False
        >>> has_more_vowels("Aal")
        True
    """
    
    set_vowels = {'a', 'e','i','o','u'}
    
    ctr_vowels = 0 
    ctr_consonent = 0 

    for char in word: 
        if char.lower() in set_vowels: 
            ctr_vowels += 1 
        else: 
            ctr_consonent += 1 

    if ctr_vowels > ctr_consonent: 
        return True
    else: 
        return False


def has_more_vowels_hb(word):
    """Does word contain more vowels than non-vowels?
    
        I/P: String
        O/P: Binary

        >>> has_more_vowels_hb("mice")
        False
        >>> has_more_vowels_hb("graph")
        False
        >>> has_more_vowels_hb("moose")
        True
        >>> has_more_vowels_hb("yay")
        False
        >>> has_more_vowels_hb("Aal")
        True
    """


    lowercase_vowels = {'a', 'e', 'i', 'o', 'u'}

    vowel_count = 0

    for letter in word:

        if letter.lower() in lowercase_vowels:
            vowel_count = vowel_count + 1

    return vowel_count > (len(word) / 2)


if __name__ == '__main__': 
    import doctest 

    results = doctest.testmod()

    if results.failed == 0: 
        print("ALL TESTS PASSED")
