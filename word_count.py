# Given a phrase, print (not return) the word count in ascending order.
# If there is a tie for a count, make sure the words are printed in ascending order 
# within the tie
# Capitalized words are considered distinct


def word_count(phrase):
    """Count words in a sentence, and print in ascending order.

        I/P: String 
        O/P: Items of a dict 

        >>> word_count("berry cherry cherry cherry berry apple")
        apple: 1
        berry: 2
        cherry: 3

        >>> word_count("hey hi hello")
        hello: 1
        hey: 1
        hi: 1

        >>> word_count("hi Hi hi")
        Hi: 1
        hi: 2

    """

    word_count = {} 
    phrase_list = phrase.strip().split(" ")

    for word in phrase_list: 
        word_count[word] = word_count.get(word, 0) + 1 

    counts = []

    for word, count in word_count.items(): 
        counts.append((count, word))

    counts.sort()

    for count, word in counts: 
        print("{w}: {c}".format(w=word, c=count))


def word_count_hb(phrase):
    """Count words in a sentence, and print in ascending order.

        I/P: String 
        O/P: Items of a dict 

        >>> word_count_hb("berry cherry cherry cherry berry apple")
        apple: 1
        berry: 2
        cherry: 3

        >>> word_count_hb("hey hi hello")
        hello: 1
        hey: 1
        hi: 1

        >>> word_count_hb("hi Hi hi")
        Hi: 1
        hi: 2

    """

    word_count = {} 
    
    for word in phrase.split(): 
        word_count[word] = word_count.get(word, 0) + 1

    counts = [(count, word) for word, count in word_count.items()]

    counts.sort() 

    for count, word in counts: 
        print("%s: %s" % (word, count))


if __name__ == "__main__": 

    import doctest 

    results = doctest.testmod()

    if results.failed == 0: 
        print("ALL TESTS PASSED")