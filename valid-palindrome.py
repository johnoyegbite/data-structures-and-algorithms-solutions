# -*- coding: utf-8 -*-
"""
Created on Tue May 12 11:07:25 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Given a string, determine if it is a palindrome, considering only
    alphanumeric characters and ignoring cases.

    Note: For the purpose of this problem, we define empty string as valid
    palindrome.

Example 1:
    Input: "A man, a plan, a canal: Panama"
    Output: true

Example 2:
    Input: "race a car"
    Output: false
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [char.lower() for char in s if char.isalnum()]
        i = 0
        j = len(s) - 1
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


if __name__ == "__main__":
    s = Solution()
    s = "race a car"
    print(s.isPalindrome(s))
