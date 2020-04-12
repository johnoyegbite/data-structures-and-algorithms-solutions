# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 19:15:43 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Given a linked list, swap every two adjacent nodes and return its head.

Example 1:
    Input: 1->2->3->4->null
    Output: 2->1->4->3->null

Example 2:
    Input: 5->null
    Output: 5->null

Challenge:
    Your algorithm should use only constant space. 
    You may not modify the values in the list, only nodes itself can be changed.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
# Case 1: When length of node in linked list is ODD
Before swapping:
    ------>---------    ------->--------    ----->>-----
    |              |    |              |    |          |
    |         -------->-------    ------->--------
    |         |    |    |    |    |    |    |    |     |
    1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 11 -> None
    |    |    |    |    |    |    |    |    |     |
    --<---    --<---    --<---    --<---    ---<---
    
After swapping:
    
    2 -> 1 -> 4 -> 3 -> 6 -> 5 -> 8 -> 7 -> 10 -> 9 -> 11 -> None
    
    
# Case 2: When length of node in linked list is EVEN
Before swapping:
     ------>---------    ------->--------    ----->>-----
    |              |    |              |    |          |
    |         -------->-------    ------->--------
    |         |    |    |    |    |    |    |    |     |
    1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> None
    |    |    |    |    |    |    |    |    |     |
    --<---    --<---    --<---    --<---    ---<---
    
    1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> None
    
After swapping:
    
    2 -> 1 -> 4 -> 3 -> 6 -> 5 -> 8 -> 7 -> 10 -> 9 -> None
    
The trick here is that, if we should consider "4 node at a time",
1. The 1st node is pointed to the 4th 
2. The 2nd node is pointed to the 1st 
3. The new 1st node begin with the 3rd node
4. Repeat from (1) till the end of the LinkedList

NOTE:
    If at any point, 3rd node is None (this also means 4th node does not exist),
    (Case 2: ... ->9 -> 10 -> None), 
    that means we:
        1. The 1st node is pointed to the 3rd (3rd node is None here)
        2. The 2nd node is pointed to the 1st.
        3. Break out of the loop since this denotes we have reached the end
           of the LinkedList
    
"""
def swapPairs(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    # if no element in ListNode or just one Node in ListNode
    if not head or not head.next:
        return head
    
    first = head
    new_head = first.next
    
    while first and first.next:
        second = first.next
        third = second.next
        
        if not third:
            first.next = third
            second.next = first
            break
        
        fourth = third.next
        
        if not fourth:
            first.next = third
            second.next = first
            break
        
        first.next = fourth
        second.next = first
        
        first = third
    
    return new_head
