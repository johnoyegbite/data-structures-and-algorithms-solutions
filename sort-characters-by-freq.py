# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 00:09:18 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Given a string, sort it in decreasing order based on the frequency of
    characters.

Example 1:
    Input:
        "tree"
    Output:
        "eert"
    Explanation:
        'e' appears twice while 'r' and 't' both appear once.
        So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also
        a valid answer.

Example 2:
    Input:
        "cccaaa"
    Output:
        "cccaaa"
    Explanation:
        Both 'c' and 'a' appear three times, so "aaaccc" is also a valid
        answer.
        Note that "cacaca" is incorrect, as the same characters must be
        together.

Example 3:
    Input:
        "Aabb"
    Output:
        "bbAa"
    Explanation:
        "bbaA" is also a valid answer, but "Aabb" is incorrect.
    Note that 'A' and 'a' are treated as two different characters.
"""


def sort_from_best(best, char_freq, sorted_s):
    for char in char_freq:
        if char_freq[char] == best:
            sorted_s.append(best*char)


def frequencySort(s):
    """
    :type s: str
    :rtype: str
    """
    char_freq = {}

    for char in s:
        char_freq[char] = char_freq.get(char, 0) + 1

    sorted_s = []

    decreasing_best = sorted(list(set(char_freq.values())), reverse=True)

    for best in decreasing_best:
        sort_from_best(best, char_freq, sorted_s)

    return ''.join(sorted_s)


if __name__ == "__main__":
    s = "eert"
    print(frequencySort(s))
