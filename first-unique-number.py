# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 21:38:03 2020

@author: johnoyegbite
"""
# SOLVED!
"""
You have a queue of integers, you need to retrieve the first unique integer in
the queue.

Implement the FirstUnique class:
    FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
    int showFirstUnique() returns the value of the first unique integer of the
    queue, and returns -1 if there is no such integer.
    void add(int value) insert value to the queue.

Example 1:
    Input: 
        ["FirstUnique","showFirstUnique","add","showFirstUnique","add",
         "showFirstUnique","add","showFirstUnique"]
        [[[2,3,5]],[],[5],[],[2],[],[3],[]]
    Output:
        [null,2,null,2,null,3,null,-1]

    Explanation:
        FirstUnique firstUnique = new FirstUnique([2,3,5]);
        firstUnique.showFirstUnique(); // return 2
        firstUnique.add(5);            // the queue is now [2,3,5,5]
        firstUnique.showFirstUnique(); // return 2
        firstUnique.add(2);            // the queue is now [2,3,5,5,2]
        firstUnique.showFirstUnique(); // return 3
        firstUnique.add(3);            // the queue is now [2,3,5,5,2,3]
        firstUnique.showFirstUnique(); // return -1

Example 2:
    Input:
        ["FirstUnique","showFirstUnique","add","add","add","add","add",
         "showFirstUnique"]
        [[[7,7,7,7,7,7]],[],[7],[3],[3],[7],[17],[]]
    Output:
        [null,-1,null,null,null,null,null,17]

    Explanation:
        FirstUnique firstUnique = new FirstUnique([7,7,7,7,7,7]);
        firstUnique.showFirstUnique(); // return -1
        firstUnique.add(7);            // the queue is now [7,7,7,7,7,7,7]
        firstUnique.add(3);            // the queue is now [7,7,7,7,7,7,7,3]
        firstUnique.add(3);            // the queue is now [7,7,7,7,7,7,7,3,3]
        firstUnique.add(7);            // the queue is now [7,7,7,7,7,7,7,3,3,7]
        firstUnique.add(17);           // the queue is now [7,7,7,7,7,7,7,3,3,7,17]
        firstUnique.showFirstUnique(); // return 17

Example 3:
    Input:
    ["FirstUnique","showFirstUnique","add","showFirstUnique"]
    [[[809]],[],[809],[]]
    Output:
    [null,809,null,-1]

    Explanation:
        FirstUnique firstUnique = new FirstUnique([809]);
        firstUnique.showFirstUnique(); // return 809
        firstUnique.add(809);          // the queue is now [809,809]
        firstUnique.showFirstUnique(); // return -1

Constraints:
    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^8
    1 <= value <= 10^8
    At most 50000 calls will be made to showFirstUnique and add.
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class Dll:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self, node):
        # insert the node at the tail so as to retain the first-in first-out
        # pattern

        node.prev = self.tail.prev
        node.next = self.tail

        self.tail.prev.next = node
        self.tail.prev = node

    def first(self):
        if self.head.next.val:
            return self.head.next.val
        return None

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        del node


class FirstUnique:
    def __init__(self, nums: list[int]):
        self.dll = Dll()
        self.node_lookup = {}
        self.appendInitial(nums)

    def appendInitial(self, nums: list[int]):
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        if not self.dll.first():
            return -1
        return self.dll.first()

    def add(self, value: int) -> None:
        if value in self.node_lookup:
            count, node = self.node_lookup[value]
            self.node_lookup[value] = (count+1, node)
            if count == 1:
                self.dll.remove(node)
        else:
            node = Node(value)
            self.node_lookup[value] = (1, node)
            self.dll.add(node)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
