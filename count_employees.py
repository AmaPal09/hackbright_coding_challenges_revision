# Consider an organization chart like:
        #              (Jane)
        #             /     \
        #            /       \
        #           /         \
        #          /           \
        #     (Jessica)       (Janet)
        #     /   |   \       /     \
        #    /    |    \     /       \
        # (Al) (Bob) (Jen) (Nick)   (Nora)
        #                             |
        #                         (Henri)

# This can be represented using nodes in a tree, like this:
# >>> henri = Node("Henri")
# >>> nora = Node("Nora", [henri])
# >>> nick = Node("Nick")
# >>> janet = Node("Janet", [nick, nora])
# >>> al = Node("Al")
# >>> bob = Node("Bob")
# >>> jen = Node("Jen")
# >>> jessica = Node("Jessica", [al, bob, jen])
# >>> jane = Node("Jane", [jessica, janet])
# Our Node class is:

# class Node(object):
#     """Node in a tree."""

#     def __init__(self, name, children=None):
#         self.name = name
#         self.children = children or []

# We want to create a method of our Node class, count_employees, which returns a 
# count of how many employees this person manages.
# This should include everyone under them, not just people who directly report to 
# them.
# For three chart above, this would return 0 for Henri, 1 for Nona, and 8 for 
# Jane.


class Node(object):
    """Node in a tree."""

    def __init__(self, name, children=None):
        self.name = name
        self.children = children or []

    def count_employees(self):
        """Return a count of how many employees this person manages.

            Return a count of how many people that manager manages. This should
            include *everyone* under them, not just people who directly report to
            them.
            >>> henri = Node("Henri")
            >>> nora = Node("Nora", [henri])
            >>> nick = Node("Nick")
            >>> janet = Node("Janet", [nick, nora])
            >>> al = Node("Al")
            >>> bob = Node("Bob")
            >>> jen = Node("Jen")
            >>> jessica = Node("Jessica", [al, bob, jen])
            >>> jane = Node("Jane", [jessica, janet])
            >>> t = henri.count_employees()
            >>> t == 0
            True
            >>> t = nora.count_employees()
            >>> t == 1
            True
            >>> t = nora.count_employees()
            >>> t == 4
            False
            >>> t = jane.count_employees()
            >>> t == 8
            True
        """
        count = 0 

        to_visit = [self]

        while to_visit: 
            current = to_visit.pop()

            if current: 
                count += 1 
            to_visit.extend(current.children)

        return count - 1 


        def count_employees_hb(self):
        """Return a count of how many employees this person manages.

            Return a count of how many people that manager manages. This should
            include *everyone* under them, not just people who directly report to
            them.
            >>> henri = Node("Henri")
            >>> nora = Node("Nora", [henri])
            >>> nick = Node("Nick")
            >>> janet = Node("Janet", [nick, nora])
            >>> al = Node("Al")
            >>> bob = Node("Bob")
            >>> jen = Node("Jen")
            >>> jessica = Node("Jessica", [al, bob, jen])
            >>> jane = Node("Jane", [jessica, janet])
            >>> t = henri.count_employees_hb()
            >>> t == 0
            True
            >>> t = nora.count_employees_hb()
            >>> t == 1
            True
            >>> t = nora.count_employees_hb()
            >>> t == 4
            False
            >>> t = jane.count_employees_hb()
            >>> t == 8
            True
        """

        count = 0 

        for child in children: 
            count = count + 1 + child.count_employees_hb()

        return count 


    def count_employees_hb2(self):
            """Return a count of how many employees this person manages.

                Return a count of how many people that manager manages. This should
                include *everyone* under them, not just people who directly report to
                them.
                >>> henri = Node("Henri")
                >>> nora = Node("Nora", [henri])
                >>> nick = Node("Nick")
                >>> janet = Node("Janet", [nick, nora])
                >>> al = Node("Al")
                >>> bob = Node("Bob")
                >>> jen = Node("Jen")
                >>> jessica = Node("Jessica", [al, bob, jen])
                >>> jane = Node("Jane", [jessica, janet])
                >>> t = henri.count_employees_hb2()
                >>> t == 0
                True
                >>> t = nora.count_employees_hb2()
                >>> t == 1
                True
                >>> t = nora.count_employees_hb2()
                >>> t == 4
                False
                >>> t = jane.count_employees_hb2()
                >>> t == 8
                True
            """

            count = 0 

            to_visit = [self]

            while to_visit: 
                emp = to.visit.pop()

                for child in emp.children: 
                    count += 1 
                    to_visit.append(child)

            return count 
                
            



if __name__ == "__main__": 

    import doctest 

    results = doctest.testmod()

    if results.failed == 0: 
        print("ALL TESTS PASSED ")

