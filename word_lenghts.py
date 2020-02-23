# Given a phrase, return dictionary keyed by word-length, with the value for each 
# length being the set of words of that length.
# Punctuation should be considered part of a word, so you only need to split the 
# string on whitespace:
# >>> answer = word_lengths("cute cats chase fuzzy rats")
# This should return {4: {'cute', 'cats', 'rats'}, 5: {'chase', 'fuzzy'}}, 
# but since both dictionaries and sets are unordered, we can’t just check if it 
# matches that exact string, so we’ll test more carefully:

def word_lengths(sentence):
    """Get dictionary of word-length: {words}.
        
        I/P: string 
        O/P: Dict of dict
        >>> answer = word_lengths("cute cats chase fuzzy rats")
        >>> sorted(answer.keys())
        [4, 5]
        >>> answer[4] == {'cute', 'cats', 'rats'}
        True
        >>> answer[5] == {'chase', 'fuzzy'}
        True

        >>> answer = word_lengths("Hi, I'm Balloonicorn")
        >>> sorted(answer.keys())
        [3, 12]
        >>> answer[3] == {'Hi,', "I'm"}
        True
        >>> answer[12] == {"Balloonicorn"}
        True
    """

    len_word_count = {} 

    for word in sentence.split(): 
        if len(word) not in len_word_count: 
            len_word_count[len(word)] = set()
        
        len_word_count[len(word)].add(word)

    return len_word_count


def word_lengths_hb(sentence):
    """Get dictionary of word-length: {words}.
        
        I/P: string 
        O/P: Dict of dict
        >>> answer = word_lengths_hb("cute cats chase fuzzy rats")
        >>> sorted(answer.keys())
        [4, 5]
        >>> answer[4] == {'cute', 'cats', 'rats'}
        True
        >>> answer[5] == {'chase', 'fuzzy'}
        True

        >>> answer = word_lengths_hb("Hi, I'm Balloonicorn")
        >>> sorted(answer.keys())
        [3, 12]
        >>> answer[3] == {'Hi,', "I'm"}
        True
        >>> answer[12] == {"Balloonicorn"}
        True
    """

    lenghts = {} 
    words = sentence.split()

    for word in words: 
        lenghts.setdefault(len(word), set()).add(word)

    return lenghts


if __name__ == "__main__": 

    import doctest 

    results = doctest.testmod()

    if results.failed == 0: 
        print("ALL TESTS PASSED")