# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 01:24:54 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    In an alien language, surprisingly they also use english lowercase letters,
    but possibly in a different order. The order of the alphabet is some
    permutation of lowercase letters.

    Given a sequence of words written in the alien language, and the order of
    the alphabet, return true if and only if the given words are sorted
    lexicographicaly in this alien language.

Example 1:
    Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
    Output: true
    Explanation: As 'h' comes before 'l' in this language, then the sequence is
        sorted.

Example 2:
    Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
    Output: false
    Explanation: As 'd' comes after 'l' in this language,
        then words[0] > words[1], hence the sequence is unsorted.

Example 3:
    Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
    Output: false
    Explanation: The first three characters "app" match, and the second string
    is shorter (in size.) According to lexicographical rules "apple" > "app",
    because 'l' > '∅', where '∅' is defined as the blank character which is
    less than any other character (More info).

Constraints:
    1 <= words.length <= 100
    1 <= words[i].length <= 20
    order.length == 26
    All characters in words[i] and order are English lowercase letters.
"""


def isAlienSorted(words, order):
    """
    :type words: List[str]
    :type order: str
    :rtype: bool
    """
    alien_alphabet = {}

    for i, letter in enumerate(order):
        alien_alphabet[letter] = i + 1

    for i in range(len(words)-1):
        first_word = words[i]
        second_word = words[i+1]

        for j in range(min(len(first_word), len(second_word))):
            print(first_word[j], second_word[j])
            if first_word[j] != second_word[j]:
                if alien_alphabet[first_word[j]] > alien_alphabet[second_word[j]]:
                    return False
                break
        else:
            if len(first_word) > len(second_word):
                return False

    return True


if __name__ == "__main__":
    words = ["apple", "app"]
    order = "abcdefghijklmnopqrstuvwxyz"
    print(isAlienSorted(words, order))
