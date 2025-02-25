"""
Kth Smallest Integer in BST
Problem: LeetCode 230 - Kth Smallest Element in a BST
Diffuculty: Medium

Problem statement:
Given the root of a binary search tree, and an integer k, return 
the kth smallest value (1-indexed) in the tree.

A binary search tree satisfies the following constraints:

The left subtree of every node contains only nodes with keys less than the node's key.
The right subtree of every node contains only nodes with keys greater than the node's key.
Both the left and right subtrees are also binary search trees.

Example 1:
Input: root = [2,1,3], k = 1
Output: 1

Example 2:
Input: root = [4,3,5,2,null], k = 4
Output: 5

Constraints:
1 <= k <= The number of nodes in the tree <= 1000.
0 <= Node.val <= 1000
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # stack for inorder traversal
        stack = []
        # start from root node
        curr = root     # current

        # traverse the tree
        while stack or curr:
            # go to the left node
            while curr:
                stack.append(curr)
                curr = curr.left

            # process the current node 
            curr = stack.pop()
            k -= 1  # decrement k
            # if k reaches 0, return current node's value
            if k == 0:
                return curr.val

            # move to right 
            curr = curr.right

        # if k is out of bound return -1
        return -1
