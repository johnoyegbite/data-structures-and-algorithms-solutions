# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 21:41:19 2020

@author: johnoyegbite
"""
# SOLVED!

"""
Problem:
    You have two numbers represented by linked list, where each node contains
    a single digit. The digits are stored in forward order, such that the 1's
    digit is at the head of the list. Write a function that adds the two
    numbers and returns the sum as a linked list.

Example 1:
    Input: 6->1->7   2->9->5
    Output: 9->1->2

Example 2:
    Input: 1->2->3   4->5->6
    Output: 5->7->9
"""

"""
Definition of ListNode
"""


class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def reverse(l):
    # You can reverse a linked list by pointing node the previous and
    # pointing the head node to None.
    current = l
    if l:
        # first node should point to a previous node of None
        prev = None
        while current.next:
            # get next node of current node (store for later use)
            next_node = current.next
            # point the current node to the previous node
            # (which is None if current node is the head node)
            current.next = prev
            # set the next previous node equal to the current node
            prev = current
            # set current node to the the next node stored earlier
            current = next_node

        # at the end of the list, last node is connected to previous
        current.next = prev
        l = current  # new head is the last node of the list
    return l


def add_list_node(l, quot, l3_list):
    while l:
        val = l.val + quot
        rem, quot = val % 10, val // 10
        l3_list.append(rem)
        l = l.next
    return quot
 
"""
@param l1: The first list.
@param l2: The second list.
@return: the sum list of l1 and l2.
"""
def addLists2(l1, l2):
    # write your code here
    
    l1 = reverse(l1)
    l2 = reverse(l2)
    
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
    
    l3 = ListNode(l3_list[-1]) # first create the head of l3
    head = l3
    for i in range(len(l3_list)-2, -1, -1):
        val = l3_list[i]
        node = ListNode(val)
        l3.next = node
        l3 = l3.next
    return head