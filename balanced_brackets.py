# Given a string, return True or False depending on whether the string’s 
# opening-and-closing marks (that is, brackets) are balanced. Account for the 
# following bracket types:
#    Type            Opener      Closer
#    Parentheses     (           )
#    Curly Braces    {           }
#    Square Brackets [           ]
#    Angle Brackets  <           >
# The string doesn’t need to have all four types of brackets, but if an open 
# bracket appears, the pair should also be closed correctly.
# Many of the same test cases from our Balanced Parentheses problem apply to this 
# expanded problem, with the caveat that they must check all types of brackets.
# case where the number of brackets opened matches the number closed, but in 
# the wrong order is False 
# If you receive a string with no brackets, consider it balanced:

class Stack(object): 
    """ Stack object to balance the brackets """

    def __init__(self): 
        """ Initialise an empty stack object """
        self._data = [] 

    def __repr__(self): 
        """ Print the top of the stack and its length """
        return "<Stack Tail = {tail}, Stack length = {length}>".format(
            tail = self._data[-1], length = len(self._data))

    def push(self, item): 
        """ Add item to the stack """
        self._data.append(item)

    def pop(self): 
        """ Remove and return item from the top of the stack """
        if self.is_empty(): 
            return None 
        else: 
            return self._data.pop()

    def is_empty(self): 
        """ Is the stack empty """
        return not bool(self._data)

    def empty(self): 
        """ Empty the stack """
        self._data = [] 

    def peek(self): 
        """ Return the element at the top of the stack """
        if self.is_empty(): 
            return None 
        else: 
            return self._data[-1]


def has_balanced_brackets(phrase):
    """Does a given string have balanced pairs of brackets?

        Given a string as input, return True or False depending on whether the
        string contains balanced (), {}, [], and/or <>.
        
        >>> has_balanced_brackets("<ok>")
        True
        >>> has_balanced_brackets("<[ok]>")
        True
        >>> has_balanced_brackets("<[{(yay)}]>")
        True
        >>> has_balanced_brackets("(Oops!){")
        False
        >>> has_balanced_brackets("{[[This has too many open square brackets.]}")
        False
        >>> has_balanced_brackets(">")
        False
        >>> has_balanced_brackets("(This has {too many} ) closers. )")
        False
        >>> has_balanced_brackets("<{Not Ok>}")
        False
        >>> has_balanced_brackets("No brackets here!")
        True

    """
    open_brackets = { "(", "{", "[", "<" }
    close_brackets = { ")", "}", "]", ">" }

    brack_tracker = Stack()

    for char in phrase: 
        if char in open_brackets: 
            brack_tracker.push(char)
        elif char in close_brackets: 
            # print(brack_tracker)
            
            if brack_tracker.is_empty(): 
                # print("Empty")
                return False
            else: 
                # print("Not empty ")
                bracket = brack_tracker.pop()
                # print(bracket)
                if char == ")" and bracket != "(": 
                    return False 
                elif char == "}" and bracket != "{": 
                    return False
                elif char == "]" and bracket != "[": 
                    return False
                elif char == ">" and bracket != "<": 
                    return False

    
    return brack_tracker.is_empty()


def has_balanced_brackets_hb(phrase):
    """Does a given string have balanced pairs of brackets?

        Given a string as input, return True or False depending on whether the
        string contains balanced (), {}, [], and/or <>.
        
        >>> has_balanced_brackets_hb("<ok>")
        True
        >>> has_balanced_brackets_hb("<[ok]>")
        True
        >>> has_balanced_brackets_hb("<[{(yay)}]>")
        True
        >>> has_balanced_brackets_hb("(Oops!){")
        False
        >>> has_balanced_brackets_hb("{[[This has too many open square brackets.]}")
        False
        >>> has_balanced_brackets_hb(">")
        False
        >>> has_balanced_brackets_hb("(This has {too many} ) closers. )")
        False
        >>> has_balanced_brackets_hb("<{Not Ok>}")
        False
        >>> has_balanced_brackets_hb("No brackets here!")
        True

    """

    # START SOLUTION

    closers_to_openers = {
                    ")" : "(", 
                    "}" : "{", 
                    "]" : "[", 
                    ">" : "<" }

    # Set of all opener characters; used to match openers quickly.
    openers = set(closers_to_openers.values())
    
    # Create an empty list to use as a stack.
    openers_seen = []

    for char in phrase: 

        # Push open brackets onto the stack.

        if char in openers: 
            openers_seen.append(char)
            # print("DDD")

        # For closers:
        #
        # - if nothing is open; fail fast
        # - if we are the twin of the most recent opener, pop & continue
        # - else we're the twin to a different opener; fail fast

        elif char in closers_to_openers:

            if openers_seen == []: 
                # print("CCC")
                return False 

            if openers_seen[-1] == closers_to_openers.get(char): 
                # print("AAA")
                openers_seen.pop()
            else: 
                # print("BBB")
                return False 

    # An empty stack means the brackts are balanced
    return openers_seen == [] 


if __name__ == "__main__": 

    import doctest 

    results = doctest.testmod()

    if results.failed == 0: 
        print("ALL TESTS PASSED")
