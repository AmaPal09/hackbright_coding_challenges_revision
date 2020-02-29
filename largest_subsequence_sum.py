# Given a list of integers, return the contiguous subsequence with the highest 
# sum:
# For example, given a list of integers, like:
# >>> my_list = [1, 0, 3, -8, 4, -2, 3]
# Return the contiguous subsequence with the largest sum. For that example, 
# the answer would be [4, -2, 3], which sums to 5.
# For ties, return the first one:
# Return the shortest version:
# If the list is all negative numbers, the subsequence with the highest sum will 
# be empty (ie, we can do no better than pick nothing!):
# Challenge
# You could do this in a very slow way by trying every possible subsequence, but 
# the runtime here would be poor (what would the runtime be?)
# There’s a way to do this with a runtime of O(n), but it requires some careful 
# thinking.


def largest_sum(nums):
    """Find subsequence with largest sum.

        I/P: List
        O/P: List 

        >>> largest_sum([1, 0, 3, -8, 4, -2, 3])
        [4, -2, 3]
        >>> largest_sum([1, 0, 3, -8, 4, -2, 3, -2])
        [4, -2, 3]
        >>> largest_sum([1, 0, 3, -8, 19, -20, 4, -2, 3, -2])
        [19]
        >>> largest_sum([2, 2, -10, 1, 3, -20])
        [2, 2]
        >>> largest_sum([2, -2, 3, -1])
        [3]
        >>> largest_sum([-1, -2])
        []
    """

    sub_sum = 0             
    sub_seq = []            
    max_sum = 0             
    sub_str = 0             
    sub_end = -1 
    max_str = 0 

    # Go through every item in the list 
    # [1, 0, 3, -8, 4, -2, 3]
    for i, num in enumerate(nums) :  

        sub_sum += num 

        # The current sub_seq sum is greater than the max sum 
        if sub_sum > max_sum: 
            max_sum = sub_sum
            max_str = sub_str
            sub_end = i 

        if sub_sum <= 0 : 
            sub_str = i + 1 
            sub_sum = 0 

    return nums[max_str: sub_end + 1 ]
    #     
    #     if sub_sum == 0:    # False
    #       sub_str = i     

    #     if sub_sum + num > 0 :     
    #         sub_sum += num         
    #         sub_end = i
    #     else : 
    #         if sub_sum > max_sum : 
    #             sub_seq = nums[sub_str: sub_end + 1]  
    #             max_sum = sub_sum
    #             sub_sum = 0 

    # if sub_sum > max_sum : 
    #     sub_seq = nums[sub_str: sub_end + 1 ]

    # return sub_seq


if __name__ == "__main__": 

    import doctest 

    results = doctest.testmod()

    if results.failed == 0: 
        print("ALL TESTS PASSED ")
