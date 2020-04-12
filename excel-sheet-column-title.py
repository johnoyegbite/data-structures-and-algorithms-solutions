# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 23:43:10 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Given a positive integer, return its corresponding column title as appear
    in an Excel sheet.

    For example:
        1 -> A
        2 -> B
        3 -> C
        ...
        26 -> Z
        27 -> AA
        28 -> AB
        ...

Example 1:
    Input: 1
    Output: "A"

Example 2:
    Input: 28
    Output: "AB"

Example 3:
    Input: 701
    Output: "ZY"
"""


def convertToTitle(n):
    """
    :type n: int
    :rtype: str
    """
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # store all the alphabets with their corresponding position on the
    # alphabetical table. 1: 'A', 2: 'B', 3: 'C', etc.
    title = {i+1: s for i, s in enumerate(alpha)}
    
    # 1. convert n to base equal to the total length of alphabets (i.e, 26).
    # note that during conversion,
    # if the remainder is 0, it is also equivalent to 26; since 0 can't be
    # found in the title dictionary. You have to also reduce n by 1 to cater
    # for the just case where remainder is 0
    # Example if n = 702;  store = ""
    # => n % 26 = 0 and n // 26 = 27    store = "Z" (title[26] instead)
    # => n -= 1 => n = 26 (27-1)
    # => store = "ZZ"
    # 2. Store the remainder during conversion to represent the letter

    t = len(alpha)
    col_name = []
    while n > t:
        if n % t == 0:
            col_name.append(title[t])
            n -= 1
        else:
            col_name.append(title[n % t])
        n //= t

    if n % t == 0:
        col_name.append(title[t])
    else:
        col_name.append(title[n])

    return ''.join(col_name[::-1])


if __name__ == "__main__":
    print(convertToTitle(702))
