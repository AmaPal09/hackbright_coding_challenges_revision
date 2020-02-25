# Lemmings are small rodents that live in arctic biomes. Unlike many other 
# creatures that live in such cold climates, they do not hibernate, but survive 
# the winter by burrowing into holes and looking for food.

# On a particular island, there are num_holes number of lemming holes, arranged in 
# a line, each 1 meter apart. Some of these lemming holes have food (we’ll call 
#     these holes “cafes”)
# You can imagine this like this:
#     1m       1m        1m       1m       1m
# (1) ---> (2) ---> (3) ---> (4) ---> (5) ---> (6)
#                    C                 C 

# The C holes are cafes.

# Imagine there’s a lemming currenly in each hole, and they’re all hungry. The 
# lemmings in hole #3 and #5 don’t need to travel at all, but the other lemmings 
# need to travel to find the nearest cafe:
# the lemming in hole #1 needs to travel 2m to hole #3
# the lemming in hole #2 needs to travel 1m to hole #3
# the lemming in hole #4 needs to travel 1m to hole #3 (or 1m to hole #5)
# the lemming in hole #6 needs to travel 1m to hole #5

# In this problem, you want to calculate the longest amount, in meters, any 
# lemming needs to travel to get food. For this example, the answer would 2, since 
# lemming in hole #1 needs to travel 2m to get to the nearest cafe.

# The Challenge
# You’ll be given two pieces of information:
# num_holes   The number of holes
# cafes       The indexes of those holes with food in them (note that these 
#             indexes are zero-based). This list is sorted, and a single hole will 
#             only appear at most once in it.
# You should return a single integer, for the maximum distance any of the lemmings 
# need to travel.

def furthest(num_holes, cafes):
    """Find longest distance between a hole and a cafe.
        I/P: Int, List 
        O/P: Int 

        >>> furthest(6, [2,4])
        2
        >>> furthest(8, [1,5,7])
        2
        >>> furthest(8, [1,7])
        3
    """

    max_dist = 0 

    for num in range(num_holes): 
        dist = []
        # print(num)
        for cafe in cafes: 
            dist.append(abs(cafe-num))
        # print(dist)
        
        if max_dist < min(dist): 
            max_dist = min(dist)
        # print(max_dist)
    return max_dist

# Runtime = O(n^2)


def furthest_hb(num_holes, cafes):
    """Find longest distance between a hole and a cafe.
        I/P: Int, List 
        O/P: Int 

        >>> furthest_hb(6, [2,4])
        2
        >>> furthest_hb(8, [1,5,7])
        2
        >>> furthest_hb(8, [1,7])
        3
    """

    worst = 0 

    for hole in range(num_holes): 
        # Looking at all cafes, find distance to this hole,
        # and choose the smallest distance.
        dist = min([abs(cafe - hole) for cafe in cafes ])

        # Keep track of the longest distance we've seen

        worst = max(worst, dist)

    return worst


def furthest_hb_2(num_holes, cafes):
    """Find longest distance between a hole and a cafe.
        I/P: Int, List 
        O/P: Int 

        >>> furthest_hb_2(6, [2,4])
        2
        >>> furthest_hb_2(8, [1,5,7])
        2
        >>> furthest_hb_2(8, [1,7])
        3
    """
    from bisect import bisect_left 

    worst = 0 

    for hole in range(num_holes): 

        # Find the place we'd insert this whole into the sorted cafes list 
        # print("hole:", hole)
        idx = bisect_left(cafes, hole)
        # print("idx: ", idx)

        if idx == len(cafes): 
            # This hole is after all the cafes, so the distance 
            #  is  from the hole to the cafe after it
            dist = hole - cafes[idx - 1]
            # print("AAA")

        elif idx == 0: 
            # This hole before all the cafes, so the distance 
            #  is from this hole to the first cafe 
            dist = cafes[idx] - hole 
            # print("BBB")

        elif cafes[idx] == hole: 
            # This whole is a cafe, so no need to travel
            dist = 0 
            # print("CCC")

        else: 
            # This whole is between 2 cafes, so select the smaller distance 
            # between them 
            dist = min(hole - cafes[idx-1], cafes[idx]-hole)
            # print("DDD")

        # Keep track of the longest distance we've seen 
        # print(dist)
        worst = max(worst, dist)
        # print("Worst: ", worst)

    return worst 


def furthest_hb_3(num_holes, cafes):
    """Find longest distance between a hole and a cafe.
        I/P: Int, List 
        O/P: Int 

        >>> furthest_hb_3(6, [2,4])
        2
        >>> furthest_hb_3(8, [1,5,7])
        2
        >>> furthest_hb_3(8, [1,7])
        3
    """
    # This solution looks at the cafes, finding the two that are furthest
    # apart, and then determining which lemming hole would have to travel
    # the furthest between them.

    # Start with the distance from first hole to the first cafe, and from
    # the last hole to the last cafe:
    distances = [ cafes[0], num_holes - cafes[-1] -1] 

    for i in range(1, len(cafes)): 
        # between cafes: distance is half the distance to leftward cafe 
        distances.append((cafes[i] - cafes[i-1]) // 2)

    return max(distances)


if __name__ == "__main__": 

    import doctest 

    results = doctest.testmod() 

    if results.failed == 0: 
        print("ALL TESTS PASSED ")