# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 00:36:16 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Implement the following operations of a stack using queues.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    empty() -- Return whether the stack is empty.

Example:
    MyStack stack = new MyStack();

    stack.push(1);
    stack.push(2);
    stack.top();   // returns 2
    stack.pop();   // returns 2
    stack.empty(); // returns false

Notes:
    You must use only standard operations of a queue -- which means only push
    to back, peek/pop from front, size, and is empty operations are valid.
    Depending on your language, queue may not be supported natively.
    You may simulate a queue by using a list or deque (double-ended queue),
    as long as you use only standard operations of a queue.
    You may assume that all operations are valid (for example, no pop or top
    operations will be called on an empty stack).
"""
from queue import Queue


class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.last = None  # top element on the stack
        self.size = 0
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q1.put(x)
        self.last = x
        self.size += 1

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        # copy the current size to control the last element that would be
        # popped.
        size = self.size
        while not self.q1.empty():
            x = self.q1.get()
            if size > 1:
                self.q2.put(x)
                self.last = x
            size -= 1
        self.size -= 1  # elemnet in the size is reduced by 1
        self.q1, self.q2 = self.q2, self.q1
        return x

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.last

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.size <= 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
