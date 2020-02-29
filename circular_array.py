# In this challenge, you will create a “circular array” — like a normal array, 
# but the end wraps around to the beginning (which makes for some interesting 
#     problems).

# A circular array is defined by having a start and indexes (be sure to think 
#     about optimizing runtime for indexing, since we’ll do this so much more 
#     often than adding items to it):

# Because the last item circles back around to the first item, you can rotate 
# the list and shift the indexes. Positive numbers rotate the list start (defined 
#     as the index 0) to the right (or higher indexes):

# And negative numbers rotate the list start to the left (or lower indexes):

# And you can also rotate more than once around the ring:

# If you add a new item after rotating, it should go at the end of the list in 
# its current rotation:


class CircularArray(object):
    """An array that may be rotated, and items retrieved by index
    
        >>> circ = CircularArray()
        >>> circ.add_item('harry')
        >>> circ.add_item('hermione')
        >>> circ.add_item('ginny')
        >>> circ.add_item('ron')
        >>> circ.print_array()
        harry
        hermione
        ginny
        ron
        >>> circ.get_by_index(2)
        'ginny'
        >>> print(circ.get_by_index(15)) 
        None

        >>> circ = CircularArray()
        >>> circ.add_item('harry')
        >>> circ.add_item('hermione')
        >>> circ.add_item('ginny')
        >>> circ.add_item('ron')
        >>> circ.rotate(1)
        >>> circ.print_array()
        hermione
        ginny
        ron
        harry
        >>> circ.get_by_index(2)
        'ron'

        >>> circ = CircularArray()
        >>> circ.add_item('harry')
        >>> circ.add_item('hermione')
        >>> circ.add_item('ginny')
        >>> circ.add_item('ron')
        >>> circ.rotate(-1)
        >>> circ.print_array()
        ron
        harry
        hermione
        ginny
        >>> circ.get_by_index(2)
        'hermione'
        
        >>> circ = CircularArray()
        >>> circ.add_item('harry')
        >>> circ.add_item('hermione')
        >>> circ.add_item('ginny')
        >>> circ.add_item('ron')
        >>> circ.rotate(-17)
        >>> circ.get_by_index(1)
        'harry'

        >>> circ = CircularArray()
        >>> circ.add_item('harry')
        >>> circ.add_item('hermione')
        >>> circ.add_item('ginny')
        >>> circ.add_item('ron')
        >>> circ.rotate(-2)
        >>> circ.add_item('dobby')
        >>> circ.print_array()
        ginny
        ron
        harry
        hermione
        dobby
    """

    def __init__(self):
        """Instantiate CircularArray."""
        self.c_array = []

    def add_item(self, item):
        """Add item to array, at the end of the current rotation."""
        self.c_array.append(item)

    def get_by_index(self, index):
        """Return the data at a particular index."""
        if index < len(self.c_array) : 
            return self.c_array[index]
        else: 
            return None 

    def rotate(self, increment):
        """Rotate array, positive for right, negative for left.

        If increment is greater than list length, keep going around.
        """
        if increment > 0 : 
            # Increment is +ve, move for right 
            while increment > 0 : 
                # move the top element to the bottom 
                elem = self.c_array.pop(0)
                self.c_array.append(elem)
                increment -= 1 

        elif increment < 0 : 
            # Increment in -ve, move for left 
            while increment < 0 : 
                # move the bottom element to the top 
                elem = self.c_array.pop()
                self.c_array = [elem] + self.c_array[0:]
                increment += 1 

    def print_array(self):
        """Print the circular array items in order, one per line"""

        for elem in self.c_array : 
            print(elem)


class CircularArray_hb(object):
    """An array that may be rotated, and items retrieved by index
    
        >>> circ = CircularArray_hb()
        >>> circ.add_item('harry')
        >>> circ.add_item('hermione')
        >>> circ.add_item('ginny')
        >>> circ.add_item('ron')
        >>> circ.print_array()
        harry
        hermione
        ginny
        ron
        >>> circ.get_by_index(2)
        'ginny'
        >>> print(circ.get_by_index(15)) 
        None

        >>> circ = CircularArray_hb()
        >>> circ.add_item('harry')
        >>> circ.add_item('hermione')
        >>> circ.add_item('ginny')
        >>> circ.add_item('ron')
        >>> circ.rotate(1)
        >>> circ.print_array()
        hermione
        ginny
        ron
        harry
        >>> circ.get_by_index(2)
        'ron'

        >>> circ = CircularArray_hb()
        >>> circ.add_item('harry')
        >>> circ.add_item('hermione')
        >>> circ.add_item('ginny')
        >>> circ.add_item('ron')
        >>> circ.rotate(-1)
        >>> circ.print_array()
        ron
        harry
        hermione
        ginny
        >>> circ.get_by_index(2)
        'hermione'
        
        >>> circ = CircularArray_hb()
        >>> circ.add_item('harry')
        >>> circ.add_item('hermione')
        >>> circ.add_item('ginny')
        >>> circ.add_item('ron')
        >>> circ.rotate(-17)
        >>> circ.get_by_index(1)
        'harry'

        >>> circ = CircularArray_hb()
        >>> circ.add_item('harry')
        >>> circ.add_item('hermione')
        >>> circ.add_item('ginny')
        >>> circ.add_item('ron')
        >>> circ.rotate(-2)
        >>> circ.add_item('dobby')
        >>> circ.print_array()
        ginny
        ron
        harry
        hermione
        dobby
    """

    def __init__(self): 
        """ Instantiate CircularArray_hb"""

        # using a list to store the array instead of linked-list
        # style nodes in order to optimize runtime for indexes
        self.array = [] 

        # track the current item at index 0 for the circular array
        # by storing that item's actual index in self.array.
        # Store None for an empty array.
        self.head = None 

    def add_item(self, item) : 
        """ Add item to the array, at the end of the current rotation """

        if self.head is None : 
            # if there are currently no items in the array, set
            # `self.array` to contain our new item, and set the head
            # to point to that item (at index 0 in self.array).
            self.head = 0 
            self.array = [item]

        else: 
            # insert item. If we insert it at the self.head position,
            # it will  get inserted just before the head, which puts
            # it at the end of the current rotation
            self.array.insert(self.head, item)

            # reassign head --- it has shifted ahead by one thanks
            # to the insert for the new item.
            self.head += 1 


    def get_by_index(self, index):
        """ Return the data at a particular index """

        # index doesn't exist the list, return None
        if index > len(self.array) : 
            return None 

        # this is the easy case -- the index doesn't go off the
        # end of self.array when you start from head
        if index + self.head < len(self.array): 
            return self.array[index + self.head ]

        # the fun case: we have to go round the twist (beyond end of
        # self.array). 
        # In this case, add index to self.head and then shift left by
        # the length of array to get back into self.array index space
        adjusted_index = index + self.head - len(self.array)
        return self.array[adjusted_index]

    def rotate(self, increment): 
        """Rotate array, positive for right, negative for left.

            If increment is greater than list length, keep going around.
        """
        # if the array dosen't have any element, dont do anything 
        if self.head is None: 
            return 

        adjusted_index = (increment + self.head) % len(self.array)
        self.head = adjusted_index

    def print_array(self): 
        """Print the circular array items in order, one per line"""

        for i in range(len(self.array)): 
            print(self.get_by_index(i))


if __name__ == "__main__": 

    import doctest 

    results = doctest.testmod() 

    if results.failed == 0: 
        print("ALL TESTS PASSED")
