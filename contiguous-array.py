# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 00:15:06 2020

@author: johnoyegbite
"""

# SOLVED!

"""
Problem:
    Given a binary array, find the maximum length of a contiguous subarray
    with equal number of 0 and 1.

Example 1:
    Input: [0,1]
    Output: 2
    Explanation: [0, 1] is the longest contiguous subarray with equal number
    of 0 and 1.

Example 2:
    Input: [0,1,0]
    Output: 2
    Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with
    equal number of 0 and 1.

Note: The length of the given binary array will not exceed 50,000.
"""


def findMaxLength(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max_length = 0
    count = 0
    count_axis = {0: 0}

    for i, num in enumerate(nums):
        count += num or -1  # if num is 1 add 1 or -1 if num is 0
        i = i + 1  # choose indexing at 1
        if count not in count_axis:
            count_axis[count] = i
        else:
            new_distance = i - count_axis[count]
            max_length = max(max_length, new_distance)

    return max_length


if __name__ == "__main__":
    nums = [0, 0, 0, 0, 1, 1]
    nums = [0, 0, 1, 0, 0, 0, 1, 1]
    nums = [0, 1, 1, 0, 1, 1, 1, 0]

    print(findMaxLength(nums))


"""
Solution:
    Let's have a variable count initially equals 0 and traverse through nums.
    Every time we meet a 0, we decrease count by 1, and increase count by 1
    when we meet 1. It's pretty easy to conclude that we have a contiguous
    subarray with equal number of 0 and 1 when count equals 0.

    What if we have a sequence [0, 0, 0, 0, 1, 1]? the maximum length is 4,
    the count starting from 0, will equal -1, -2, -3, -4, -3, -2, and won't
    go back to 0 again. But wait, the longest subarray with equal number of
    0 and 1 started and ended when count equals -2. We can plot the changes
    of count on a graph, as shown below. Point (0,0) indicates the initial
    value of count is 0, so we count the sequence starting from index 1.
    The longest subarray is from index 2 to 6.

          ( plot count against index; where index starts at 1)

    From above illustration, we can easily understand that two points with the
    same y-axis value indicates the sequence between these two points has
    equal number of 0 and 1.


    Another example, sequence [0, 0, 1, 0, 0, 0, 1, 1], as shown below,

          ( plot count against index; where index starts at 1)

    There are 3 points have the same y-axis value -2.
    So subarray from index 2 to 4 has equal number of 0 and 1, and subarray
    from index 4 to 8 has equal number of 0 and 1. We can add them up to form
    the longest subarray from index 2 to 8, so the maximum length of the
    subarray is 8 - 2 = 6.



    Yet another example, sequence [0, 1, 1, 0, 1, 1, 1, 0], as shown below.
    The longest subarray has the y-axis value of 0.

        ( plot count against index; where index starts at 1)
"""
