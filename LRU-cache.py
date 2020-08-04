# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 00:45:14 2019

@author: USER
"""
# SOLVED!
"""
Problem:
    Design and implement a data structure for Least Recently Used (LRU) cache.
    It should support the following operations: get and put.

    get(key) -
        Get the value (will always be positive) of the key if the key exists
        in the cache, otherwise return -1.

    put(key, value) -
        Set or insert the value if the key is not already present.
        When the cache reached its capacity, it should invalidate the least
        recently used item before inserting a new item.

    The cache is initialized with a positive capacity.

    Follow up:
        Could you do both operations in O(1) time complexity?

Example:
    cache = LRUCache( 2 /* capacity */ );

    cache.put(1, 1);
    cache.put(2, 2);
    cache.get(1);       // returns 1
    cache.put(3, 3);    // evicts key 2
    cache.get(2);       // returns -1 (not found)
    cache.put(4, 4);    // evicts key 1
    cache.get(1);       // returns -1 (not found)
    cache.get(3);       // returns 3
    cache.get(4);       // returns 4
"""


class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class Dll(object):
    def __init__(self):
        # Initialize empty Double linked list,
        # by pointing head to tail and tail to head
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert_node_at_head(self, node):
        # insert node between head and the next node after head
        node.prev = self.head
        node.next = self.head.next

        # Update the back pointer of the original head.next to the node
        # also update the front pointer of head to node.
        self.head.next.prev = node
        self.head.next = node

    def remove_tail(self):
        # Note that the least recently used would be at the tail
        # So we can just delete the node at the tail to invalidate
        # the least recently used node.
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail

    def move_to_head(self, node):
        # Note that the most recently used would be at the head
        # Hence, any node we move to the head would be the most recently used

        # disconnect the node from its current position in the double
        # linked list by connecting its adjacent nodes together
        node.prev.next = node.next
        node.next.prev = node.prev

        # after disconneting, insert it at the head to make it the
        # most recently used.
        self.insert_node_at_head(node)

    def get_tail(self):
        return self.tail.prev

    def printCache(self, typ):
        l = ["HEAD"]
        curr = self.head.next
        while curr:
            if not curr.val:
                l.append("TAIL")
            else:
                l.append("[{}]:[{}]".format(curr.key, curr.val))
            curr = curr.next
        path = " <--> ".join(l)
        return typ + ": " + path


class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.dll = Dll()

    def put(self, key, value):
        # if key exists, just modify its value in the cache
        # and this does it automatically in the Dll.
        # Also move to head to make it the most recently used and return early.
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.dll.move_to_head(node)
            return

        # if the capacity of the cache is full, the invalidate the least
        # recently used by deleting the tail node and also deleting it from
        # the cache
        if len(self.cache) == self.capacity:
            tail_node = self.dll.get_tail()
            del self.cache[tail_node.key]
            self.dll.remove_tail()

        # Insert the node at the head in the Dll which would automatically
        # make it the most recently used and also insert in the cache.
        node = Node(key, value)
        self.cache[key] = node
        self.dll.insert_node_at_head(node)
        # print(self.dll.printCache("PUT"))

    def get(self, key):
        # if the key exists, return its value and also make sure you move it to
        # the head to make it the most recently used node.
        # REMEMBER that the least recently used is always at the tail.
        if key in self.cache:
            node = self.cache[key]
            self.dll.move_to_head(node)
            # print(self.dll.printCache("GET"))
            return node.val
        return -1


if __name__ == "__main__":
    # ["LRUCache", "put", "put", "get", "put", "put", "get"]
    # [[2], [2, 1], [2, 2], [2], [1, 1], [4, 1], [2]]

    # ["LRUCache","get","put","get","put","put","get","get"]
    # [[2], [2], [2, 6], [1], [1, 5], [1, 2], [1], [2]]

    ["LRUCache", "put", "put", "put", "put", "get", "get"]
    [[2], [2, 1], [1, 1], [2, 3], [4, 1], [1], [2]]

    # Your LRUCache object will be instantiated and called as such:
    cache = LRUCache(2)

    cache.put(2, 1)  # null
    # cache.print_()
    cache.put(1, 1)  # null
    # cache.print_()
    cache.put(2, 3)  # null
    # cache.print_()
    cache.put(4, 1)  # null
    # cache.print_()
    print(cache.get(1))  # -1
    print(cache.get(2))  # 3

    # cache.put("a", 1)
    # cache.put("b", 2)
    # print("Answer: ", cache.get("a")) # returns a
    # cache.put("c", 3)     # evicts key b
    # print("Answer: ", cache.get("b")) # returns -1 (not found)
    # cache.put("d", 4)     # evicts key a
    # print("Answer: ", cache.get("a")) # returns -1 (not found)
    # print("Answer: ", cache.get("c")) # returns c
    # print("Answer: ", cache.get("d")) # returns d
    # # print("Answer: ", cache.get("b")) # returns d
