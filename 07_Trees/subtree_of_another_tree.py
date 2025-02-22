"""
Subtree of Another Tree
Problem: LeetCode 57 - Subtree of Another Tree
Difficulty: Easy

Problem statement:
Given the roots of two binary trees root and subRoot, 
return true if there is a subtree of root with the same structure 
and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in 
tree and all of this node's descendants. The tree tree could also be 
considered as a subtree of itself.

Example 1:
Input: root = [1,2,3,4,5], subRoot = [2,4,5]
Output: true

Example 2:
Input: root = [1,2,3,4,5,null,null,6], subRoot = [2,4,5]
Output: false

Constraints:
0 <= The number of nodes in both trees <= 100.
-100 <= root.val, subRoot.val <= 100
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # If subRoot is None, it is a subtree of any tree
        if not subRoot:
            return True
        
        # If root is None but subRoot is not, subRoot cannot be a subtree
        if not root:
            return False
        
        # Check if the current subtree matches subRoot
        if self.isSameTree(root, subRoot):
            return True
        
        # Recursively check left and right subtrees for subRoot
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Both nodes are None: structural match
        if not p and not q:
            return True
        
        # One node is None, the other is not: structural mismatch
        if not p or not q:
            return False
        
        # Value mismatch
        if p.val != q.val:
            return False
        
        # Recursively check left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
