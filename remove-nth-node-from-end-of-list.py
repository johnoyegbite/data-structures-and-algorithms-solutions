# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 17:00:00 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Given a linked list, remove the n-th node from the end of list and return its head.

Example:
    Given linked list: 1->2->3->4->5, and n = 2.

    After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
    Given n will always be valid.

Follow up:
    Could you do this in one pass?
"""

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
    
    def append(self, node):
        current = self.head
        if not self.head:
            self.head = node
        else:
            while current.next:
                current = current.next
            current.next = node
        return self.head
            
    # DONE in Two Pass
    # def removeNthFromEnd(self, n):
    #     """
    #     :type head: ListNode
    #     :type n: int
    #     :rtype: ListNode
    #     """
    #     current = self.head 
    #     if self.head:
    #         count = 0
    #         while current.next:
    #             current = current.next
    #             count += 1
    #         count += 1
    #         print(count)
    #         node_position = count - n + 1
    #         print(node_position)
            
    #         current = self.head
    #         if node_position == 1:
    #             current = current.next
    #             self.head = current
    #         else:
    #             for position in range(1, node_position-1):
    #                 current = current.next # get node at (position - 1)
    #             print("pos - 1:", current.data)
    #             node_at_plus_1 = current.next.next # get node at (position + 1)
    #             print("pos + 1:", node_at_plus_1.data)
    #             current.next = node_at_plus_1
    
    # Done in One pass
    def removeNthFromEnd(self, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # using two pointers to navigate through the list
        # make sure the distance between the two pointer (first and second),
        # is n.
        # When the second pointer is at the end of the list, then the distance
        # between the two pointers would have make sure the first pointer is
        # at node to be deleted.
        dummy = Node(None)
        dummy.next = self.head
        if self.head:
            first, second = dummy, dummy
            first_distance, second_distance = 0, 0
            while second:
                dist_diff = second_distance - first_distance
                print(first.data, second.data, "| dist:", dist_diff)
                second = second.next
                if (dist_diff) > n:
                    first = first.next
                    first_distance += 1
                second_distance += 1
            print(first.data, first.next.data)
            if first.data is None:
                self.head = first.next.next
            else:
                first.next = first.next.next
            return self.head
                
    def Print(self, reverse=False): # Recursion
        def print_help(head):
            if not head: # base case
                return ""
            else: # recursive case
                if reverse:
                    pointer = " <- " if head.next else ""
                    return print_help(head.next) + pointer + str(head.data) # print in reverse order
                pointer = " -> " if head.next else ""
                return str(head.data) + pointer + print_help(head.next)
                
        print("Linked List:", print_help(self.head))
            

if __name__ == "__main__":
    ll = LinkedList()
    
    data = [0,0,8,8,0,9,5,0,1,1,7,5,6,9,4,4,2,5,2]

    for d in data:
        node = Node(d)
        ll.append(node)
        
    ll.Print(reverse=False)
    print(ll.removeNthFromEnd(14))
    ll.Print(reverse=False)
    
    