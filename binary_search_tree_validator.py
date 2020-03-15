# A valid binary search tree follows a specific rule. In our case, the rule is 
# “left child must value must be less-than parent-value” and “right child must 
# be greater-than-parent value”.

# This rule is recursive, so everything left of a parent must less than that 
# parent (even grandchildren or deeper) and everything right of a parent must 
# be greater than the parent.

# For example, this tree is valid:
                #         (4)
                #     /         \
                #    (2)        (7)
                #  /     \     /    \
                # (1)    (3)  (5)   (8)

# This tree isn’t valid, as the left-hand 3 is wrong (it’s less than 2):
                #         (4)
                #     /         \
                #    (2)        (7)
                #  /     \     /    \
                # (3)    (3)  (5)   (8)

# This tree is invalid, as the bottom-right 1 is wrong — it is less than its 
# parent, 6, but it’s also less than its grandparent, 4, and therefore should 
# be left of 4:
                #         (4)
                #     /         \
                #    (2)        (7)
                #  /     \     /    \
                # (1)    (3)  (1)   (8)


# Your Challenge
# Your challenge is to write a method that, given a node in a binary search tree, 
# returns True or False depending on whether the tree rooted at that node is 
# valid.

# For example, checking the three trees above:

# >>> t = Node(4, Node(2, Node(1), Node(3)), Node(6, Node(5), Node(7)))
# >>> t.is_valid()
# True

# >>> t = Node(4, Node(2, Node(3), Node(3)), Node(6, Node(5), Node(7)))
# >>> t.is_valid()
# False

# >>> t = Node(4, Node(2, Node(1), Node(3)), Node(6, Node(1), Node(7)))

# >>> t.is_valid()
# False

class Node(object): 
    """ Node of a tree """

    def __init__(self, data, left=None, right=None): 
        """ Initialise """
        self.data = data 
        self.left = left 
        self.right = right 

    def __repr__(self): 
        """ Representation for printing """
        return "<Node {data}>".format(
            data = self.data)

    def is_valid_hb_1(self): 
        """ is this a valid BST 
            >>> t = Node(4, Node(2, Node(1), Node(3)), Node(6, Node(5), Node(7)))
            >>> t.is_valid_hb_1()
            True

            >>> t = Node(4, Node(2, Node(3), Node(3)), Node(6, Node(5), Node(7)))
            >>> t.is_valid_hb_1()
            False

            >>> t = Node(4, Node(2, Node(1), Node(3)), Node(6, Node(1), Node(7)))

            >>> t.is_valid_hb_1()
            False
        """
        # root = self 

        # if root.

        def _ok(n,lt,gt): 
            """Check this node and recurse to its children 
                
                lt: left children must be <= this 
                gt: right children must be >= this 

            """ 
            # print("n is: ",n)
            # print("lt is: ",lt)
            # print("gt is: ", gt)
            if n is None: 
                # This is not a node 
                # print("IF1")
                return True 

            if lt is not None and n.data > lt: 
                # Base case, bigger than allowed 
                # so fail 
                # print("IF2")
                return False 

            if gt is not None and n.data < gt: 
                # Base case, smaller than allowed 
                # so fail 
                # print("IF3")
                return False 

            if not _ok(n.left, n.data, gt ): 
                # general case: check left child of 
                # all the descendents of the left child 
                # must be less than our data and (greater than 
                # whatever we had to be greater than )
                # print("IF4")
                return False 

            if not _ok(n.right, lt, n.data): 
                # general case: check left child of 
                # all the descendents of the left child 
                # must be less than our data and (greater than 
                # whatever we had to be greater than )
                # print("IF5")
                return False 

            # If we reach here, we're either a leaf node with
            # valid data for lt/gt, or we're higher up, but
            # our recursive calls downward succeeded. Either way,
            # this is our winning base case.
            return True 

        # Call our recursive function, starting here.
        # Since we haven't yet gone left or right, we don't know
        # our `lt` or `gt` values yet, so pass None for these.
        return _ok(self, None, None)

# #############################################################################
# Iterration solution 
# Another way to think about the problem is: “if I gather the nodes in the order 
# of traversal of the tree, is this list sorted”?

# We can write a method that will let us loop over the tree using Python 
# for-loops and list comprehensions. To do this, we’ll create a special method,
# __iter__.
    
    def __iter__(self):

        """ Iterate over nodes in BST in proper order.

            The __iter__ method is called when you iterate
            over an object. It should yield successive
            values (for information on yielding, learn about
            "generators").

            Our BST can be iterated over to get the values
            in order. For example, for this tree::

                    4
                 2     6
                1 3   5 7

            We can loop over it::

            >>> t = Node(4, Node(2, Node(1), Node(3)), Node(6, Node(5), Node(7)) )
            >>> for n in t:
            ...     print(n.data, end=' ')
            1 2 3 4 5 6 7 

            This method of navigating a BST by left-recurse, self,
            right-recurse, is often called 'in-order traversal'.
        """

        # walk the left descendants recursively:
        for n in self.left or []:
            yield n

        yield self

        for n in self.right or []: 
            yield n 


    def is_valid_using_iter_check(self):
        """Is tree a valid BST?

            Another way to use our __iter__ method --- this time,
            walking over the iteration, and just making sure it
            doesn't ever go backwards.

            This solution is O(n) and does let us fail fast.

            >>> t = Node(4, Node(2, Node(1), Node(3)), Node(6, Node(5), Node(7)))
            >>> t.is_valid_hb_1()
            True

            >>> t = Node(4, Node(2, Node(3), Node(3)), Node(6, Node(5), Node(7)))
            >>> t.is_valid_hb_1()
            False

            >>> t = Node(4, Node(2, Node(1), Node(3)), Node(6, Node(1), Node(7)))

            >>> t.is_valid_hb_1()
            False
        """
        last = None

        for n in self: 
            if last is not None and n.data < last : 
                return False
            last = n.data 

        return True 


if __name__ == "__main__": 

    import doctest 

    results = doctest.testmod()

    if results.failed == 0: 
        print("ALL TESTS PASSED ")