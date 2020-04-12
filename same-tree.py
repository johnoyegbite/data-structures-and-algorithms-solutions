# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 20:17:27 2020

@author: johnoyegbite
"""
# SOLVED !
"""
Problem:
    Check if two binary trees are identical. Identical means the two binary
    trees have the same structure and every identical position has the same value.

Example 1:
    Input:{1,2,2,4},{1,2,2,4}
    Output:true
    Explanation:
        1                   1
       / \                 / \
      2   2   and         2   2
     /                   /
    4                   4

    are identical.

Example 2:
    Input:{1,2,3,4},{1,2,3,#,4}
    Output:false
    Explanation:

        1                  1
       / \                / \
      2   3   and        2   3
     /                        \
    4                          4
    are not identical.
"""
"""
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

from queue import Queue

from binary_tree import BinaryTree

def isIdentical(a, b):
    # write your code here
    # Serialize Tree a
    q = Queue()
    q.put(a)
    a_nodes = []
    while not q.empty():
        node = q.get()
        if node == None:
            a_nodes.append(None)
            continue
        # IMPORTANT!
        # make sure you append the val or data because node object are not equal
        # hence you can't compare them instead you should compare the values of
        # the node object.
        a_nodes.append(node.data)
        q.put(node.left)
        q.put(node.right)
    
    # Serialize Tree b
    q = Queue()
    q.put(b)
    b_nodes = []
    while not q.empty():
        node = q.get()
        if node == None:
            b_nodes.append(None)
            continue
        b_nodes.append(node.data)
        q.put(node.left)
        q.put(node.right)
            
    return a_nodes == b_nodes


if __name__ == "__main__":
    bt1 = BinaryTree()
    l = [8, 12, 1, 2, 3, 6, 9, 10, 20, 15, 11, 7, 7]
    bt1.insert(l)
    
    bt2 = BinaryTree()
    l = [8, 12, 1, 10, 20, 15, 11, 2, 3, 6, 9, 7, 7]
    bt2.insert(l)
        
    # print(bt.print_as_bfs())
        
    print(isIdentical(bt1.tree, bt2.tree))
            
            
        
        

