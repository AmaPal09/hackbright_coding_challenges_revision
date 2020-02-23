# Write a function to turn a phrase into Pig Latin.
# Your function will be given a phrase (of one or more space-separated words). 
# There will be no punctuation in it. You should turn this into the same phrase in 
# Pig Latin.

# Rules
# If the word begins with a consonant (not a, e, i, o, u), move the first letter 
# to the end and add ‘ay’
# If the word begins with a vowel, add ‘yay’ to the end


def pig_latin(phrase):
    """Turn a phrase into pig latin.
        There will be no uppercase letters or punctuation in the phrase.

        I/P: String 
        O/P: String 

        >>> pig_latin('hello awesome programmer')
        'ellohay awesomeyay rogrammerpay'

        >>> pig_latin('porcupines are cute')
        'orcupinespay areyay utecay'

        >>> pig_latin('give me an apple')
        'ivegay emay anyay appleyay'

    """
    phrase_list = phrase.strip().split(" ")
    vowel_set = {'a', 'e', 'i', 'o','u'}

    pig_latin_list = []

    for word in phrase_list: 
        if word.lower()[0] in vowel_set: 
            pig_latin_list.append((word+'yay'))
        elif word.lower()[0] not in vowel_set: 
            pig_latin_list.append((word[1:]+word[0]+'ay'))
        else: 
            print("Some error")

    return " ".join(pig_latin_list)


def pig_latin_word_hb(word): 
    """Turn a word into the pig latin version.
            
            I/P: String
            O/P: String

            >>> pig_latin_word_hb('porcupine')
            'orcupinepay'

            >>> pig_latin_word_hb('apple')
            'appleyay'
    """

    if word[0] in 'aeiou': 
        return word + 'yay'
    else: 
        return word[1:] + word[0] + 'ay' 


def pig_latin_hb(phrase):
    """Turn a phrase into pig latin.
        There will be no uppercase letters or punctuation in the phrase.

        I/P: String 
        O/P: String 

        >>> pig_latin_hb('hello awesome programmer')
        'ellohay awesomeyay rogrammerpay'

        >>> pig_latin_hb('porcupines are cute')
        'orcupinespay areyay utecay'

        >>> pig_latin_hb('give me an apple')
        'ivegay emay anyay appleyay'

    """
    words = phrase.split(" ")

    pl_words = [pig_latin_word_hb(word) for word in words]

    return " ".join(pl_words)


if __name__ == '__main__': 

    import doctest 

    results = doctest.testmod()

    if results.failed == 0: 
        print("ALL TESTS PASSED")

