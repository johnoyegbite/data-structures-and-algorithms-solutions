# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 14:24:46 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Implement a stack with following functions:
        push(val) push val into the stack
        pop() pop the top element and return it
        min() return the smallest number in the stack
    All above should be in O(1) cost.

Example 1:
    Input:
      push(1)
      pop()
      push(2)
      push(3)
      min()
      push(1)
      min()
    Output:
      1
      2
      1

Example 2:
    Input:
      push(1)
      min()
      push(2)
      min()
      push(3)
      min()
    Output:
      1
      1
      1
      
Notice
min() will never be called when there is no number in the stack.

"""


import sys


class MinStack(object):
    def __init__(self):
        # do intialization if necessary
        self.stack = []
        self.minimum_number = sys.maxsize

    def push(self, number):
        """
        type number: int
        rtype: None
        """
        if not len(self.stack):
            self.minimum_number = number
            self.stack.append(number)
        else:
            if number < self.minimum_number:
                # let x be the number you want to push
                # let min be the current minimum
                # But:
                # x < min
                # x - min < 0
                # 2x - min < x (adding 'x' to both side)
                # I can store "2x - min" as new 'x' and 'x' as new 'min'
                number_to_push = 2*number - self.minimum_number
                self.stack.append(number_to_push)
                self.minimum_number = number
            else:
                self.stack.append(number)

    def pop(self):
        """
        rtype: int
        """
        # write your code here
        if len(self.stack):
            elem_to_del = self.stack.pop()
            if elem_to_del < self.minimum_number:
                new_elem_to_del = self.minimum_number
                self.minimum_number = 2*self.minimum_number - elem_to_del
                elem_to_del = new_elem_to_del
            return elem_to_del

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack):
            if self.stack[-1] < self.minimum:
                return self.minimum
            return self.stack[-1]

    def min(self):
        """
        rtype: int
        """
        # write your code here
        return self.minimum_number


if __name__ == "__main__":
    stack = MinStack()
    
    # Example 1 => Output: 1, 2, 1
    # stack.push(1)
    # print(stack.pop())
    # stack.push(2)
    # stack.push(3)
    # print(stack.min())
    # stack.push(1)
    # print(stack.min())
    
    # Example 2 => Output: 1, 1, 1
    stack.push(1)
    print(stack.min())
    stack.push(2)
    print(stack.min())
    stack.push(3)
    print(stack.min())
    
    # Example 3 => Output: 1, 1, 1, 1
    # stack.push(1)
    # stack.push(1)
    # stack.push(1)
    # print(stack.min()) # 1
    # print(stack.pop()) # [1, 1] # 1
    # print(stack.min()) # 1
    # print(stack.pop()) # 1
    