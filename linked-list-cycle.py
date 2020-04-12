# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 23:03:03 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Given a linked list, determine if it has a cycle in it.


Example 1:
	Input: 21->10->4->5,  then tail connects to node index 1(value 10).
	Output: true
		
Example 2:
	Input: 21->10->4->5->null
	Output: false
	
Challenge:
    Follow up:
        Can you solve it without using extra space?
"""
"""
Intuition:
    Imagine two runners running on a track at different speed. 
    What happens when the track is actually a circle?

Algorithm:
    The space complexity can be reduced to O(1)O(1) by considering two pointers
    at different speed - a slow pointer and a fast pointer. 
    The slow pointer moves one step at a time while the fast pointer moves two 
    steps at a time.

    If there is no cycle in the list, the fast pointer will eventually reach 
    the end and we can return false in this case.

    Now consider a cyclic list and imagine the slow and fast pointers are two 
    runners racing around a circle track. The fast runner will eventually meet
    the slow runner. Why? 
    Consider this case (we name it case A) - The fast runner is just one step 
    behind the slow runner. In the next iteration, they both increment one and
    two steps respectively and meet each other.
"""
"""
Definition of ListNode
"""


class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


"""
@param head: The first node of linked list.
@return: True if it has a cycle, or false
"""
def hasCycle(head):
    # write your code here
    if not head:
        return False
        
    slow = head
    fast = head.next
    
    while slow != fast: # while fast has not catched up with slow
        if not fast  or not fast.next:
            return False
        slow = slow.next # move one step at a time
        fast = fast.next.next # move two steps at a time
        
    return True