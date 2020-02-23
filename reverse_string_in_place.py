# Given a string, return the same string, reversed.
# For example, as “porcupine” would reverse to “enipucrop”:

def rev_string(astring):
    """Return reverse of string.

        You may NOT use the reversed() function!
    
        >>> rev_string("porcupine")
        'enipucrop'
    """

    reversed_string = ''

    for char in astring[-1::-1]: 
        reversed_string += char

    return reversed_string


def rev_string_hb(astring):
    """Return reverse of string.

        You may NOT use the reversed() function!
    
        >>> rev_string_hb("porcupine")
        'enipucrop'
    """
    out = ""

    for i in range(len(astring), 0, -1): 
        out += astring[i - 1]

    return out 


def rev_string_2(astring):
    """Return reverse of string.

        You may NOT use the reversed() function!
    
        >>> rev_string_2("porcupine")
        'enipucrop'
    """

    return astring[::-1]


def rev_string_3(astring): 
    """Return reverse of string.

        You may NOT use the reversed() function!
    
        >>> rev_string_3("porcupine")
        'enipucrop'
    """

    if len(astring) == 0: 
        return astring 
    else: 
        return rev_string_3(astring[1:]) + astring[0]


class Stack(object): 
    """ Stack object to be used for revering the list """

    def __init__(self): 
        """ Initialise an empty stack """ 
        self._data = []

    def __repr__(self): 
        """ Print the stack """
        return "<Stack tail = {tail} and length = {length}>".format(
            tail = self._data[-1], length = len(self._data))

    def push(self, item): 
        """ Add item to the stack """
        self._data.append(item)

    def pop(self): 
        """ Remove item from the stack """
        return self._data.pop()

    def length(self): 
        """ Return length of the stack """
        return len(self._data)

    def peek(self): 
        """ Return item at the top of the stack """ 
        if self.is_empty(): 
            return None 
        else: 
            return self._data[-1]

    def empty(self): 
        """ Empty the stack """
        self._data = [] 

    def is_empty(self): 
        """ Is the stack empty """
        return not bool(self._data)


def rev_string_4(astring): 
    """Return reverse of string.

        You may NOT use the reversed() function!
    
        >>> rev_string_4("porcupine")
        'enipucrop'
    """

    reverse_stack = Stack()
    result_string = ''

    for char in astring: 
        reverse_stack.push(char)
    # print(reverse_stack._data)

    while not reverse_stack.is_empty(): 
        result_string += reverse_stack.pop()

    return result_string


# print(rev_string_4('hello')) 

if __name__ == '__main__': 

    import doctest 

    results = doctest.testmod()

    if results.failed == 0: 
        print("ALL TESTS PASSED")
