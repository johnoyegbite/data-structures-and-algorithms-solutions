# -*- coding: utf-8 -*-
"""
Created on Sun May  3 13:24:16 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Given an arbitrary ransom note string and another string containing
    letters from all the magazines, write a function that will return true
    if the ransom note can be constructed from the magazines;
    otherwise, it will return false.

    Each letter in the magazine string can only be used once in your
    ransom note.

Note:
    You may assume that both strings contain only lowercase letters.

    canConstruct("a", "b") -> false
    canConstruct("aa", "ab") -> false
    canConstruct("aa", "aab") -> true
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_freq = {}
        for alpha in magazine:
            magazine_freq[alpha] = magazine_freq.get(alpha, 0) + 1

        for alpha in ransomNote:
            if alpha not in magazine_freq:
                return False
            magazine_freq[alpha] -= 1
            if magazine_freq[alpha] < 0:
                return False

        return True
