# In this challenge, you should create a function that works like that built-in 
# Python .split() method 1.
# You may not use the split method in your solution!
# You may not use regular expressions in your solution!


def split(astring, splitter):
    """Split a string by splitter and return list of splits.


    >>> split("i love balloonicorn", " ")
    ['i', 'love', 'balloonicorn']

    >>> split("that is which is that which is that", " that ")
    ['that is which is', 'which is that']

    >>> split("that is which is that which is that", "that")
    ['', ' is which is ', ' which is ', '']

    >>> split("hello world", "nope")
    ['hello world']

    """

    w_str = 0 
    w_end = 0
    i = 0
    split_list = []
    w_storage = 0
    
    # print("Splitter: {}, length:{}".format(splitter, len(splitter)))

    while i < len(astring) : 
        
        if astring[i:i+len(splitter)] == splitter : 
            
            split_list.append(astring[w_str:w_end])

            i += len(splitter)
            w_str = i
            w_end = i
            
        else: 
            i += 1 
            w_end += 1 
            
    split_list.append(astring[w_str:w_end])

    return split_list


def split_hb(astring, splitter):
    """Split a string by splitter and return list of splits.


    >>> split_hb("i love balloonicorn", " ")
    ['i', 'love', 'balloonicorn']

    >>> split_hb("that is which is that which is that", " that ")
    ['that is which is', 'which is that']

    >>> split_hb("that is which is that which is that", "that")
    ['', ' is which is ', ' which is ', '']

    >>> split_hb("hello world", "nope")
    ['hello world']

    """
    out = []
    index = 0 

    while index < len(astring): 

        curr_index = index 
        index = astring.find(splitter, index)

        if index != -1: 
            out.append(astring[curr_index:index])
            index += len(splitter)
        else: 
            out.append(astring[curr_index:])
            break

    return out 


if __name__ == '__main__': 

    import doctest 

    results = doctest.testmod()

    if results.failed == 0: 
        print("ALL TESTS PASSED")
