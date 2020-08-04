# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 21:31:52 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Given n, how many structurally unique BST's (binary search trees) that
    store values 1 ... n?

Example:
    Input: 3
    Output: 5
    Explanation:
        Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""


class Solution:
    def numTrees(self, n: int, memo={}) -> int:
        if n in memo:
            return memo[n]
        if n == 0 or n == 1:
            return 1

        total_bst = 0
        for node in range(1, n+1):
            left = self.numTrees(node - 1)
            right = self.numTrees(n - node)
            total = left * right
            total_bst += total

        memo[n] = total_bst
        return total_bst


if __name__ == "__main__":
    s = Solution()
    n = 4
    print(s.numTrees(n))
