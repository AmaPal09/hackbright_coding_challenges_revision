# In this challenge, you’ll write a decoder.
# A valid code is a sequence of numbers and letters, always starting with a 
# number and ending with letter(s).
# Each number tells you how many characters to skip before finding a good letter. 
# After each good letter should come the next next number.
# For example, the string “hey” could be encoded by “0h1ae2bcy”. This means “skip 
# 0, find the ‘h’, skip 1, find the ‘e’, skip 2, find the ‘y’”.

def decode(s):
    """Decode a string.
        
        I/P: String 
        O/P: String 

        >>> decode("0h")
        'h'
        >>> decode("2abh")
        'h'
        >>> decode("0h1ae2bcy")
        'hey'
    """

    index_ctr = 0 
    coded_elem = None 
    decoded_lst = [] 

    while index_ctr < len(s): 
        coded_elem = s[index_ctr]
        index_ctr += 1 

        if coded_elem.isalpha(): 
            decoded_lst.append(coded_elem)    
        else: 
            index_ctr += int(coded_elem)

    return "".join(decoded_lst)


def decode_hb(s):
    """Decode a string.
        
        I/P: String 
        O/P: String 

        >>> decode_hb("0h")
        'h'
        >>> decode_hb("2abh")
        'h'
        >>> decode_hb("0h1ae2bcy")
        'hey'
    """

    word = ""

    i = 0 

    while i <len(s): 

        num_to_skip = int(s[i])

        i += num_to_skip+1 

        word += s[i]

        i += 1 

    return word 



if __name__ == "__main__": 

    import doctest 

    results = doctest.testmod() 

    if results.failed == 0: 
        print("ALL TESTS PASSED ")