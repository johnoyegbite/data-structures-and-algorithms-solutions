# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 19:50:36 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    You are given coins of different denominations and a total amount of money
    amount.
    Write a function to compute the fewest number of coins that you need to
    make up that amount. If that amount of money cannot be made up by any
    combination of the coins, return -1.

Example 1:
    Input: coins = [1, 2, 5], amount = 11
    Output: 3
    Explanation: 11 = 5 + 5 + 1

Example 2:
    Input: coins = [2], amount = 3
    Output: -1

Note:
    You may assume that you have an infinite number of each kind of coin.
"""
from sys import maxsize


class Solution:
    def treeCount(self, amount, coins, memo={}):
        # You can also use the amount + 1 as the maximum amount to make change
        # with.
        if amount in memo:
            return memo[amount]
        if amount == 0:
            return 0
        if amount < 0:
            return maxsize

        # count = []  # this was replaced by amount_min
        amount_min = maxsize
        for coin in coins:
            fewest_num = self.treeCount(amount-coin, coins, memo)
            # count.append(fewest_num)
            amount_min = min(amount_min, fewest_num)

        # print(amount, count)
        # fewest_no = 1 + min(count)
        fewest_no = 1 + amount_min
        memo[amount] = fewest_no

        return fewest_no

    def coinChange(self, coins, amount) -> int:  # Top Down Approach.
        """
        type coins: List[int]
        type amount: int
        rtype: int
        """
        fewest_no = self.treeCount(amount, coins)
        if fewest_no < maxsize:
            return fewest_no
        return -1


# Bottom Up Approach.
# https://www.youtube.com/watch?v=jgiZlGzXMBw
def coinChange(coins, amount):
    MAX_SIZE = amount + 1
    dp = [MAX_SIZE] * (amount + 1)
    dp[0] = 0

    for i in range(amount+1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i-coin] + 1, dp[i])

    if dp[-1] >= MAX_SIZE:
        return -1
    return dp[-1]


if __name__ == "__main__":
    s = Solution()
    coins = [1, 2, 5]
    amount = 11
    # coins = [1, 2]
    # amount = 3
    # coins = [2]
    # amount = 3
    print(coinChange(coins, amount))
