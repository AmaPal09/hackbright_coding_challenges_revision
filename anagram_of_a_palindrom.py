# Is the word an anagram of a palindrome?
# A palindrome is a word that reads the same forward and backwards (eg, “racecar”, 
#     “tacocat”). An anagram is a rescrambling of a word (eg for “racecar”, you 
#     could rescramble this as “arceace”).
# Determine if the given word is a re-scrambling of a palindrome.
# The word will only contain lowercase letters, a-z.
# Don’t Care If It’s Real
#     You don’t need to worry about whether it’s an actual English word or 
#     not—just whether a palindrome could be made of it.
#     For example, the word “bcbc” could be rearranged as “bccb”, so this should 
#     be true, even though “bccb” isn’t an actual English word.


def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?

        I/P: string 
        O/P: Binary

        >>> is_anagram_of_palindrome("a")
        True

        >>> is_anagram_of_palindrome("ab")
        False

        >>> is_anagram_of_palindrome("aab")
        True

        >>> is_anagram_of_palindrome("arceace")
        True

        >>> is_anagram_of_palindrome("arceaceb")
        False
    """ 


    char_count = {} 
    char_single = False 

    for char in word: 
        char_count[char] = char_count.get(char, 0) + 1
    # print(char_count)

    for count in char_count.values(): 
        # print(count)
        if count % 2 != 0: 
            # print(char_single)
            if char_single: 
                return False
            else: 
                char_single = True

    return True


def is_anagram_of_palindrome_hb(word):
    """Is the word an anagram of a palindrome?

        I/P: string 
        O/P: Binary

        >>> is_anagram_of_palindrome_hb("a")
        True

        >>> is_anagram_of_palindrome_hb("ab")
        False

        >>> is_anagram_of_palindrome_hb("aab")
        True

        >>> is_anagram_of_palindrome_hb("arceace")
        True

        >>> is_anagram_of_palindrome_hb("arceaceb")
        False
    """ 

    seen = {}

    for letter in word: 
        count = seen.get(letter, 0)
        seen[letter] = count + 1 

    seen_an_odd = False 

    for count in seen.values(): 
        if count % 2 != 0: 
            if seen_an_odd: 
                return False
            seen_an_odd = True

    return True


if __name__ == "__main__": 

    import doctest 

    results = doctest.testmod()

    if results.failed == 0: 
        print("ALL TESTS PASSED")