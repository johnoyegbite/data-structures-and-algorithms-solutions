# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 14:44:41 2020

@author: johnoyegbite
"""
# SOLVED!


class MyQueue:
    
    def __init__(self):
        # do intialization if necessary
        self.stack = []
        self.queue = []
        self.front = -1

    """
    @param: element: An integer
    @return: nothing
    """
    def push(self, element):
        # write your code here
        if self.front < 0:
            self.front = 0
        self.stack.append(element)
        return (self.stack, self.front)

    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        if -1 < self.front < len(self.stack):
            elem_del = self.stack[self.front]
            self.front += 1
            return elem_del

    """
    @return: An integer
    """
    def top(self):
        # write your code here
        if -1 < self.front < len(self.stack):
            # print("top():", self.front)
            return self.stack[self.front]
     
if __name__ == "__main__":
    q = MyQueue()
    
    print(q.push(1))
    print(q.pop())  
    print(q.push(2))
    print(q.push(3))
    print(q.top())  
    print(q.pop())
    # print(q.top())
    