# A binary search tree is a binary tree where all left-hand node values are less 
# than or equal to the node value, and all right-hand node values are greater 
# than the node value.
#
# For example:
# We’ve written a simple BinaryNode class for binary search tree nodes, with a 
# data attribute and left and right child note attributes.

class BinaryNode(object):
    """Node in a binary tree."""

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

# When you run the makebst.py file, the tests do not pass. This is expected, as 
# we haven’t implemented the make_bst function.
#
# Given a sorted Python list of integers, produce a balanced binary search tree 
# from the list of integers.
# For example, given the list nums = [1, 2, 3, 4, 5, 6, 7], you should produce 
# the tree :
                #         (4)
                #     /         \
                #    (2)        (6)
                #  /     \     /    \
                # (1)    (3)  (5)   (7)

# If you can’t generate a perfectly-balanced tree, you should prefer to fill 
# left-hand children over right-hand ones.
#
# So, for example, nums = [1, 2, 3, 4] should give:
                #         (3)
                #     /         \
                #    (2)        (4)
                #  /    
                # (1)    

# Implement the make_bst function.
# Once you do this, all tests should pass.

def make_bst(nums):
    """Given a list of sorted numbers, make a binary search tree.

    Returns the root node of a new BST that is valid and balanced.
    """

    if not nums: 
        return None 

    # Listed is sorted. Use binary approach, divide it in 2 parts 

    mid_index = len(nums) // 2 

    # make node out of the value at mid point 
    node = BinaryNode(nums[mid_index])

    # Recursively find the new left side and right side nodes 
    node.left = make_bst(nums[:mid_index])
    node.right = make_bst(nums[mid_index+1:])

    return node 

if __name__ == "__main__": 

    import doctest 

    results = doctest.testmod()

    if results.failed == 0: 
        print("ALL TESTS PASSED ")

