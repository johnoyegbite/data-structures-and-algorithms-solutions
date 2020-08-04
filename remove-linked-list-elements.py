# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 13:39:13 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Remove all elements from a linked list of integers that have value val.

Example:
    Input:  1->2->6->3->4->5->6, val = 6
    Output: 1->2->3->4->5
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def removeElements(head, val):
    """
    :type head: ListNode
    :type val: int
    :rtype: ListNode
    """
    # =>
    # head =>
    # 1 -> 1 -> 2 -> 3 -> 4 -> 4-> 4 -> 5 -> 6

    # Store the first node that doesn't have its value as val,
    # so as to return the node as head node later on.
    while head and head.val == val:
        head = head.next
    # =>
    # head =>
    # 2 -> 3 -> 4 -> 4-> 4 -> 5 -> 6

    if head:
        prev_node = head  # ensure the previous node starts from head.
        current_node = head.next
        # =>
        # p    c
        # 2 -> 3 -> 4 -> 4-> 4 -> 5 -> 6
        while current_node:
            # =>
            #      p    c
            # 2 -> 3 -> 4 -> 4-> 4 -> 5 -> 6
            # remove successive current nodes that has its val == val.
            while current_node and current_node.val == val:
                current_node = current_node.next
            # from the immediate loop above,
            # it implies that the resulting current node might be None or
            # its val != val.
            # =>
            #      p                  c
            # 2 -> 3 -> 4 -> 4-> 4 -> 5 -> 6

            # Since the previous node stored is defined,
            # 1. point the previous node to the current node
            #    to delete "intenal" nodes.
            # 2. set the previous node to the current node.
            prev_node.next = current_node
            prev_node = current_node
            # =>
            #           p
            #           c
            # 2 -> 3 -> 5 -> 6

            if prev_node:
                current_node = prev_node.next
            # =>
            #           p    c
            # 2 -> 3 -> 5 -> 6

    return head
