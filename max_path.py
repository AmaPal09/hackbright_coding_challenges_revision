# In a tree, a node can have many children, but each node can have only 
# one parent:
                #         (1)
                #     /         \
                #    (2)        (3)
                #  /     \     /    \
                # (4)    (5)  (6)   (7)
# A slightly-less-rigid structure is a “directed acyclic graph” (often called 
#   a “DAG”). This is a little more flexible than a tree, in that a node can 
#   have multiple parents. It’s still “directed”, meaning the arrows go in a 
#   particular direction, and “acyclic”, meaning there are no loops in it (it’s 
#   impossible to return to the same node a second time).
# Here’s an example of a DAG:
                #           (2)
                #        /      \
                #       /        \
                #      /          \
                #     /            \
                #    (5)           (4)
                #  /     \        /    \
                # /       \      /      \
            #    /         \    /        \
            #   (3)         (4)          (7)
            #  /   \       /   \        /   \
            # /     \     /     \      /     \
        #    (1)      (6)         (9)        (6)

# (We’ll call this particular type of DAG a “triangle” in this challenge).

# Imagine starting at the root node, 2. You can go down either to 5 or 4, and so on.
# In this challenge, you want to find the highest-scoring path to walk the DAG. 
# (In this example, this would be 2, 4, 7, 9 = 22):

# class Node(object):
#     """Basic node class that keeps track fo parents and children.

#         This allows for multiple parents---so this isn't for trees, where
#         nodes can only have one children. It is for "directed graphs".
#     """

#     def __init__(self, value):
#         self.value = value
#         self.children = []
#         self.parents = []

#     def __repr__(self):
#         return str(self.value)

    # We’ve also created a make_triangle function. This takes a list of 
    # node-level-data, and returns a list of nodes (where each node has the 
    #     proper parents and children attributes).
    # For example, to make the triangle above:

# >>> triangle = make_triangle([[2], [5, 4], [3, 4, 7], [1, 6, 9, 6]])
# Now triangle is a list of those nodes.
# In this challenge, you should write a maxpath function that takes that list 
# of nodes, and returns the value of the best path:

# >>> maxpath(triangle)
# 22
# The data values in the triangle will always be positive, whole integers.

# We’ve provided a stub function for you:


class Node(object):
    """Basic node class that keeps track fo parents and children.

        This allows for multiple parents---so this isn't for trees, where
        nodes can only have one children. It is for "directed graphs".
    """

    def __init__(self, value):
        self.value = value
        self.children = []
        self.parents = []

    def __repr__(self):
        return str(self.value)


def make_triangle(levels):
    """Make a triangle given a list of levels.

    For example, imagining this triangle::

               1
              2 3
             4 5 6
            7 8 9 10

    We could create it like this::

        >>> triangle = make_triangle([[1], [2,3], [4,5,6], [7,8,9,10]])
        >>> triangle
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    Let's check to make sure this works::

        >>> n1, n2, n3, n4, n5, n6, n7, n8, n9, n10 = triangle
        >>> n1.parents
        []
        >>> n1.children
        [2, 3]
        >>> n2.parents
        [1]
        >>> n2.children
        [4, 5]
        >>> n3.parents
        [1]
        >>> n3.children
        [5, 6]
        >>> n4.parents
        [2]
        >>> n4.children
        [7, 8]
        >>> n5.parents
        [2, 3]
        >>> n5.children
        [8, 9]
        >>> n6.parents
        [3]
        >>> n6.children
        [9, 10]

    """
    # make_triangle([
                    # [1], 
                    # [2,3], 
                    # [4,5,6], 
                    # [7,8,9,10]
                    # ])
    nodes = []
    for y, row in enumerate(levels):  
        for x, value in enumerate(row): 
            node = row[x] = Node(value) 
            nodes.append(node)  
            if y == 0:  
                continue
            if x == 0:  
                parents = [levels[y - 1][0]] 
            elif x == y:  
                parents = [levels[y - 1][x - 1]] 
            else:
                parents = [levels[y - 1][x - 1], 
                           levels[y - 1][x]]
            node.parents = parents           
            for p in parents:                
                p.children.append(node)      
    return nodes

def maxpath(nodes):
    """Given list of nodes in triangle, return high-scoring path."""
    # A good realization is that if a node at has two parents, it can look at the 
    # parents to decide which parent would have been more valuable to have 
    # traveled through.
    # We can keep track of, on each node, the “best score to have reached this 
    # node”, always choosing the better-parent and using it’s best score, plus 
    # that parent’s own data. Then, we just need to additionally keep track of 
    # the best score we found by the end of the list.

    # We can do this without having to traverse multiple paths, but just by 
    # visiting each node, and looking at it’s parent’s nodes.

    # Best score we've seen so far
    best = 0

    for n in nodes:

        if not n.parents: 
            # For the root, it has no best path 
            n.best = n.value 

        else: 
            n.best = n.value + max(p.best for p in n.parents)

        best = max(n.best, best)

    return best 


if __name__ == '__main__':
    import doctest

    print()
    if doctest.testmod().failed == 0:
        print("\t*** ALL TESTS PASSED; GOOD WORK!")
    print()