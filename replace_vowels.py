# Given list of chars, return a new copy, but with vowels replaced by *.
# An empty list should return an empty list:
# Make sure to handle uppercase:
# Do not consider y a vowel:

def replace_vowels(chars):
    """Given list of chars, return a new copy, but with vowels replaced by '*'.

        I/P: List 
        O/P: List 

        >>> replace_vowels(['h', 'i'])
        ['h', '*']

        >>> replace_vowels(['o', 'o', 'o'])
        ['*', '*', '*']

        >>> replace_vowels(['z', 'z', 'z'])
        ['z', 'z', 'z']

        >>> replace_vowels([])
        []

        >>> replace_vowels(["A", "b"])
        ['*', 'b']

        >>> replace_vowels(["y", "a", "y"])
        ['y', '*', 'y']
    """

    vowel_set = {'a', 'e', 'i', 'o', 'u'}
    new_chars = []

    for char in chars: 
        if char.lower() in vowel_set: 
            new_chars.append('*')
        else: 
            new_chars.append(char)

    return new_chars


def replace_vowels_hb(chars):
    """Given list of chars, return a new copy, but with vowels replaced by '*'.

        I/P: List 
        O/P: List 

        >>> replace_vowels_hb(['h', 'i'])
        ['h', '*']

        >>> replace_vowels_hb(['o', 'o', 'o'])
        ['*', '*', '*']

        >>> replace_vowels_hb(['z', 'z', 'z'])
        ['z', 'z', 'z']

        >>> replace_vowels_hb([])
        []

        >>> replace_vowels_hb(["A", "b"])
        ['*', 'b']

        >>> replace_vowels_hb(["y", "a", "y"])
        ['y', '*', 'y']
    """

    vowels = {'a', 'e', 'i', 'o', 'u'}
    new = []

    for char in chars: 

        if char.lower() in vowels: 
            char = '*'

        new.append(char)

    return new


if __name__ == '__main__': 

    import doctest 

    results = doctest.testmod()

    if results.failed == 0: 
        print("ALL TESTS PASSED")

