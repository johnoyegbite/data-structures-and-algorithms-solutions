# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 18:03:35 2020

@author: johnoyegbite
"""
# SOLVED !
"""
Problem:
    Serialization is the process of converting a data structure or object into
    a sequence of bits so that it can be stored in a file or memory buffer, 
    or transmitted across a network connection link to be reconstructed later 
    in the same or another computer environment.

    Design an algorithm to serialize and deserialize a binary tree. 
    There is no restriction on how your serialization/deserialization algorithm 
    should work. You just need to ensure that a binary tree can be serialized 
    to a string and this string can be deserialized to the original tree structure.

Example: 
    You may serialize the following tree:

        1
       / \
      2   3
         / \
        4   5

    as "[1,2,3,null,null,4,5]"
    
Clarification: 
    The above format is the same as how LeetCode serializes a binary tree. 
    You do not necessarily need to follow this format, so please be creative 
    and come up with different approaches yourself.

Note: 
    Do not use class member/global/static variables to store states. 
    Your serialize and deserialize algorithms should be stateless.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BinaryTree(object):
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        queue = [root]
        
        serialized = []
        front = 0
        while front < len(queue):
            node = queue[front]
            if node == None:
                serialized.append(None)
                front += 1
                continue
            serialized.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
            front += 1
            
        return serialized
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data or data[0] == None:
            return None
            
        root_val = data[0]
        root = TreeNode(root_val)
        
        tree_queue = [root]
        
        # Track the tree_queue index
        # This index is for each node and 1 increment is performed
        # each time through the loop.
        t_idx = 0
        
        # Track the data index
        # This index is for children of a node (left and right)
        # and 2 increments is performed each time through the loop:
        # 1 for the left node and 1 for the right node.
        d_idx = 1 
        
        while t_idx < len(tree_queue) and d_idx < len(data):
            node_val = data[d_idx]
            if node_val != None:
                node = TreeNode(node_val)
                tree_queue[t_idx].left = node
                tree_queue.append(node)
            else:
                tree_queue[t_idx].left = None
            
            d_idx += 1 # 2nd increment for the right child
            
            node_val = data[d_idx]
            if node_val != None:
                node = TreeNode(node_val)
                tree_queue[t_idx].right = node
                tree_queue.append(node)
            else:
                tree_queue[t_idx].right = None
            
            d_idx += 1 # 1st increment for the left child
            
            t_idx += 1 # One (1) increment for node
    
        return root


if __name__ == "__main__":
    data = [3, 9, 20, None, None, 15, 7]
    
    data = [1, 2, 3, 11, None, 4, 5, None, None, 6, 7,
            None, 10, None, None, 8, 9, None, None, 12, 
            13, None, None, None, None, None, 14
            ]
    
    bt = BinaryTree()
    
    root = bt.deserialize(data)
    
    data = bt.serialize(root)
    print(data)
    