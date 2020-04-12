# SOLVED!
"""
Problem Description:
    Given a binary tree

    struct Node {
      int val;
      Node *left;
      Node *right;
      Node *next;
    }
    Populate each next pointer to point to its next right node. 
    If there is no next right node, the next pointer should be set to NULL.
    
    Initially, all next pointers are set to NULL.
    
    Follow up:
        You may only use constant extra space.
        Recursive approach is fine, you may assume implicit stack space 
        does not count as extra space for this problem.
     
    
    Example 1:
        
          (1)                     (1)--> None
         /   \                   /   \
       (2)   (3)               (2)--->(3)--> None
      /   \     \             /   \     \
    (4)   (5)   (7)         (4)--->(5)-->(7)--> None
       figure A                  figure B
       
        Input: root = [1,2,3,4,5,null,7]
        Output: [1,#,2,3,#,4,5,7,#]
        Explanation: 
            Given the above binary tree (Figure A), your function should 
            populate each next pointer to point to its next right node, just 
            like in Figure B. The serialized output is in level order as 
            connected by the next pointers, with '#' signifying the end of each level.
     
    
    Constraints:
        The number of nodes in the given tree is less than 6000.
        -100 <= node.val <= 100
"""


# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
        
def connect(root):
    """
    :type root: Node
    :rtype: Node
    """
    if not root:
        return root
    root.next = None # first node in tree has its next pointer to None.
    level = [root]
    while len(level) > 0:
        new_level = [] # To store all nodes on a level in the tree
        
        # Store all nodes on a level by getting the children of all the nodes
        # on the previous level.
        for node in level:
            if node.left:
                new_level.append(node.left)
            if node.right:
                new_level.append(node.right)
        
        # On a new level, populate each next pointer to the point to
        # its next right node.
        # I am going to stop at the penultimate node to avoid index error
        # which means I won't cater for the last node.
        if len(new_level) > 0:
            for node_index in range(len(new_level)-1):
                new_level[node_index].next = new_level[node_index+1]
        
            # Now to cater for the last node.
            # Last node won't have a right node. Hence set the next pointer 
            # to 'None' according to the problem description.
            new_level[-1].next = None

        # now the nodes on the 'new_level' would be our next new nodes to get their 
        # children and populate their pointers.
        level = new_level[:]   
    return root
            
        
