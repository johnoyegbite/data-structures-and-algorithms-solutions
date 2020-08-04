# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 20:03:40 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    You are given a doubly linked list which in addition to the next and
    previous pointers, it could have a child pointer, which may or may not
    point to a separate doubly linked list.
    These child lists may have one or more children of their own, and so on,
    to produce a multilevel data structure, as shown in the example below.

    Flatten the list so that all the nodes appear in a single-level,
    doubly linked list. You are given the head of the first level of the list.


Example 1:
    Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
    Output: [1,2,3,7,8,11,12,9,10,4,5,6]
    Explanation:
        The multilevel linked list in the input is as follows:
            1---2---3---4---5---6--NULL
                    |
                    7---8---9---10--NULL
                        |
                        11--12--NULL

    After flattening the multilevel linked list it becomes:
        1---2---3---7---8---11---12---9---10---4---5---6--NULL

Example 2:
    Input: head = [1,2,null,3]
    Output: [1,3,2]
    Explanation:
        The input multilevel linked list is as follows:

            1---2---NULL
            |
            3---NULL
Example 3:
    Input: head = []
    Output: []


How multilevel linked list is represented in test case:

We use the multilevel linked list from Example 1 above:

 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL

The serialization of each level is as follows:
    [1,2,3,4,5,6,null]
    [7,8,9,10,null]
    [11,12,null]

To serialize all levels together we will add nulls in each level to signify no
node connects to the upper node of the previous level. The serialization
becomes:
    [1,2,3,4,5,6,null]
    [null,null,7,8,9,10,null]
    [null,11,12,null]

Merging the serialization of each level and removing trailing nulls we obtain:
    [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12] 

Constraints:
    Number of Nodes will not exceed 1000.
    1 <= Node.val <= 10^5
"""


# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def serialize(self, node: 'Node', flattened) -> None:
        # -> base case
        # exit the recursive call if we can't find
        # a node to go through
        if not node:
            return

        flattened.append(node)

        # First serialize or go through this node's child
        if node.child:
            self.serialize(node.child, flattened)

        # then serialize or go through the node's next element
        if node.next:
            self.serialize(node.next, flattened)

        # after serializing the node's child and next element,
        # set the prev, next and child's node to null
        # to set default for each node
        node.prev = None
        node.next = None
        node.child = None
        return

    def flatten(self, head: 'Node') -> 'Node':
        # init an array to store the nodes to be
        # flattened
        flattened = []

        # first serialize
        # i.e append each node to an array according
        # to the spec. which is children first before
        # next node.
        self.serialize(head, flattened)

        # if after serializing we can't find any element
        # then the head parameter is empty, so return None
        if not flattened:
            return None

        # after serializing and array is not empty,
        # for every node-element in the array,
        # the previous element is the previous node
        # and the next element is the next node
        for i, node in enumerate(flattened):
            if i > 0:
                node.prev = flattened[i-1]
            if (i + 1) < len(flattened):
                node.next = flattened[i+1]
        # return the first element which would be the head
        return flattened[0]
