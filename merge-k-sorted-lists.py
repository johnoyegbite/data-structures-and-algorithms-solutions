# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 23:17:02 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Merge k sorted linked lists and return it as one sorted list.
    Analyze and describe its complexity.

Example:
    Input:
        [
            1->4->5,
            1->3->4,
            2->6
        ]
    Output: 1->1->2->3->4->4->5->6
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeKLists(self, lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    if not len(lists):
        return None

    sorted_list = []

    for list_node in lists:
        while list_node:
            sorted_list.append(list_node.val)
            list_node = list_node.next

    if not len(sorted_list):
        return None

    sorted_list.sort()

    head = ListNode(sorted_list[0])
    curr = head

    for i, val in enumerate(sorted_list):
        if i == 0:
            continue
        curr.next = ListNode(val)
        curr = curr.next

    return head
