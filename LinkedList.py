# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 18:12:33 2019

@author: USER
"""
# SOLVED!
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
            
    def insert(self, new_node, position):
        current = self.head
        if position == 1:
            new_node.next = current
            self.head = new_node
        else:
            for i in range(1, position-1):
                current = current.next # position-1 element
            new_node.next = current.next
            current.next = new_node
            
    def delete(self, position):
        # Assumes position of list start count from 1.
        current = self.head 
        if position == 1:
            current = current.next
            self.head = current
        else:
            for position in range(1, position-1):
                if not current.next:
                    raise Exception("Linked list out of range")
                current = current.next # get node at (postion - 1)
            if not current.next:
                raise Exception("Linked list out of range")
            node_plus_1 = current.next.next # get node at (postion + 1)
            current.next = node_plus_1 # skip the node at position
            
    # def reverse(self):
    #     # You can reverse a linked list by pointing node the previous and
    #     # pointing the head node to None.
    #     current = self.head
    #     if self.head:
    #         prev = None # first node should point to a previous node of None
    #         while current.next:
    #             next_node = current.next # get next node of current node (store for later use)
    #             current.next = prev # point the current node to the previous node 
    #                                 # (which is None if current node is the head node)
    #             prev = current # set the next previous node equal to the current node
    #             current = next_node # set current node to the the next node stored earlier
                
    #         current.next = prev # at the end of the list, last node is connected to previous
    #         self.head = current # new head is the last node of the list
    #     return self.head
    
    def reverse(self):
        def reverse_help(previous, current):
            if not current:
                self.head = previous
                return
            else:
                next_node = current.next # get next node of current node (store for later use)
                current.next = previous # point the current node to the previous node 
                                    # (which is None if current node is the head node)
                previous = current # set the next previous node equal to the current node
                current = next_node # set current node to the the next node stored earlier
                return reverse_help(previous, current)
            
        return reverse_help(None, self.head)
            
    # def Print(self, reverse=False):
    #     ll = ""
    #     current = self.head
    #     if self.head:
    #         while current.next:
    #             if reverse:
    #                 ll = " <- " + str(current.data) + ll
    #             else: 
    #                 ll += str(current.data) + " -> "
    #             current = current.next
    #         if reverse:
    #             ll = str(current.data) + ll
    #         else: 
    #             ll += str(current.data)
    #         print(ll)
    #         return
    #     print("Empty List")
        
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
                
        print(print_help(self.head))
    

if __name__ == "__main__":
    ll = LinkedList()
    
    data = [2, 3, 5, 7]
    
    for d in data:
        node = Node(d)
        ll.append(node)
    
    # ll.delete(7)   
    ll.Print(reverse=False)
    ll.reverse()
    ll.Print()