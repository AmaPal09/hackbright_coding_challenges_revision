# A lemur wants to jump across a span in the forest on branches. She can jump 1 
# or 2 branches at a time. Unfortunately, some of the branches are on dead 
# trees, and she can’t use those branches to jump.

# For example:
# (1) ---> (2) ---> (3) ---> (4) ---> (5) ---> (6)
#  A        D        C        A         C       A
# A => Alive
# D => Dead 
# The D's are dead branches. In this example, the lemur starts on the first branch, and jumps 1 to branch #2 (she can’t jump 2 to branch #3, as it’s dead). She then jumps from 2 to 4 and from 4 to 6. As she ends up on the last branch, she’s finished.

# The first and last branch will always be alive, and there will never be two 
# dead branches in a row (that is, it will always be possible for her to make 
# this trip).

# Your challenge is to calculate how many jumps she needs to make.
# Code
# You’ll be given a list of the branches, like:
# [0, 0, 1, 0, 1, 0]
# 0 represents alive branches and 1 represents dead branches. The lemur starts 
# on the first branch in the list (index 0) and is finished when she reaches the 
# last branch in the list.

def  lemur(branches):
    """Return number of jumps needed.

        I/P: List 
        O/P: Int 
        >>> lemur([0])
        0
        >>> lemur([0, 0])
        1
        >>> lemur([0, 0, 0])
        1
        >>> lemur([0, 1, 0])
        1
        >>> lemur([0, 0, 1, 0])
        2
        >>> lemur([0, 0, 0, 0, 1, 0, 0, 1, 0])
        5
        >>> lemur([0,1,0,0,1,0,0])
        4
    """

    assert branches[0] == 0, "First branch must be alive"
    assert branches[-1] == 0, "Last branch must be alive"

    num_of_jumps = 0 
    i = 0 

    while i < (len(branches) -1 ): 
        if ((i < (len(branches)-2)) and (branches[i+2] == 0)): 
            i += 2 
            num_of_jumps += 1 
        elif (branches[i+1] == 0): 
            i += 1 
            num_of_jumps += 1 

    return num_of_jumps


def  lemur_hb(branches):
    """Return number of jumps needed.

        I/P: List 
        O/P: Int 
        >>> lemur([0])
        0
        >>> lemur([0, 0])
        1
        >>> lemur([0, 0, 0])
        1
        >>> lemur([0, 1, 0])
        1
        >>> lemur([0, 0, 1, 0])
        2
        >>> lemur([0, 0, 0, 0, 1, 0, 0, 1, 0])
        5
        >>> lemur([0,1,0,0,1,0,0])
        4
    """

    assert branches[0] == 0, "First branch must be alive"
    assert branches[-1] == 0, "Last branch must be alive"

    # START SOLUTION

    at = 2 
    n_jumps = 0 

    while at < len(branches) - 1: 
        at += 2 
        if at >= len(branches) or branches[at] == 1: 
            # We can't jump this far, so only jump 1
            at -= 1 

        n_jumps += 1 

    return n_jumps


if __name__ == "__main__": 

    import doctest 

    results = doctest.testmod() 

    if results.failed == 0: 
        print("ALL TESTS PASSED ")