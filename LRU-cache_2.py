# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 18:14:13 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Design and implement a data structure for Least Recently Used (LRU) cache.
    It should support the following operations: get and put.

    get(key) - Get the value (will always be positive) of the key if the key
    exists in the cache, otherwise return -1.

    put(key, value) - Set or insert the value if the key is not already
    present.
    When the cache reached its capacity, it should invalidate the least
    recently used item before inserting a new item.

    The cache is initialized with a positive capacity.

Follow up:
    Could you do both operations in O(1) time complexity?

Example:
    LRUCache cache = new LRUCache( 2 /* capacity */ );

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
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class DLL(object):
    def __init__(self):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert_at_head(self, node):
        # h <-> t
        # h <-> 1 <-> t
        # h <-> 2 <-> 1 <-> t
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        return node

    def move_to_head(self, node):
        # h <-> 5 <-> 4 <-> 3 <-> 2 <-> 1 <-> t

        # move 3 to head
        # h <-> 3 <-> 5 <-> 4 <-> 2 <-> 1 <-> t
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

        self.insert_at_head(node)

    def invalidate_least_recent(self):
        last_node = self.tail.prev
        new_last_node = last_node.prev
        new_last_node.next = self.tail
        self.tail.prev = new_last_node
        return last_node.key

    def __str__(self):
        """For debugging purpose"""
        cache = []
        curr = self.head
        while curr:
            cache.append((curr.key, curr.value))
            curr = curr.next
        return str(cache)


class LRUCache(object):

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.dll = DLL()

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.dll.move_to_head(node)
            # print("get({}): {}".format(key, self.dll))
            return node.value
        # print("get({}): {}".format(key, self.dll))
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            key_node = self.cache[key]
            key_node.value = value
            self.dll.move_to_head(key_node)
            # print("exist-put({}:{}): {}".format(key, value, self.dll))
            return
        node = Node(key, value)
        if self.size < self.capacity:
            self.size += 1
            # print("not_full-put({}:{}): {}".format(key, value, self.dll))
        else:
            least_used = self.dll.invalidate_least_recent()
            del self.cache[least_used]
            # print("full-put({}:{}): {}".format(key, value, self.dll))
        self.cache[key] = self.dll.insert_at_head(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
