# Reverse a list in-place. Remember, for this to be “in-place” it can only use a 
# small, constant amount of extra storage space, so no duplicating the list!

def rev_list_in_place(lst):
    """Reverse list in place.
        You cannot do this with reversed(), .reverse(), or list slice
        assignment!

        I/P: List 
        O/P: List 

        >>> lst = [1, 2, 3]
        >>> rev_list_in_place(lst)
        >>> lst
        [3, 2, 1]

    """
    if len(lst) <= 1: 
        return lst 

    start_ctr = 0 
    end_ctr = len(lst) - 1
    temp = 0

    while start_ctr < end_ctr: 

        temp = lst[start_ctr]
        lst[start_ctr] = lst[end_ctr]
        lst[end_ctr] = temp

        start_ctr += 1 
        end_ctr -= 1 

    # return lst 


def rev_list_in_place_hb(lst):
    """Reverse list in place.
        You cannot do this with reversed(), .reverse(), or list slice
        assignment!

        I/P: List 
        O/P: List 

        >>> lst = [1, 2, 3]
        >>> rev_list_in_place_hb(lst)
        >>> lst
        [3, 2, 1]
        
    """

    for i in range(len(lst)//2): 
        # Use tuple unpacking to avoid using temp variable 
        lst[i], lst[-i - 1] = lst[-i - 1], lst[i]


if __name__ == '__main__': 

    import doctest 

    results = doctest.testmod()

    if results.failed == 0: 
        print("ALL TESTS PASSED")