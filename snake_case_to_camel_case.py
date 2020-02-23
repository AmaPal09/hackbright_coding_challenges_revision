# Python programmers write variable names in snake_case, where each word is 
# lowercased and joined by underscores. JavaScript programmers write variable 
# names in camelCase, where the initial word is lowercase, and other words are 
# capitalized and jammed together.
# Given a variable name in snake_case, return a string with that variable name 
# written in camelCase.

def snake_to_camel(variable_name):
    """Given a variable name in snake_case, return camelCase of name.

        I/P: String 
        O/P: String 
        >>> snake_to_camel("hi_balloonicorn")
        'hiBalloonicorn'
    """

    snake_case_list = variable_name.strip().split("_")

    camel_case_list = []

    for i in range(len(snake_case_list)): 
        if i == 0: 
            camel_case_list.append(snake_case_list[0])
            continue
        camel_case_list.append((
                        snake_case_list[i][0].upper()+snake_case_list[i][1:]
                        ))

    return "".join(camel_case_list)


def snake_to_camel_hb(variable_name):
    """Given a variable name in snake_case, return camelCase of name.

        I/P: String 
        O/P: String 
        >>> snake_to_camel_hb("hi_balloonicorn")
        'hiBalloonicorn'
    """

    words = variable_name.split("_")

    for i in range(1, len(words)):
        words[i] = words[i].capitalize()

    return "".join(words)


if __name__ == "__main__": 

    import doctest 

    results = doctest.testmod()

    if results.failed == 0: 
        print("ALL TESTS PASSED")