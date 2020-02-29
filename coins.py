# You have an endless supply of dimes and pennies. How many different amounts of 
# total change can you make using exactly num_coins number coins?

# For example, when num_coins = 3, you can create 4 different kinds of change:
# 3 cents from penny + penny + penny
# 12 cents dime + penny + penny
# 21 cents from dime + dime + penny
# 30 cents from dime + dime + dime

# So, you should have a function that returns the set {3, 12, 21, 30} when 
# num_coins is 3.


def coins(num_coins):
    """Find change from combinations of `num_coins` of dimes and pennies.
        This should return a set of the unique amounts of change possible.
        
        I/P: Int 
        O/P: Set 

        >>> coins(1) == {1, 10}
        True
        >>> coins(2) == {2, 11, 20}
        True
        >>> coins(3) == {3, 12, 21, 30}
        True
        >>> coins(4) == {4, 13, 22, 31, 40}
        True
        >>> coins(10) == {10, 19, 28, 37, 46, 55, 64, 73, 82, 91, 100}
        True

    """

    amounts = set()
    num_pennies = 0 

    while num_pennies < num_coins + 1 : 
        num_dimes = num_coins - num_pennies 
        amount = (num_dimes * 10) + (num_pennies * 1)
        amounts.add(amount)
        num_pennies += 1 

    return amounts


def add_coins(left, total, results):
    """Add combos coins to total.

        If this is the last time we can add coins, return change.

        Otherwise, recursively call until that condition.

        >>> results = set()
        >>> add_coins(left=1, total=0, results=results)
        >>> results == set([1, 10])
        True
    """

    DIME = 10 
    PENNY = 1 
    # print(left, total, results)
    if left == 0: 
        # Base Case
        # We've added all the coins we're supposed to, so keep
        # track of this total of change and stop recursing
        results.add(total)
        return

    # Fork into two recursions, one adding a dime and another a penny
    # For each, we'll have 1 fewer coin to add afterwards, so left -= 1
    add_coins(left - 1, total + DIME, results)
    add_coins(left - 1, total + PENNY, results)


def coins_hb(num_coins):
    """Find change from combinations of `num_coins` of dimes and pennies.

        This should return a set of the unique amounts of change possible.

        >>> coins_hb(1) == {1, 10}
        True
        >>> coins_hb(2) == {2, 11, 20}
        True
        >>> coins_hb(3) == {3, 12, 21, 30}
        True
        >>> coins_hb(4) == {4, 13, 22, 31, 40}
        True
        >>> coins_hb(10) == {10, 19, 28, 37, 46, 55, 64, 73, 82, 91, 100}
        True

    """

    results = set()
    add_coins(left = num_coins, total = 0 , results = results)

    return results


def coins_simpler(num_coins):
    """Find change from combinations of `num_coins` of dimes and pennies.

    This should return a set of the unique amounts of change possible.
    
        >>> coins_simpler(0) == {0}
        True

        >>> coins_simpler(1) == {1, 10}
        True

        >>> coins_simpler(2) == {2, 11, 20}
        True

        >>> coins_simpler(3) == {3, 12, 21, 30}
        True

        >>> coins_simpler(4) == {4, 13, 22, 31, 40}
        True

    Let's make sure it works when we can spend over 10 pennies::

        >>> coins_simpler(11) == {65, 101, 38, 74, 11, 110, 47, 83, 20, 56, 92, 29}
        True

    """ 

    results = set()

    for npennies in range(num_coins + 1) : 
        ndimes = num_coins - npennies 
        results.add(npennies + (ndimes * 10) )

    return results


if __name__ == "__main__" : 

    import doctest 

    results = doctest.testmod()

    if results.failed == 0 : 
        print("ALL TESTS PASSED")
