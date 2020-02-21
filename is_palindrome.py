# Return True/False if this word is a palindrome. A palindrome is a word that is
 # spelled the same backwards and forwards.
# Treat spaces and uppercase letters normally—so “Racecar” wouldn’t be a 
# palindrome since “R” and “r” aren’t the same letter:

def is_palindrome(word):
    """Return True/False if this word is a palindrome.
        
        I/P: strg
        O/P: Binary 

        >>> is_palindrome("a")
        True
        
        >>> is_palindrome(" ")
        True

        >>> is_palindrome("noon")
        True

        >>> is_palindrome("racecar")
        True

        >>> is_palindrome("porcupine")
        False

        >>> is_palindrome("Racecar")
        False

    """

    word_len = len(word)
    
    if word_len <= 1: 
        return True

    f_ctr = 0 
    b_ctr = word_len - 1 


    while f_ctr < b_ctr:
        
        if word[f_ctr] != word[b_ctr]: 
            return False 
        f_ctr += 1 
        b_ctr -= 1 

    return True


def is_palindrome_hb(word):
    """Return True/False if this word is a palindrome.
        
        I/P: strg
        O/P: Binary 

        >>> is_palindrome_hb("a")
        True

        >>> is_palindrome_hb(" ")
        True

        >>> is_palindrome_hb("noon")
        True

        >>> is_palindrome_hb("racecar")
        True

        >>> is_palindrome_hb("porcupine")
        False

        >>> is_palindrome_hb("Racecar")
        False

    """

    for i in range(len(word)//2): 
        if word[i] != word[-i-1]: 
            return False

    return True 


def is_palindrome_2(word):
    """Return True/False if this word is a palindrome.
        
        I/P: strg
        O/P: Binary 

        >>> is_palindrome_2("a")
        True

        >>> is_palindrome_2(" ")
        True

        >>> is_palindrome_2("noon")
        True

        >>> is_palindrome_2("racecar")
        True

        >>> is_palindrome_2("porcupine")
        False

        >>> is_palindrome_2("Racecar")
        False

    """

    return word == word[::-1]


if __name__ == "__main__": 
    
    import doctest 

    results = doctest.testmod()

    if results.failed == 0: 
        print("ALL TESTS PASSED")

    


