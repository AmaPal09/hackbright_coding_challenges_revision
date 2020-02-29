# Hexadecimal is a numbering system that uses base 16, rather than the base 10 
# of our normal numbering system. Therefore, there are digits from 0-9 and A-F. 
# (Hexadecimal is an important concept in computer science, and you can learn 
#     more about it at the Wikipedia article about hexadecimal)

# Write a function that, when given a hexadecimal number as a string, returns 
# the equivalent decimal value.

def hex_convert(hex_in):
    """Convert a hexadecimal string, like '1A', into it's decimal equivalent.
        
        I/P: String 
        O/P: Int 
        >>> hex_convert('6')
        6
        >>> hex_convert('1A')
        26
        >>> hex_convert('FFFF')
        65535
    """

    dec_out = 0 
    position = 0 

    dec_for_hex_chars = { 
                        "A" : 10 ,
                        "B" : 11 ,
                        "C" : 12 ,
                        "D" : 13 ,
                        "E" : 14 ,
                        "F" : 15 }

    for item in hex_in[-1::-1] : 
        
        if item.isalpha(): 
            temp = dec_for_hex_chars[item.upper()]
        elif item.isdigit(): 
            temp = int(item)

        dec_out += temp * (16 ** position)
        position += 1 

    return dec_out


def hex_convert_hb(hex_in):
    """Convert a hexadecimal string, like '1A', into it's decimal equivalent.
        
        I/P: String 
        O/P: Int 
        >>> hex_convert_hb('6')
        6
        >>> hex_convert_hb('1A')
        26
        >>> hex_convert_hb('FFFF')
        65535
    """ 

    # Dictionary to convert a hex character to equivalent decimal value

    CONVERT = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
        '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
    }

    # Straightforward solution: for each digit, multiply it's value
    # by 16 ** (position):

    result = 0 

    for i, hex_char in enumerate(hex_in): 
        hex_digit = CONVERT[hex_char]
        power = 16 ** (len(hex_in) - i - 1)
        result = result + hex_digit * power

    return result


if __name__ == "__main__" : 

    import doctest 

    results = doctest.testmod()

    if results.failed == 0 : 
        print("ALL TESTS PASSED")
