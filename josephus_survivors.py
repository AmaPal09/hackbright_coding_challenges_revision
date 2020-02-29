# This is a classic algorithm problem, based on a Biblical-era tale.

# Imagine a group of 10 people in a circle, numbered 1 to 10. If we started at 
# the first person (#1) and killed every three people, it would look like this:

# 1  2  3  4  5  6  7  8  9  10
#       !        !        !
# This continues, though, looping around again, starting with where we left of at 
# #10 (we’ll mark the freshly-removed as red/! and the previously-removed in 
#     striked-out gray/X):

# 1  2  3  4  5  6  7  8  9  10
#    !  X        X  !     X
# And again, starting where that left off, at #8, and continuing:

# 1  2  3  4  5  6  7  8  9  10
# !  X  X        X  X  !  X

# 1  2  3  4  5  6  7  8  9  10
# X  X  X     !  X  X  X  X

# 1  2  3  4  5  6  7  8  9  10
# X  X  X     X  X  X  X  X  !
# At this point, only #4 remains, so that person would be our “survivor”.

# Write an algorithm that, given a number of people, and the “skip”, which person 
# will be the survivor.

class Node(object): 
    """ Node to be used for linked list """
    # def __init__(self, data, prev=None, next=None):
    def __init__(self, data, prev = None, next = None): 
        """ Instantiate node """
        self.data = data 
        self.prev = prev
        self.next = next 

    def __repr__(self):
        """ Print node """
        return "<Node prev=%s, data=%s, next=%s>" %(
                self.prev.data, self.data, self.next.data)

    @classmethod
    def make_list(cls, n): 
        """Construct a circular doubly-linked list of n items. Returns head node.

            >>> node = Node.make_list(3)

            >>> node.data
            1

            >>> node.next.data
            2

            >>> node.next.next.next.data
            1

            >>> node.prev.data
            3

            >>> node.prev.prev.prev.data
            1
        """

        #Make the first node (and remember that it's first node)
        first = node = prev = cls(1)

        #Make other node and link them 
        for i in range(2, n+1): 
            node = Node(i, prev = prev)
            prev.next = node 
            # print(node.prev.data, node.data)
            prev = node 

        node.next = first
        first.prev = node 

        return first 

# class LinkedList(object): 
#     """ Class Linked List """

#     def __init__(self, head = None, tail = None): 
#         """ Instantiate linked list """
#         self.head = None 
#         self.tail = None

#     def __repr__(self): 
#         """ Print the linked list """
#         return "<LinkedList head = %s, tail=%s>" %(
#                 self.head, self.tail)

#     def append(self, data): 
#         """ Add node with data to the end of the linkedlist """
#         # Add note as the first elem. 
#         # point head to node
#         # prev of node is None
#         # next of node is tail 
#         new_node = Node(data)

#         if self.head is None: 
#             self.head = new_node

#             new_node.next = self.tail 
#             new_node.prev = self.tail 



def find_survivor(num_people, kill_every):
    """Given num_people in circle, kill [kill_every]th person, return survivor.

        >>> find_survivor(10, 3)
        4
    """

    node = Node.make_list(num_people)

    # loop until only one node is left 
    while node.next != node : 

        for i in range(kill_every - 1) : 
            # if we kill_every 3rd person, we need to skip 2. 
            node = node.next 

        node.prev.next = node.next 
        node.next.prev = node.prev 

        node = node.next 

    return node.data


if __name__ == "__main__": 

    import doctest 

    results = doctest.testmod()

    if results.failed == 0: 
        print("ALL TESTS PASSED ")
