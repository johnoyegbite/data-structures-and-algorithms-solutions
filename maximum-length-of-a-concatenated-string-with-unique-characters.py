# -*- coding: utf-8 -*-
"""
Created on Sat May 23 00:02:03 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Given an array of strings arr. String s is a concatenation of a
    sub-sequence of arr which have unique characters.

    Return the maximum possible length of s.


Example 1:
    Input: arr = ["un","iq","ue"]
    Output: 4
    Explanation: All possible concatenations are "","un","iq","ue","uniq" and
        "ique". Maximum length is 4.

Example 2:
    Input: arr = ["cha","r","act","ers"]
    Output: 6
    Explanation: Possible solutions are "chaers" and "acters".

Example 3:
    Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
    Output: 26

Constraints:
    1 <= arr.length <= 16
    1 <= arr[i].length <= 26
    arr[i] contains only lower case English letters.
"""


class Solution:
    def unique(self, subset):
        orig_max = 0
        for sub in subset:
            orig_max += len(sub)
        return orig_max == len(set(''.join(subset))), orig_max

    def maxLength(self, arr) -> int:
        # Generate power set, find if all the string in the
        # subset in the power set is unique, then update the maximum.
        maximum = 0

        # loop through the size of the list i.e. i = 0, 1, 2, ..., len(L)-1.
        for i in range(1, 1 << len(arr)):  # 1 << len(L) implies 1*(2**len(L))
            index, subset = 0, []  # subset: a new subset for each i.

            # convert each i to base 2 and if remainder is unit at any point,
            # insert to the subset.
            while i > 0:
                if i % 2 == 1:
                    subset.append(arr[index])
                i >>= 1  # converting to base 2
                index += 1
            unique_details = self.unique(subset)
            if unique_details[0]:
                maximum = max(maximum, unique_details[1])
            # power_set.append(subset)
        return maximum


def maxLength(self, arr) -> int:
    unique_sets = [set()]

    for string in arr:
        if len(string) != len(set(string)):
            continue
        string_set = set(string)
        for unique_set in unique_sets[:]:
            if unique_set & string_set:
                continue
            unique_sets.append(unique_set | string_set)

    return max(len(unique) for unique in unique_sets)


if __name__ == "__main__":
    s = Solution()
    arr = ["cha", "r", "act", "ers"]  # 6
    arr = ["a", "abc", "d", "de", "def"]  # 6
    arr = ["un", "iq", "ue"]  # 4
    print(s.maxLength(arr))
