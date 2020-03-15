# In this challenge, you will write a function to append a child to a node in a 
# Binary Search Tree.
# We’ll give you a Node class with left and right attributes, as well as a data 
# attribute:

# bstadd.py
# class Node(object):  # ...
#     def __init__(self, data, left=None, right=None):
#         """Create node, with data and optional left/right."""

#         self.left = left
#         self.right = right
#         self.data = data

# Consider this tree:
                #         (4)
                #     /         \
                #    (2)        (7)
                #  /     \     /    \
                # (1)    (3)  (5)   (8)

# We can build this tree using our Node class like this:
# >>> t = Node(4,
# ...       Node(2, Node(1), Node(3)),
# ...       Node(7, Node(5), Node(8))
# ... )

# If we wanted to add 0 to our tree, it would end up as the left-most child of 
# our tree, as it comes before everything else in the tree. We’d end up with 
# this tree:
              #           (4)
              #       /         \
              #      (2)        (7)
              #    /     \     /    \
              #   (1)    (3)  (5)   (8)
              #   /
              # (0)
# Our insert method should do this correctly:
# >>> t.insert(0)
# >>> t.left.left.left.data == 0
# True
# >>> t.left.left.right is None
# True

# If we added 9, it would end up as the right-most node, as it comes after 
# else in the tree:
              #           (4)
              #       /         \
              #      (2)        (7)
              #    /     \     /    \
              #   (1)    (3)  (5)   (8)
              #   /                    \
              # (0)                    (9)
# Our insert method should do this correctly:
# >>> t.insert(9)
# >>> t.right.right.right.data == 9
# True
# >>> t.right.right.left is None
# True

# If we added 6, it would end up to the right of the 5:
              #           (4)
              #       /         \
              #      (2)        (7)
              #    /     \     /    \
              #   (1)    (3)  (5)   (8)
              #   /             \      \
              # (0)             (6)    (9)
# Our insert method should do this correctly:
# >>> t.insert(6)
# >>> t.right.left.right.data == 6
# True
# >>> t.right.left.left is None
# True

# We’ve given you a stub of the insert method:


# class Node(object):  # ...
#     def insert(self, new_data):
#         """Insert new node with `new_data` to BST tree rooted here."""


class Node(object): 
    """ Node of a Binary Tree """

    def __init__(self, data, left = None, right = None): 
        """ Initialise         """
        self.data = data 
        self.left = left 
        self.right = right 

    def __repr__(self):
        """ Representation for printing """
        return "<Node {data}>".format(
            data = self.data)

    def insert(self, new_data): 
        """ Insert new node with 'new_data ' to the BST tree root 
            >>> t = Node(4, Node(2, Node(1), Node(3)), Node(7, Node(5), Node(8)))
            >>> t.insert(0)
            >>> t.left.left.left.data == 0
            True
            >>> t.left.left.right is None
            True

            >>> t.insert(9)
            >>> t.right.right.right.data == 9
            True
            >>> t.right.right.left is None
            True

            >>> t.insert(6)
            >>> t.right.left.right.data == 6
            True
            >>> t.right.left.left is None
            True
        """

        if new_data < self.data: 
            # new_data node will be on the left of the root node 
            if self.left is None: 
                # No child node present, add new_data as the left child 
                self.left = Node(new_data)
            else: 
                # Keep looking on the left side of this node 
                self.left.insert(new_data)

        else: 
            # new_data node will be on the right of the root node 
            if self.right is None: 
                # No child node present, add new_data as the right child 
                self.right = Node(new_data)
            else: 
                # Keep looking on the right side of this node 
                self.right.insert(new_data) 


if __name__ == "__main__": 

    import doctest 

    results = doctest.testmod()

    if results.failed == 0: 
        print("ALL TESTS PASSED ")