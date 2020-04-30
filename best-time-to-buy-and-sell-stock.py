# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 14:21:57 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Say you have an array for which the ith element is
    the price of a given stock on day i.

    If you were only permitted to complete at most one transaction
    (ie, buy one and sell one share of the stock),
    design an algorithm to find the maximum profit.


Example 1
    Input: [3, 2, 3, 1, 2]
    Output: 1
    Explanation: You can buy at the third day and then sell it at the 4th day.
    The profit is 2 - 1 = 1

Example 2
    Input: [1, 2, 3, 4, 5]
    Output: 4
    Explanation: You can buy at the 0th day and then sell it at the 4th day.
    The profit is 5 - 1 = 4

Example 3
    Input: [5, 4, 3, 2, 1]
    Output: 0
    Explanation: You can do nothing and get nothing.
"""


def maxProfit(prices):
    # write your code here

    # 5, 7, 8, 11, 2, 20

    # min_prev_stock = 5

    # 5 & 7 = 2
    # 7 & 8 = 1
    # 8 & 11 = 3 also 5 & 11 = 6
    # 11 & 2 = --
    # 2 & 20 = 18

    min_prev_stock = prices[0]
    total_max = 0
    i = 0
    while i < len(prices) - 1:
        buy = prices[i]
        sell = prices[i+1]
        min_prev_stock = min(min_prev_stock, buy)
        if buy <= sell:
            curr_max = sell - buy
            total_max = max(total_max, curr_max)
            curr_max = sell - min_prev_stock
            total_max = max(total_max, curr_max)
        i += 1
    return total_max


if __name__ == "__main__":
    prices = [3, 2, 3, 1, 2]
    prices = [1, 2, 3, 4, 5]
    print(maxProfit(prices))
