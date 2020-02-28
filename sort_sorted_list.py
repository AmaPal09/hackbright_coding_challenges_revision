# Given two already-sorted lists:

# Write a function that returns a new list that is the sorted merge of both of 
# them. For the above lists, our result would be:


# It would be easy to do this by just using Python’s built-in sort method, 
# like this:
# >>> out = a + b
# >>> out.sort()

# However, this would have the runtime of O(n log n), where n is the combined 
# length of a and b. You can get a much better runtime by exploiting the fact 
# that both of the input lists are already sorted.

# Your challenge is to implement sort_ab where the runtime is O(a + b) (where a 
#     and b are the lengths of those lists, respectively).



def sort_ab(a, b):
    """Given already-sorted lists, `a` and `b`, return sorted list of both.

        You may not use sorted() or .sort().

        >>> a = [1, 3, 5, 7]
        >>> b = [2, 6, 8, 10]
        >>> sort_ab(a, b)
        [1, 2, 3, 5, 6, 7, 8, 10]

    """

    a_ctr = 0 
    b_ctr = 0 
    sorted_ab = []

    # print(a, len(a))
    # print(b, len(b))

    while ( (a_ctr < len(a)) and (b_ctr < len(b)) ) : 
        # print(a_ctr)
        # print(b_ctr)
        # print(sorted_ab)
        if a[a_ctr] < b[b_ctr] : 
            # print("A")
            sorted_ab.append(a[a_ctr])
            # print(sorted_ab)
            # print(a_ctr)
            a_ctr += 1 
        elif b[b_ctr] < a[a_ctr] : 
            # print("B")
            sorted_ab.append(b[b_ctr])
            b_ctr += 1
        elif a[a_ctr] == b[b_ctr] : 
            # print("C")
            sorted_ab.append(a[a_ctr])
            sorted_ab.append(b[b_ctr])
            a_ctr += 1 
            b_ctr += 1
        

    sorted_ab.extend(a[a_ctr:])
    sorted_ab.extend(b[b_ctr:])

    return sorted_ab


if __name__ == '__main__': 

    import doctest 

    results = doctest.testmod()

    if results.failed == 0: 
        print("ALL TESTS PASSED")


