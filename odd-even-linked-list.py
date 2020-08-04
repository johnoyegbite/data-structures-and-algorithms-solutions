# -*- coding: utf-8 -*-
"""
Created on Sun May 17 02:55:31 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Given a singly linked list, group all odd nodes together followed by the
    even nodes.
    Please note here we are talking about the node number and not the value in
    the nodes.

    You should try to do it in place. The program should run in O(1) space
    complexity and O(nodes) time complexity.

Example 1:
    Input: 1->2->3->4->5->NULL
    Output: 1->3->5->2->4->NULL

Example 2:
    Input: 2->1->3->5->6->4->7->NULL
    Output: 2->3->6->7->1->5->4->NULL

Note:
    The relative order inside both the even and odd groups should remain as it
    was in the input.
    The first node is considered odd, the second node even and so on ...
"""


"""
Explanation:
    # Try case when lenght of linked list is even
    Original: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10
    Final: 1 -> 3 -> 5 -> 7 -> 9 -> 2 -> 4 -> 6 -> 8 -> 10

    # Note the last odd would always point to the first even node
    # Hence store the first even node.
    first_even = head.next

    1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10
    => We need to connect:
        a. 2 to 4
        b. 1 to 3
        c. 3 to 2

    # Using 2nd Approach:
    # Initial assignments

    last_odd = head (keep track of 1)
    last_even = head.next (keep track of 2)
    # number immediately after last even
    odd_after_last_even = last_even.next (keep track of 3)

    last_even.next = odd_after_last_even.next  # 2 -> 4 (point 2 to 4)
    last_even = odd_after_last_even.next  # keep track of the current last even, 4
    last_odd.next = odd_after_last_even  # 1 -> 3  (that is point 1 to 3)
    odd_after_last_even.next = first_even  # 3 -> 2  (that is point 3 to 2)

    After first loop: 1 -> 3 -> 2 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10

    # Pattern is keep track of the last odd and last even before linking
    # is made.
    # You will get the definiton of of last odd and last even;
    # pay attention to the pattern
    => Now we have to connect: (also keep track of 3, 4)
        a. 4 to 6
        b. 3 to 5
        c. 5 to 2

    last_odd = odd_after_last_even (track of 3)  # last odd
    odd_after_last_even = last_even.next  (track of 5)  # number immediately after last even

    last_even.next = odd_after_last_even.next  # 4 -> 6
    last_even = odd_after_last_even.next  # keep track of the current last even, 6
    last_odd.next = odd_after_last_even  # 3 -> 5
    odd_after_last_even.next = first_even  # 5 -> 2

    After second loop: 1 -> 3 -> 5 -> 2 -> 4 -> 6 -> 7 -> 8 -> 9 -> 10

    => Now we have to connect: (also keep track of 5, 6)
        a. 6 to 8
        b. 5 to 7
        c. 7 to 2

    last_odd = odd_after_last_even (track of 5)  # last odd
    odd_after_last_even = last_even.next  (track of 7)  # number immediately after last even

    last_even.next = odd_after_last_even.next  # 6 -> 8
    last_even = odd_after_last_even.next  # keep track of the current last even, 8
    last_odd.next = odd_after_last_even  # 5 -> 7
    odd_after_last_even.next = first_even  # 7 -> 2

    After third loop: 1 -> 3 -> 5 -> 7 -> 2 -> 4 -> 6 -> 8 -> 9 -> 10

    => Now we have to connect: (also keep track of 7, 8)
        a. 8 to 10
        b. 7 to 9
        c. 9 to 2

    last_odd = odd_after_last_even (track of 7)  # last odd
    odd_after_last_even = last_even.next  (track of 9) # number immediately after last even

    last_even.next = odd_after_last_even.next  # 8 -> 10
    last_even = odd_after_last_even.next  # keep track of the current last even, 10
    last_odd.next = odd_after_last_even  # 7 -> 9
    odd_after_last_even.next = first_even  # 9 -> 2

    After fourth loop: 1 -> 3 -> 5 -> 7 -> 9 -> 2 -> 4 -> 6 -> 8 -> 10


    # Extend it to a case when length of linkedlist is odd
    : 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 11

    1 -> 3 -> 5 -> 7 -> 9 -> 2 -> 4 -> 6 -> 8 -> 10 -> 11
    => Now we have to connect: (also keep track of 9, 10)
        a. 10 to None
        b. 9 to 11
        c. 11 to 2

    last_odd = odd_after_last_even  (track of 9)  # last odd
    odd_after_last_even = last_even.next  (track of 11) # number immediately after last even

    last_even.next = odd_after_last_even.next  # 10 -> None
    last_even = odd_after_last_even.next  # keep track of the current last even, 10
    last_odd.next = odd_after_last_even  # 9 -> 11
    odd_after_last_even.next = first_even  # 11 -> 2

    After fifth loop: 1 -> 3 -> 5 -> 7 -> 9 -> 11 -> 2 -> 4 -> 6 -> 8 -> 10

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # if we have None or 1 or 1->2 only
        if not head or not head.next or not head.next.next:
            return head

        first_even = head.next

        last_odd = head
        last_even = head.next
        odd_after_last_even = last_even.next

        while odd_after_last_even:
            last_even.next = odd_after_last_even.next
            last_even = odd_after_last_even.next
            last_odd.next = odd_after_last_even
            odd_after_last_even.next = first_even

            last_odd = odd_after_last_even
            if last_even:
                odd_after_last_even = last_even.next
            else:
                odd_after_last_even = last_even

        return head
