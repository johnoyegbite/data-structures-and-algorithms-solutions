# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 15:58:51 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Given a non-negative integer num represented as a string, remove k digits
    from the number so that the new number is the smallest possible.

Note:
    The length of num is less than 10002 and will be ≥ k.
    The given num does not contain any leading zero.

Example 1:
    Input: num = "1432219", k = 3
    Output: "1219"
    Explanation:
        Remove the three digits 4, 3, and 2 to form the new number 1219 which
        is the smallest.

Example 2:
    Input: num = "10200", k = 1
    Output: "200"
    Explanation:
        Remove the leading 1 and the number is 200. Note that the output must
        not contain leading zeroes.

Example 3:
    Input: num = "10", k = 2
    Output: "0"
    Explanation:
        Remove all the digits from the number and it is left with nothing which
        is 0.

"""


class Solution:
    def removeK(self, num, num_len, seen, k):
        if num in seen:
            return
        seen.add(num)

        if k == 0:
            return
        for p in range(num_len):
            # Neglect digit at position p or index p in num
            # (index is read from right to left)
            # Say num = 2351607498,
            # p = 0 denote remove 8(8 is at index 0 reading from right to left)
            # p = 1 denote remove 9, p = 2 denote remove 4,
            # p = 3 denote remove 7
            # and so on...
            # Say p = 2 which means remove 4,
            # num // 10**(p+1) = 2351607 =>(remove 4 and everything after)
            # num // 10**(p+1) * 10**p = 235160700
            # num % 10**p = 98 (keep everything after 4)
            # (num // 10**(p+1)) * 10**p + num % 10**p = 235160798
            new_num = (num // 10**(p+1)) * 10**p + num % 10**p

            self.smallest = min(self.smallest, new_num)
            self.removeK(new_num, num_len-1, seen, k-1)

    def removeKdigits(self, num: str, k: int) -> str:  # Time limit Exceeded
        num_len = len(num)
        if k == num_len:
            return '0'
        num_int = int(num)
        self.smallest = num_int
        seen = set()
        self.removeK(num_int, num_len, seen, k)
        return str(self.smallest)


def removeKdigits(num: str, k: int) -> str:  # Accepted
    num_len = len(num)
    # if k is the same as the length of num then just remove all the digit
    # in num.
    if k == num_len:
        return '0'

    stack = []
    for i, char in enumerate(num):
        # How big a number is depends on the left most digit,
        # if I remove the left most digit, the number would be smaller
        # so going from left to left,
        # whenever we meet a digit which is less than the previous digit,
        # discard the previous one.
        while len(stack) and stack[-1] > char and k > 0:
            stack.pop()
            k -= 1
        stack.append(char)

    # case of num = '11111' or num = '12345',
    # k would still be greater than zero.
    while k > 0:
        stack.pop()
        k -= 1

    # remove all the preceeding zeroes
    j = 0
    while j < len(stack) and stack[j] == '0':
        j += 1

    return ''.join(stack[j:]) if j < len(stack) else '0'


if __name__ == "__main__":
    s = Solution()
    num = "1432219"
    k = 3
    # num = "10200"
    # k = 1
    # num = "10"
    # k = 2
    print(s.removeKdigits(num, k))
