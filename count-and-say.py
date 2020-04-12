# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 22:30:33 2020

@author: johnoyegbite
"""
# SOLVED
"""
Problem:
    The count-and-say sequence is the sequence of integers with the first five
    terms as following:

    1.     1
    2.     11
    3.     21
    4.     1211
    5.     111221

    1 is read off as "one 1" or 11.
    11 is read off as "two 1s" or 21.
    21 is read off as "one 2, then one 1" or 1211.

    Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the
    count-and-say sequence.
    You can do so recursively, in other words from the previous member read
    off the digits, counting the number of digits in groups of the same digit.

    Note: Each term of the sequence of integers will be represented
          as a string.

Example 1:
    Input: 1
    Output: "1"
    Explanation: This is the base case.

Example 2:
    Input: 4
    Output: "1211"
    Explanation: For n = 3 the term was "21" in which we have two groups "2"
    and "1", "2" can be read as "12" which means frequency = 1 and value = 2,
    the same way "1" is read as "11", so the answer is the concatenation of
    "12" and "11" which is "1211".
"""


def compress(string):
    if not len(string):
        return ""
    new_string = []
    count = 0
    i = 0
    s = string[0]

    while i < len(string):
        if s == string[i]:
            count += 1
        else:
            new_string.append(str(count))
            new_string.append(s)
            s = string[i]
            count = 1
        i += 1

    if count > 0:
        new_string.append(str(count))
        new_string.append(s)

    return ''.join(new_string)


def countAndSay(n):
    """
    :type n: int
    :rtype: str
    """
    prev_num = 1
    prev_str = "1"

    while prev_num < n:
        prev_num += 1
        prev_str = compress(prev_str)

    return prev_str


n = 6
print(countAndSay(n))
