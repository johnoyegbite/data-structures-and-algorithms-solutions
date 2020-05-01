# -*- coding: utf-8 -*-
"""
Created on Fri May  1 13:35:48 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Given a binary tree, return all root-to-leaf paths.

    Note: A leaf is a node with no children.

Example:
    Input:

       1
     /   \
    2     3
     \
      5

    Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def dfs(self, node, visited, curr_path, paths):
        visited[node] = True
        curr_path.append(str(node.val))

        if not node.left and not node.right:
            paths.append('->'.join(curr_path[:]))

        children = list(filter(lambda x: x != None, [node.left, node.right]))
        for child in children:
            if child.val not in visited:
                self.dfs(child, visited, curr_path, paths)

        curr_path.pop()
        del visited[node]
        return

    def binaryTreePaths(self, root: TreeNode) -> list[str]:
        if not root:
            return []
        paths = []
        curr_path = []
        visited = {}
        self.dfs(root, visited, curr_path, paths)
        return paths
