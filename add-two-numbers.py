# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 04:13:59 2019

@author: USER
"""
# SOLVED!
"""
Problem Description:
    You are given two non-empty linked lists representing two non-negative integers.
    The digits are stored in reverse order and each of their nodes contain a single digit. 
    Add the two numbers and return it as a linked list.

    You may assume the two numbers do not contain any leading zero, except
    the number 0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

Explanation: 342 + 465 = 807.

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
def add_list_node(l, quot, l3_list):
     while l:
         val = l.val + quot
         rem, quot = val % 10, val // 10
         l3_list.append(rem)
         l = l.next
     return quot
 
def addTwoNumbers(l1, l2):
     """
     :type l1: ListNode
     :type l2: ListNode
     :rtype: ListNode
     """
     quot = 0 # to track the carry over
     l3_list = [] # list to store the added numbers
     while l1 and l2:
         val = l1.val + l2.val + quot
         rem, quot = val % 10, val // 10
         l3_list.append(rem)
         l1 = l1.next
         l2 = l2.next
        
     # Go ahead and add the remaining number in ListNode l1.
     # also return if any, the quotient that remains to be used by l2
     quot = add_list_node(l1, quot, l3_list)
     
     # Go ahead and add the remaining number in ListNode l2.
     # also return if any, the quotient that remains to be appended to l3_list
     quot = add_list_node(l2, quot, l3_list)
         
     if quot > 0: # if the carry over is 0 then nothing is to carried over
         l3_list.append(quot) # a carry over might still be left
         
     l3 = ListNode(l3_list[0]) # first create the head of l3
     head = l3
     for i, val in enumerate(l3_list):
         if i > 0:
             node = ListNode(val)
             l3.next = node
             l3 = l3.next
     return head