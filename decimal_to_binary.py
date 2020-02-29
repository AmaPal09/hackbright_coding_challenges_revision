# Binary numbers are base 2 numbers – there are only 0s and 1s in the numbers. 
# So, for example:
# Decimal         Binary
# 0               0
# 1               1
# 2               10
# 3               11
# 4               100             
# 5               101     
# 6               110
# 7               111
# 8               1000
# 9               1001
# 10              1010
# 11              1011
# 12              1100
# 13              1101
# 14              1110
# 15              1111
# 16              10000

# Write a function that is given a decimal number and returns the binary number 
# as a string.

def dec2bin(num):
    """Convert a decimal number to binary representation.
    
        I/P: Int 
        O/P: String 

        >>> dec2bin(6)
        '110'
    """

    Q = 0 
    R = 0 
    bin_num = ""

    if num == 0: 
        return "0"
    elif num == 1: 
        return "1"

    while num >= 2: 
        # Get the remainder for the units place of the binary 
        R = num % 2 
        bin_num += str(R)
        Q = num // 2 
        if Q == 1: 
            bin_num += str(Q)
        num = num // 2 

    return bin_num[-1::-1]


def dec2bin_backwards(num):
    """Convert a decimal number to binary representation.

        >>> dec2bin_backwards(6)
        '110'
    """

    # Work backwards, finding the least-significant-bit first,
    # moving up to the most-significant bit.
    #
    # At the end, print the list of bits reversed

    result = [] 
    place = 0 

    while place == 0 or num >= 2 ** place : 

        if num % (2 ** (place + 1) ) : 
            result.append("1")
            num -= 2 ** place 

        else: 
            result.append("0")

        place += 1 

    return "".join(reversed(result))


def dec2bin_forwards(num):
    """Convert a decimal number to binary representation.
    
        >>> def2bin_forwards(6)
        '110'
    """

    # Work forwards. Figure out how many bits there will be,
    # so you know what power of two the left-most bit will have.
    #
    # Calculate each bit, from most-significant to least, adding
    # to a string answer.

    out = ""

    # Figure out how many bits there will be 
    num_bits = 1 

    while 2 ** num_bits <= num: 
        num_bits += 1 

    for position in range(num_bits -1 , -1, -1 ) : 

        if 2 ** position <= num : 
            num -= 2 ** position
            out += "1"
        else: 
            out += "0"

    return out 


def dec2bin_division(num):
    """Convert a decimal number to binary representation.
    
        >>> dec2bin_division(6) 
        '110'
    """

    # Work from right to left, from 1's place up to 2^n's place
    #
    # Use mod to tell you if each digit should be a zero or a one
    #
    # Then divide by two to move onto the next digit

    if num == 0: 
        return "0"

    reversed_digits = []

    while num > 0 : 
        #num % 2 will always be 0 or 1 
        reversed_digits.append(num % 2 )
        num // 2

    return "".join(reversed(reversed_digits))

if __name__ == "__main__" : 

    import doctest 

    results = doctest.testmod()

    if results.failed == 0 : 
        print("ALL TESTS PASSED")
