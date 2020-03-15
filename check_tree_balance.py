# A tree is balanced if 1) the depths of its child trees differ by no more than 
# one and 2) this is true for EVERY subtree.
# Here’s an example of a balanced tree:
                #         (n)
                #     /         \
                #    (n)        (n)
                #  /     \     /    \
                # (n)    (n)  (n)   (n)

# This is also a balanced tree — there’s more on the big left trunk, but the 
# heights vary by only one:
                #         (n)
                #     /         \
                #    (n)        (n)
                #  /     \    
                # (n)    (n)  

# Here’s an imbalanced tree — the heights vary by too much (the left-hand child 
#     of the root has two levels of descendants, whereas the right-hand child has 
#     zero levels):
                #         (n)
                #     /      
                #    (n)     
                #  /     \    
                # (n)    (n)  

# In this exercise, you’ll make a function that tests where a binary tree is 
# balanced.

# We’ve defined a class, BinaryNode:

# checkbalanced.py
class BinaryNode(object):
    """Node in a binary tree."""

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def is_balanced(self):
        """Is the tree at this node balanced?
        """

        def _num_descendants(node): 
            """ Return number of descendants or None if already imbalance """

            if not node: 
                # Base case, this is the child of a leaf, not a real node 
                return 0 

            # Get the descendants on the left. if None, means already imbalanced 
            left = _num_descendants(node.left)

            if left is None: 
                return None

            # Get the descendants on the right, if None, means already imbalanced 
            right = _num_descendants(node.right)

            if right is None: 
                return None 

            if abs(left-right) > 1: 
                return None 

            # height of this node is the height of the deepest descendants and 
            # overselves 
            return max(left, right) + 1 

        return _num_descendants(self)




