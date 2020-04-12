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


class DllNode(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class Dll(object):
    def __init__(self):
        self.head = DllNode(None, None)
        self.tail = DllNode(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def move_to_head(self, node):
        # detach node from its current position
        node_prev = node.prev
        node_next = node.next
        node_prev.next = node_next
        node_next.prev = node_prev
        # move node to after head
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def add_node(self, key, val):
        node = DllNode(key, val)
        node.next, node.prev = self.head.next, self.head
        self.head.next.prev, self.head.next = node, node
        return node

    def remove_tail(self):
        last_node = self.tail.prev
        last_node.prev.next, self.tail.prev = self.tail, last_node.prev

    def last_node(self):
        return self.tail.prev


class LRUCache(object):
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.Dll = Dll()
        self.node_lookup = {}
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.node_lookup:
            return -1
        key_node = self.node_lookup[key]
        self.Dll.move_to_head(key_node)
        # key_node_index = 1
        return key_node.val

    def put(self, key: int, value: int) -> None:
        if key in self.node_lookup:
            key_node = self.node_lookup[key]
            # print(key_node.val)
            key_node.val = value
            self.Dll.move_to_head(key_node)
            return
        if self.size == self.capacity:
            last_node = self.Dll.last_node()
            del self.node_lookup[last_node.key]
            self.Dll.remove_tail()
            self.size -= 1
        self.node_lookup[key] = self.Dll.add_node(key, value)
        self.size += 1


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
