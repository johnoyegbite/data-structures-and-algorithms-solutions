# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 12:57:32 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Given a non-empty list of words, return the k most frequent elements.

    Your answer should be sorted by frequency from highest to lowest. 
    If two words have the same frequency, then the word with the lower 
    alphabetical order comes first.

Example 1:
    Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
    Output: ["i", "love"]
    Explanation: 
        "i" and "love" are the two most frequent words.
        Note that "i" comes before "love" due to a lower alphabetical order.

Example 2:
    Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
    Output: ["the", "is", "sunny", "day"]
    Explanation: 
        "the", "is", "sunny" and "day" are the four most frequent words,
        with the number of occurrence being 4, 3, 2 and 1 respectively.
Note:
    You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
    Input words contain only lowercase letters.

Follow up:
    Try to solve it in O(n log k) time and O(n) extra space.
"""

def get_frequency(words):
    words_freq = {}
    for word in words:
        words_freq[word] = words_freq.get(word, 0) + 1
    return words_freq

def words_for_best(best, words_freq):
    words_best = []
    for word in words_freq:
        if words_freq[word] == best:
            words_best.append(word)
    return sorted(words_best)

def topKFrequent(words, k):
    """
    :type words: List[str]
    :type k: int
    :rtype: List[str]
    """
    # write your code here
    words_freq = get_frequency(words)

    top_k_frequent = []

    done = False
    # also check if there is a key in the dictionary to proceed
    while not done and words_freq: 
        words_freq_values = words_freq.values()
        maximum = max(words_freq_values)

        words_for_max = words_for_best(maximum, words_freq)

        for word in words_for_max:
            if k < 1:
                done = True
                break
            top_k_frequent.append(word)
            del words_freq[word]
            k -= 1

    return top_k_frequent


if __name__ == "__main__":
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 3
    print(topKFrequent(words, k))