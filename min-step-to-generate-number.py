# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 13:33:54 2019

@author: USER
"""
# SOLVED!
"""
Problem Description:
    Given an int n. You can use only 2 operations:
    1. multiply by 2
    2. integer division by 3 (e.g. 10 / 3 = 3)
    Find the minimum number of steps required to generate n from 1.

Example 1:
    Input: 10
    Output: 6
    Explanation: 1 * 2 * 2 * 2 * 2 / 3 * 2
    6 steps required, as we have used 5 multiplications by 2, and one division by 3.

Example 2:
    Input: 3
    Output: 7
    Explanation: 1 * 2 * 2 * 2 * 2 * 2 / 3 / 3
    7 steps required, as we have used 5 multiplications by 2 and 2 divisions by 3.
"""

"""EXPLANATION
# 1. Using BFS, create a tree where each node has its left child as node*2 and right child is node//3 (this can be taken as a step)
# 2. Traverse through the tree using queue implementation.
# 3. During traversal, don't continue with a node that has already been seen (since its subtree would be repetition)
# 4. To determine if a step, use the farthest left child node of the tree at any tree height which is always a power of 2 (where 1 and 0 not inclusive)
# 5. To determine if a digit is a power of two => (digit & (digit-1) == 0
# 6. What the ampersand sign does is to convert 'digit' to bit and use the logic operator on it
# 7. 4 & (4-1) == 4 & 3 == 100 & 11 == 0
"""

from queue import Queue

def min_step(n):
    q = Queue()
    seen = set()
    
    head = 1
    q.put(head)

    steps = 0
    
    # using breadth first search
    while True:
        head = q.get()
        # Make sure 'head' is a power of 2 greater or equal to 2 and not visited before 'steps ' can be increased
        # Meaning it would increase 'steps ' based on the left most node values on the tree
        if ((head & (head-1))) == 0 and (head != 1)\
                and (head != 0) and (head not in seen):
            steps += 1
        if head == n: # return number of steps early if we have seen our winner 
            return steps 
        left_child = head*2 # create left child for node 
        right_child = head//3 # create right child for node
        if left_child not in seen: # only traverse through this left child node later on if it has not been visited
            q.put(left_child)
        if right_child not in seen:  # only traverse through this right child node later on if it has not been visited
            q.put(right_child)
        
        seen.add(head)


if __name__ == "__main__":
    n = 10
    print(min_step(n))