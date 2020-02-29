# Insertion sort is a straightforward, well-performing sort algorithm. While it 
# has O(n²) runtime (rather than O(n log n), like Quicksort and Mergesort), it 
# is often faster for smaller, close-to-already sorted lists, because of the way 
# the algorithm works.

# Read about Insertion sort at https://en.wikipedia.org/wiki/Insertion_sort, 
# paying close attention to the description of the algorithm.

# We’ve given you a file, insertionsort.py, with a function, insertion_sort:

def insertion_sort(alist):
    """Given a list, sort it using insertion sort.
        
        I/P: List 
        O/P: List 

        >>> insertion_sort([3,1,2,6,5])
        [1, 2, 3, 5, 6]

        >>> insertion_sort([3, 7, 4, 9, 5, 2, 6, 1])
        [1, 2, 3, 4, 5, 6, 7, 9]

    """
    # Insertion sort iterates, consuming one input element each repetition, and 
    # growing a sorted output list. At each iteration, insertion sort removes 
    # one element from the input data, finds the location it belongs within the 
    # sorted list, and inserts it there. It repeats until no input elements 
    # remain.
    # At each array-position, it checks the value there against the largest 
    # value in the sorted list (which happens to be next to it, in the previous 
    #     array-position checked). If larger, it leaves the element in place and 
    # moves to the next. If smaller, it finds the correct position within the 
    # sorted list, shifts all the larger values up to make a space, and inserts 
    # into that correct position.
    
    i = 1 
    while i < len(alist) : 
        x = alist[i]
        j = i - 1 
        while j >= 0 and alist[j] > x : 
            alist[j+1] = alist[j]
            j -= 1 
        alist[j+1] = x 
        i += 1 

    return alist 


def insertion_sort_hb(alist):
    """Given a list, sort it using insertion sort.
    
        >>> insertion_sort_hb([3,1,2,6,5])
        [1, 2, 3, 5, 6]

        >>> insertion_sort_hb([3, 7, 4, 9, 5, 2, 6, 1])
        [1, 2, 3, 4, 5, 6, 7, 9]

    """

    for i in range(1, len(alist) ): 
        # For each item in the list, starting at the second, find out
        # how far to the left it goes--as soon as we find a number
        # smaller than it, we've gone far enough back    
        j = i - 1 

        while j >= 0 and alist[j] > alist[i] : 
            j -= 1 
        j += 1 

        if j != i : 
            alist[j: i+1] = alist[i:i+1] + alist[j:i]

    return alist 

        # 

if __name__ == "__main__" : 

    import doctest 

    results = doctest.testmod()

    if results.failed == 0 : 
        print("ALL TESTS PASSED")
