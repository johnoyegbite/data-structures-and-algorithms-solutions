# -*- coding: utf-8 -*-
"""
Created on Mon May 18 21:48:35 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Given two strings s1 and s2, write a function to return true if s2 contains
    the permutation of s1. In other words, one of the first string's
    permutations is the substring of the second string.


Example 1:
    Input: s1 = "ab" s2 = "eidbaooo"
    Output: True
    Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
    Input:s1= "ab" s2 = "eidboaoo"
    Output: False

Note:
    The input strings only contain lower case letters.
    The length of both given strings is in range [1, 10,000].
"""


class Solution:
    def matches(self, s1_d, s2):
        s2_d = {}
        for char in s2:
            s2_d[char] = s2_d.get(char, 0) + 1
        for char in s1_d:
            if char not in s2_d or s1_d[char] != s2_d[char]:
                return False
        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:  # TLE
        s1_len = len(s1)
        if s1_len > len(s2):
            return False
        s1_d = {}
        for char in s1:
            s1_d[char] = s1_d.get(char, 0) + 1

        # We consider every possible substring of s2 of the same length as
        # that of s1, find its corresponding hashmap as well.
        # If the two hashmaps obtained are identical for any such window,
        # we can conclude that s1's permutation is a substring of s2,
        # otherwise not.
        for i, char in enumerate(s2):
            curr_s2 = s2[i:i+s1_len]
            if self.matches(s1_d, curr_s2):
                return True
        return False


# Method 2: Accepted!
def matches(s1_window, s2_window):
    for i in range(len(s1_window)):
        if s1_window[i] != s2_window[i]:
            return False
    return True


def checkInclusion(s1: str, s2: str) -> bool:
    s1_len = len(s1)
    if s1_len > len(s2):
        return False

    # Create arrays for s1 and s2 that stores the position of the character in
    # the alphabet instead of the character itself.
    # i.e. 0 rep 'a', 1 rep 'b', 2 rep 'c', ..., 25 rep 'z'
    s1_arr = [ord(x)-ord('a') for x in s1]
    s2_arr = [ord(x)-ord('a') for x in s2]
    # print('s1-arr:', s1_arr)
    # print('s2-arr:', s2_arr)
    # print()

    # since s1 can only contain characters from 'a' to 'z' (but we have
    # represented it from 0 to 25), create an array to store frequency of
    # character that would be encountered.
    s1_window = [0] * 26
    for char_val in s1_arr:
        s1_window[char_val] += 1
    # print("s1-window:", s1_window)
    # print('------')

    # since s2 can also only contain characters from 'a' to 'z' (but we have
    # represented it from 0 to 25), create an array to store frequency of
    # character that would be encountered.
    s2_window = [0] * 26
    for i, char_val in enumerate(s2_arr):
        s2_window[char_val] += 1

        # This is to make sure that the frequency of characters in s2_window
        # doesn't exceed the length of s1.
        if i >= len(s1_arr):
            # Say s1_arr = [0, 1], s2_arr = [15, 8, 4, 1, 14, 0, 14, 11]
            # if i >= len(s1_arr) => i >= 2, this means our pointer is at 4
            # s2_arr = [15, 8, 4, 1, 14, 0, 14, 11]
            #                  ^
            # Now, we remove/reduce the frequency of 15 in the s2_window,
            # so s2_window would now contain  8 and 4 (which is the length of
            # s1).
            # if the pointer moves to 1
            # s2_arr = [15, 8, 4, 1, 14, 0, 14, 11]
            #                     ^
            # Now, we remove/reduce the frequency of 8 in the s2_window,
            # so s2_window would now contain  4 and 1 (which is the length of
            # s1). And so on. Hence, maintaining window of lenght equals to s1
            s2_window[s2_arr[i - len(s1_arr)]] -= 1

        if matches(s1_window, s2_window):  # same as s1_window == s2_window
            return True
        # print('s2-window:', s2_window)
    return False


if __name__ == "__main__":
    s = Solution()
    s1 = "ab"
    s2 = "pieboaol"
    s2 = "eidbaooo"
    print(checkInclusion(s1, s2))
