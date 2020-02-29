# In this exercise, you’ll build a “polish notation calculator”.
# Polish notation is a different way to write an artithmetic expression. 
# For example, instead of writing 1 + 2 * 3, as we would in normal (“infix”) 
# style, we could write it with the operators to the left of their arguments. 
# This expression would become + 1 * 2 3. You can read a polish notation 
# expression backwards to see exactly what it does — in this case, multiply 2 
# times 3, and add that result to 1.
# Let’s make sure we have non-commutative operators (subtraction and division) 
# working:

def calc(s):
    """Evaluate expression.
        
        I/P: String 
        O/P: Number 

        >>> calc("+ 1 2")  # 1 + 2
        3
        >>> calc("* 2 + 1 2")  # 2 * (1 + 2)
        6
        >>> calc("+ 9 * 2 3")   # 9 + (2 * 3)
        15
        >>> calc("- 1 2")  # 1 - 2
        -1
        >>> calc("- 9 * 2 3")  # 9 - (2 * 3)
        3
        >>> calc("/ 6 - 4 2")  # 6 / (4 - 2)
        3

    """

    num1 = None 
    num2 = None 
    i = len(s) - 1 

    while i > -1 : 
        # Check if its a number and store it as an int 
        if s[i].isdigit() and num2 is None : 
            num2 = int(s[i]) 
        # Check if its a number and store it as an int 
        elif s[i].isdigit() and num1 is None : 
            num1 = int(s[i])

        # Check for valid math operations 
        elif s[i] == "+" : 
            num2 = num1 + num2 
            num1 = None 
        elif s[i] == "-" : 
            num2 = num1 - num2 
            num1 = None 
        elif s[i] == "*" : 
            num2 = num1 *  num2
            num1 = None 
        elif s[i] == "/" : 
            num2 = num1 / num2 
            num1 = None 
        elif s[i] == "%" : 
            num2 = num1 % num2 
            num1 = None 

        # Decrement the index counter and move to the previous index
        i -= 1 

    return int(num2)


def polish_calc_hb(s): 
    """Evaluate expression.
        
        I/P: String 
        O/P: Number 

        >>> polish_calc_hb("+ 1 2")  # 1 + 2
        3
        >>> polish_calc_hb("* 2 + 1 2")  # 2 * (1 + 2)
        6
        >>> polish_calc_hb("+ 9 * 2 3")   # 9 + (2 * 3)
        15
        >>> polish_calc_hb("- 1 2")  # 1 - 2
        -1
        >>> polish_calc_hb("- 9 * 2 3")  # 9 - (2 * 3)
        3
        >>> polish_calc_hb("/ 6 - 4 2")  # 6 / (4 - 2)
        3

    """

    # convert string into list of tokens
    tokens = s.split(" ")

    # Start with right-most number (in a well-formed polish notation
    # expression, it must ALWAYS end with a number)
    operand2 = int(tokens.pop())

    while tokens: 
        operand1 = int(tokens.pop())
        operator = tokens.pop()

        # Do the math and use the result as our "right-hand" value
        # for the next time we do math

        if operator == "+":
            operand2 = operand1 + operand2

        elif operator == "-":
            operand2 = operand1 - operand2

        elif operator == "*":
            operand2 = operand1 * operand2

        elif operator == "/":
            operand2 = operand1 // operand2

    return operand2 


if __name__ == "__main__": 

    import doctest 

    results = doctest.testmod() 

    if results.failed == 0: 
        print("ALL TESTS PASSED")




