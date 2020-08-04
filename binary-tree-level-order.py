# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 17:05:51 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).


Example 1:
    Input：{1,2,3}
    Output：[[1],[2,3]]
    Explanation：
      1
     / \
    2   3
    it will be serialized {1,2,3}
    level order traversal

Example 2:
    Input：{1,#,2,3}
    Output：[[1],[2],[3]]
    Explanation：
    1
     \
      2
     /
    3
    it will be serialized {1,#,2,3}
    level order traversal

Challenge 1: Using only 1 queue to implement it.

Challenge 2: Use BFS algorithm to do it.

Notice
The first data is the root node, followed by the value of the left and right son nodes, 
and "#" indicates that there is no child node.
The number of nodes does not exceed 20.
"""


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


def levelOrder(self, root):
    """
    type root: TreeNode
    rtype: List[List[int]]
    """
    # write your code here
    if not root:
        return []
        
    
    level = [root]
    level_order = [[root.val]]
    
    while len(level):
        new_node_level = []
        new_val_level = []
        for node in level:
            left_node = node.left
            right_node = node.right
            if left_node:
                new_node_level.append(left_node)
                new_val_level.append(left_node.val)
            if right_node:
                new_node_level.append(right_node)
                new_val_level.append(right_node.val)
        if new_val_level:
            level_order.append(new_val_level)   
        level = new_node_level
    return level_order



