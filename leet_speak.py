# Leet speak in which standard letters are often replaced by numerals or special 
# characters.
# Letter        Becomes
# a             @
# o             0
# e             3
# l             1
# s             5
# t             7
# In this exercise, you’ll make a function that translate a word to leet-speak:

def translate_leet(phrase):
    """Translates input into "leet-speak

        I/P: String 
        O/P: String

        >>> translate_leet("Hi Balloonicorn")
        'Hi B@1100nic0rn'

        >>> translate_leet("Hackbright is the Shizzle")
        'H@ckbrigh7 i5 7h3 5hizz13'

        >>> translate_leet("")
        ''
    """

    leet_dict = {'a': '@',
                'o': '0', 
                'e': '3', 
                'l': '1', 
                's': '5',
                't': '7'
                }

    translated_phrase = ""

    for char in phrase: 
        if char.lower() in leet_dict: 
            translated_phrase += leet_dict[char.lower()]
        else: 
            translated_phrase += char 

    return translated_phrase
# Runtime is O(n^2) - 
# Reason being, we are adding a new char every time to a string, 
# and as strings are immutable in Python, what is actually happening in the background 
# is that we are building up a new string everytime in the backgroud and increasing 
# its length. 


def translate_leet_hb(phrase):
    """Translates input into "leet-speak

        I/P: String 
        O/P: String

        >>> translate_leet_hb("Hi Balloonicorn")
        'Hi B@1100nic0rn'

        >>> translate_leet_hb("Hackbright is the Shizzle")
        'H@ckbrigh7 i5 7h3 5hizz13'

        >>> translate_leet_hb("")
        ''
    """

    translated = ""

    leet_speak = {
        'a': '@',
        'o': '0',
        'e': '3',
        'l': '1',
        's': '5',
        't': '7',
    }

    for char in phrase: 
        translated += leet_speak.get(char.lower(), char)

    return translated


if __name__ == "__main__": 
    
    import doctest 

    results = doctest.testmod()

    if results.failed == 0: 
        print("ALL TESTS PASSED")
