# SOLVED!
"""
Problem:
    Given a set of distinct integers, nums, return all possible
    subsets (the power set)
    
    Note: 
        The solution must not contain duplicate subsets
        and ordering does not matter. 
        
    
Example:
    Input: nums = [1, 2, 3]
    Output: [[3], [1], [2], [1, 2, 3], [1, 3], [2, 3], [1, 2], []]
"""


def subset(s):
    s_len = len(s)
    
    all_subsets = [[]]
    
    power = pow(2, s_len) # size of a subset
    
    for n in range(1, power):
        subset = []
        index = s_len - 1 # index to pick the character from
        # using the knowledge of binary conversion to the advantage here
        # if s = "abcd" => power = 2^len(s) = 16
        
        # say n = 2; 2 == 0010 base 2.
        # hence pick the 3 character
        # say n = 7; 7 == 0111 base 2.
        # hence pick only the last 3 characters
        while n > 0:
            rem, n = n % 2, n // 2 # remainder, quotient
            if rem == 1:
                subset.append(s[index])
            index -= 1
        all_subsets.append(subset)
    return all_subsets


if __name__ == "__main__":
    s = [1, 2, 3]
    print(subset(s))
