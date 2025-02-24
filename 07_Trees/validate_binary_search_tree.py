"""
Valid Binary Search Tree
Problem: LeetCode 98 - Validate Binary Search Tree
Difficulty: Medium

Problem statement:
Given the root of a binary tree, return true if it is a valid binary search tree, otherwise return false.

A valid binary search tree satisfies the following constraints:

The left subtree of every node contains only nodes with keys less than the node's key.
The right subtree of every node contains only nodes with keys greater than the node's key.
Both the left and right subtrees are also binary search trees.

Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [1,2,3]
Output: false
Explanation: The root node's value is 1 but its left child's value is 2 which is greater than 1.

Constraints:
1 <= The number of nodes in the tree <= 1000.
-1000 <= Node.val <= 1000
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Initialize a stack for inorder traversal
        stack = deque()
        # Initialize previous value as negative infinity
        prev = float('-inf')

        # Traverse the tree
        while stack or root:
            # Go to the leftmost node
            while root:
                stack.append(root)
                root = root.left

            # Process the current node
            root = stack.pop()
            # Check if the current node's value is greater than the previous value
            if root.val <= prev:
                return False
            # Update the previous value
            prev = root.val

            # Move to the right subtree
            root = root.right

        # If the traversal completes without issues, it's a valid BST
        return True
