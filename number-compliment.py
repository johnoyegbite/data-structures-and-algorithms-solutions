# -*- coding: utf-8 -*-
"""
Created on Mon May  4 13:40:30 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Given a positive integer, output its complement number.
    The complement strategy is to flip the bits of its binary representation.


Example 1:
    Input: 5
    Output: 2
    Explanation:
        The binary representation of 5 is 101 (no leading zero bits),
        and its complement is 010. So you need to output 2.

Example 2:
    Input: 1
    Output: 0
    Explanation:
        The binary representation of 1 is 1 (no leading zero bits),
        and its complement is 0. So you need to output 0.

Note:
    The given integer is guaranteed to fit within the range of a 32-bit signed
    integer.
    You could assume no leading zero bit in the integer’s binary representation
    This question is the same as 1009:
        https://leetcode.com/problems/complement-of-base-10-integer/
"""
"""
Explanation:
    We are going to consider a pattern.

    let num = n
    let compliment = c

    n   | n in base 2 | flip base | c
 -----------------------------------------
    1   |           1 |         0 | 0
    2   |          10 |         1 | 1
    3   |          11 |         0 | 0
    4   |         100 |        11 | 3
    5   |         101 |        10 | 2
    6   |         110 |         1 | 1
    7   |         111 |         0 | 0
    8   |        1000 |       111 | 7
    9   |        1001 |       110 | 6
   10   |        1010 |       101 | 5
   11   |        1011 |       100 | 4
   12   |        1100 |        11 | 3

   Using some cases:
       also, let p be the maximum power of 2 you can get from n
       and let c be the compliment of n.

    n  |      n in powers of  2     | c |  c in powers of 2
 -----------------------------------------------------------------------
    4  | 2^2 + 0 = 2^2 + (4  - 2^2) | 3 | 2^2 - 1 = 2^2 - (4  - 2^2 + 1)
    5  | 2^2 + 1 = 2^2 + (5  - 2^2) | 2 | 2^2 - 2 = 2^2 - (5  - 2^2 + 1)
    6  | 2^2 + 2 = 2^2 + (6  - 2^2) | 1 | 2^2 - 3 = 2^2 - (6  - 2^2 + 1)
    7  | 2^2 + 3 = 2^2 + (7  - 2^2) | 0 | 2^2 - 4 = 2^2 - (7  - 2^2 + 1)
    8  | 2^3 + 0 = 2^3 + (8  - 2^3) | 7 | 2^3 - 1 = 2^3 - (8  - 2^3 + 1)
    9  | 2^3 + 1 = 2^3 + (9  - 2^3) | 6 | 2^3 - 2 = 2^3 - (9  - 2^3 + 1)
   10  | 2^3 + 2 = 2^3 + (10 - 2^3) | 5 | 2^3 - 3 = 2^3 - (10 - 2^3 + 1)
   11  | 2^3 + 3 = 2^3 + (11 - 2^3) | 4 | 2^3 - 4 = 2^3 - (11 - 2^3 + 1)
   12  | 2^3 + 4 = 2^3 + (12 - 2^3) | 3 | 2^3 - 5 = 2^3 - (12 - 2^3 + 1)
   '                   '              '              '
   '                   '              '              '
   '                   '              '              '
   k   | 2^a + b = 2^a + c          | m | 2^3 - (b + 1) = 2^3 - (c + 1)
   '                   '              '              '
   '                   '              '              '
   '                   '              '              '
   n   |  2^p + (n - 2^p)           | c | 2^p + (n - 2^p + 1) = (2*2^p) - (n+1)


   Hence the compliment of n, c = (2*2^p) - (n+1);

"""


class Solution:
    def powerOf2(self, num):
        power = 0
        while num >> 1 > 0:
            num >>= 1
            power += 1
        return power

    def findComplement(self, num: int) -> int:
        pow_of_2 = self.powerOf2(num)
        print(pow_of_2)
        print(2**pow_of_2)
        print(2*2**pow_of_2)
        return (2*2**pow_of_2) - (num + 1)


def findComplement(num: int) -> int:
    # convert num to 1's (when expressed in binary) and then XOR it with the
    # orginal num.

    # Say num = 10 (1010 in binary)
    # => num.bit_length() == 4
    # => 2**4 - 1 = 15 (1111 in binary)
    # => 1111 ^ 1010 == 101

    # because bitwise '^' operator convert bit of the same value to 0 else 1
    # i.e 1 ^ 1 = 0
    #     0 ^ 0 = 0
    #     1 ^ 0 = 1
    #     0 ^ 1 = 1
    return (2**num.bit_length()-1) ^ num


if __name__ == "__main__":
    s = Solution()
    num = 2147483647
    print(findComplement(7))
