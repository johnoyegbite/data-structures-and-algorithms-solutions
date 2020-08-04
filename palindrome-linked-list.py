# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 01:54:21 2020

@author: johnoyegbite
"""
# SOLVED!  faster than 91.10% of Python3 online submissions.
"""
Prolem:
    Given a singly linked list, determine if it is a palindrome.

Example 1:
    Input: 1->2
    Output: false

Example 2:
    Input: 1->2->2->1
    Output: true

Follow up:
    Could you do it in O(n) time and O(1) space?
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        singly = []
        curr = head
        while curr:
            singly.append(curr.val)
            curr = curr.next
        return singly == singly[::-1]
