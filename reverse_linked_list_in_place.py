# Write a function that takes a linked list and changes the list so that the 
# nodes are in the reverse order.

class Node(object):
    """Class in a linked list."""

    def __init__(self, data, next = None) : 
        self.data = data 
        self.next = next 

class LinkedList(object):
    """Linked list."""

    def __init__(self, head = None) : 
        self.head = head 

    def as_string(self) : 
        """Represent data for this list as a string.

        >>> LinkedList(Node(3)).as_string()
        '3'

        >>> LinkedList(Node(3, Node(2, Node(1)))).as_string()
        '321'
        """
        out = []
        n = self.head 

        while n : 
            out.append(str(n.data))
            n = n.next 

        return "".join(out)


def reverse_linked_list_in_place(lst): 
    """ Reverse the linked list in place 
        
        I/P: Linked List 
        O/P: Linked List 
        >>> ll = LinkedList(Node(1, Node(2, Node(3))))
        >>> reverse_linked_list_in_place(ll)
        >>> ll.as_string()
        '321'
    """
    # head ---> 1 ---> 2 ---> 3 ---> None 
    # should return None <--- 1 <--- 2 <--- 3 <--- head
    #  None <--- 1  2 ---> 3

    prev = None 
    curr = lst.head                         # curr = head / 1 

    while curr is not None :                # True 
        next = curr.next                    # next = 2 
        curr.next = prev                    # 1 ---> None 
        prev = curr                         # prev = 1   
        curr = next 

    lst.head = prev 


def reverse_linked_list_in_place(lst) : 
    """ Reverse the linked list in place using recursion 
        
        I/P: LinkedList 
        O/P: LinkedList 

        >>> ll = LinkedList(Node(1, Node(2, Node(3))))
        >>> reverse_linked_list_in_place(ll)
        >>> ll.as_string()
        '321'
    """

    curr = lst.head 
    prev = None 

    def _rec_reverse(curr, prev) : 

        #base case 
        if not curr : 
            return prev 

        nxt = curr.next 
        curr.next = prev 
        prev = curr 
        curr = nxt 

        return _rec_reverse(curr , prev)

    lst.head = _rec_reverse(curr, prev)


if __name__ == "__main__": 

    import doctest 

    results = doctest.testmod() 

    if results.failed == 0: 
        print("ALL TESTS PASSED")
