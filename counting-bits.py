# -*- coding: utf-8 -*-
"""
Created on Thu May 28 21:55:39 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Given a non negative integer number num. For every numbers i in the range
    0 ≤ i ≤ num calculate the number of 1's in their binary representation and
    return them as an array.

Example 1:
    Input: 2
    Output: [0,1,1]

Example 2:
    Input: 5
    Output: [0,1,1,2,1,2]

Follow up:
    It is very easy to come up with a solution with run time
    O(n*sizeof(integer)).
    But can you do it in linear time O(n) /possibly in a single pass?
    Space complexity should be O(n).
    Can you do it like a boss? Do it without using any builtin function like
    __builtin_popcount in c++ or in any other language.
"""


class Solution:
    def countBits(self, num):
        """
        type num: int
        rtype: List[int]
        """
        # the caret sign points to the least significant 1 bit
#         num             = ... 1 1 0 1 0 0
#                                     ^

#         # note that for (num - 1)
#         # 1. all the bits to the left of '^' remains the same
#         # 2. all the bits to the right is flipped
#         # 3. the bit at that '^' position is flipped too
#         num - 1         = ... 1 1 0 0 1 1

#         # note that (num & (num - 1)) and num differs by just 1 bit
#         # This means that to count the number of bits in n, we just have
#         # to add 1 to the number of bits in (n & (n - 1)) since they just
#         # differ by 1.
#         num & (num - 1) = ... 1 1 0 0 0 0

        counts = [0]
        for n in range(1, num+1):
            counts.append(counts[n & n-1] + 1)
        return counts
