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


class Solution:
    def frequencySort(self, s: str) -> str:
        """
        :type s: str
        :rtype: str
        """
        # Get the frequency of each character.
        char_freq = {}
        for char in s:
            char_freq[char] = char_freq.get(char, 0) + 1

        # Store the [frequency, character] in a list an sort in descending
        # order. i.e. the character with the highest frequency comes first.
        sorted_s = []
        for char in char_freq:
            sorted_s.append([char_freq[char], char])
        # Here we sort based on the frequency which is at index 0 of every
        # [frequency, character] and we also reverse it because the default is
        # ascending and we require descending (highest to lowest).
        sorted_s.sort(key=lambda x: x[0], reverse=True)

        # Replace each [frequency, character] with [character*frequency].
        # i.e. [3, 'a'] would be replaced by 'aaa' (i.e. 'a'*3).
        for i in range(len(sorted_s)):
            sorted_s[i] = sorted_s[i][1]*sorted_s[i][0]

        return ''.join(sorted_s)


if __name__ == "__main__":
    s = "eert"
    print(Solution().frequencySort(s))
