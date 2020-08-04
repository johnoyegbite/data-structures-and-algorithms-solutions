# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 11:32:13 2020

@author: johnoyegbite
"""
# SOLVED
"""
Problem:
    Given a non-empty, singly linked list with head node head,
    return a middle node of linked list.

    If there are two middle nodes, return the second middle node.

Example 1:
    Input: [1,2,3,4,5]
    Output: Node 3 from this list (Serialization: [3,4,5])
    The returned node has value 3.
    (The judge's serialization of this node is [3,4,5]).
     Note that we returned a ListNode object ans, such that:
         ans.val = 3, ans.next.val = 4, ans.next.next.val = 5,
         and ans.next.next.next = NULL.

Example 2:
    Input: [1,2,3,4,5,6]
    Output: Node 4 from this list (Serialization: [4,5,6])
    Since the list has two middle nodes with values 3 and 4,
    we return the second one.

Note:
    The number of nodes in the given list will be between 1 and 100.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def middleNode(head):  # O(n+n/2) => O(n)
    """
    :type head: ListNode
    :rtype: ListNode
    """
    num_of_nodes = 1
    current = head
    while current.next:
        current = current.next
        num_of_nodes += 1

    mid = 0

    current = head
    while mid < (num_of_nodes // 2):
        current = current.next
        mid += 1

    return current


def middleNode2(head):  # O(n/2) => O(n); but a little significant change
    """
    :type head: ListNode
    :rtype: ListNode
    """
    mid = head
    end = head

    # Using 2 pointers (*, *);The 2nd pointer moves double distance of the 1st

    # [1]  # Correct

    # [1, 2]  # Correct

    #        *
    # [1, 2, 3, 4, 5]  # Correct
    #              *

    # [1, 2, 3, 4, 5, 6]  # Correct

    # [1, 2, 3, 4, 5, 6, 7, 8, 9]  # Correct

    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Correct

    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
    #      14, 15, 16, 17, 18, 19, 20, 21]  # Correct

    try:
        while mid.next and end.next.next:
            mid = mid.next
            end = end.next.next

        if end.next:
            mid = mid.next
    except AttributeError:
        # Caused by end.next.next becasue end.next might be None,
        # and a NoneType can't have a ".next" (i.e, None.next doesn't exist)
        done = True  # dummy assingment so the except block would not be empty

    return mid
