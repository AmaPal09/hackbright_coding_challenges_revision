# Given a string, return True or False depending on whether that string has 
# balanced parentheses.
# For the purposes of this problem, you only need to worry about parentheses 
# (( and )), not other opening-and-closing marks, like curly brackets, square 
# brackets, or angle brackets.
# You may consider a string with no parentheses balanced:

def has_balanced_parens(phrase):
    """Does a string have balanced parentheses?

        I/P: String 
        O/P: Boolean 

        >>> has_balanced_parens("()")
        True

        >>> has_balanced_parens("(Oh Noes!)(")
        False

        >>> has_balanced_parens("((There's a bonus open paren here.)")
        False

        >>> has_balanced_parens(")")
        False

        >>> has_balanced_parens("(")
        False

        >>> has_balanced_parens("(This has (too many closes.) ) )")
        False

        >>> has_balanced_parens("Hey...there are no parens here!")
        True

    """

    paren_dict = {
            "open": 0,
            "close": 0 
            } 

    for char in phrase: 
        if char == "(": 
            paren_dict["open"] += 1
        elif char == ")": 
            paren_dict["close"] += 1 
        else: 
            continue 

    if paren_dict["open"] == paren_dict["close"]: 
        return True 
    else: 
        return False 


def has_balanced_parens_2(phrase):
    """Does a string have balanced parentheses?

        I/P: String 
        O/P: Boolean 

        >>> has_balanced_parens_2("()")
        True

        >>> has_balanced_parens_2("(Oh Noes!)(")
        False

        >>> has_balanced_parens_2("((There's a bonus open paren here.)")
        False

        >>> has_balanced_parens_2(")")
        False

        >>> has_balanced_parens_2("(")
        False

        >>> has_balanced_parens_2("(This has (too many closes.) ) )")
        False

        >>> has_balanced_parens_2("Hey...there are no parens here!")
        True

    """        

    paren_ctr = 0 

    for char in phrase: 
        if char == "(": 
            paren_ctr += 1 
        elif char == ")": 
            paren_ctr -= 1 
        else: 
            continue

    if paren_ctr == 0: 
        return True 
    else: 
        return False 


def has_balanced_parens_hb(phrase):
    """Does a string have balanced parentheses?

        I/P: String 
        O/P: Boolean 

        >>> has_balanced_parens_hb("()")
        True

        >>> has_balanced_parens_hb("(Oh Noes!)(")
        False

        >>> has_balanced_parens_hb("((There's a bonus open paren here.)")
        False

        >>> has_balanced_parens_hb(")")
        False

        >>> has_balanced_parens_hb("(")
        False

        >>> has_balanced_parens_hb("(This has (too many closes.) ) )")
        False

        >>> has_balanced_parens_hb("Hey...there are no parens here!")
        True

    """        

    # START SOLUTION

    parens = 0

    for char in phrase:

        if char == "(":
            parens = parens + 1

        elif char == ")":
            parens = parens - 1

            if parens < 0:
                # We can never close more than we have open
                return False

    # Make sure we have none left

    if parens > 0:
        return False

    else:
        return True


class Stack(object): 
    """ Object used for balancing paranthesis """

    def __init__(self): 
        """ Initialise an empty stack """
        self._data = [] 

    def __repr__(self):
        """ Print the element at the top of the stack""" 
        return "<Stack tail = {tail}, Stack length = {length}>".format(
            tail= self._data[-1], length= len(self._data)
            )

    def push(self, item): 
        """ Add item to the top of the stack """
        self._data.append(item)

    def pop(self): 
        """ Remove the element from the top of the stack """
        self._data.pop()

    def length(self): 
        """ Return the length of the stack """
        return len(self._data)

    def is_empty(self): 
        """ Is the stack empty """
        return not bool(self._data) 

    def empty(self): 
        """ Empty the stack """
        self._data = []

    def peek(self): 
        """ Return the item at the top of the stack """
        if self.is_empty(): 
            return None 
        else: 
            return self._data[-1 ]


def has_balanced_parens_3(phrase):
    """Does a string have balanced parentheses?

        I/P: String 
        O/P: Boolean 

        >>> has_balanced_parens_3("()")
        True

        >>> has_balanced_parens_3("(Oh Noes!)(")
        False

        >>> has_balanced_parens_3("((There's a bonus open paren here.)")
        False

        >>> has_balanced_parens_3(")")
        False

        >>> has_balanced_parens_3("(")
        False

        >>> has_balanced_parens_3("(This has (too many closes.) ) )")
        False

        >>> has_balanced_parens_3("Hey...there are no parens here!")
        True

    """                    

    parens_stack = Stack()

    for char in phrase: 
        if char == "(": 
            parens_stack.push(char)
        elif char == ")": 
            if parens_stack.is_empty(): 
                return False 
            else: 
                parens_stack.pop()

    # if parens_stack.is_empty(): 
    #     return True
    # else: 
    #     return False 
    return parens_stack.is_empty()


if __name__ == "__main__": 

    import doctest 

    results = doctest.testmod()

    if results.failed == 0: 
        print("ALL TESTS PASSED")
