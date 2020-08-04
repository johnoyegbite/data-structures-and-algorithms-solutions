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
    6.     312211
    7.     13112221
    8.     1113213211
    9.     31131211131221
    10.    13211211123113112211
    11.    11131221123112122113212221
    12.    3113112221121221121122211212113211
    13.    132113213221121122211221322112111221131221
    14.    111312211312111322211221322122111322211231222113112211
    15.    31131122211211123112322122111322112231123221121311322112212221
    16.    1321132132211231121321121322112131132221221321121322211211132113222122113211

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
    "21 would give 1211"
    "1211 would give 111221"
    "111221 would give 312211"
    "312211 would give 13112221"

    if not len(string):
        return ""
    new_string_list = []

    # pick the first character.
    s = string[0]

    # to keep track of how many times you have seen character 's' until you
    # meet a new character.
    count = 0

    i = 0
    while i < len(string):
        # keep counting till you meet a new character
        if s == string[i]:
            count += 1

        # if you meet a new character,
        # 1. store the count (how many times you have seen that character)
        # 2. store the character
        # PS: The order above matters.
        else:
            new_string_list.append(str(count))  # (1)
            new_string_list.append(s)  # (2)
            s = string[i]  # Now, get the new character that we are to count
            count = 1  # This is the first time we have seen it.
        i += 1

    # The else block above won't allow me to store the count for the last
    # character since we are not going to meet a new character that would allow
    # me to store it. Hence I store it after the loop.
    if count > 0:
        new_string_list.append(str(count))
        new_string_list.append(s)

    # I used list to store instead of string,
    # so as to improve the time complexity.
    return ''.join(new_string_list)


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
