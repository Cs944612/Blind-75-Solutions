"""
Binary Tree Maximum Path Sum
Problem: LeetCode 124 - Binary Tree Maximum Path Sum
Difficulty: Hard

Problem statement:
Given the root of a non-empty binary tree, return the maximum path sum of any non-empty path.

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes has 
an edge connecting them. A node can not appear in the sequence more than once. 
The path does not necessarily need to include the root.

The path sum of a path is the sum of the node's values in the path.

Example 1:
Input: root = [1,2,3]
Output: 6
Explanation: The path is 2 -> 1 -> 3 with a sum of 2 + 1 + 3 = 6.

Example 2:
Input: root = [-15,10,20,null,null,15,5,-5]
Output: 40
Explanation: The path is 15 -> 20 -> 5 with a sum of 15 + 20 + 5 = 40.

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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Initialize global maximum to negative infinity
        self.global_max = float('-inf')
        
        def max_downward_path(node):
            # Base case: if node is None, contribute nothing
            if node is None:
                return 0
            
            # Recursively get the maximum downward path from left and right subtrees
            # Use max(0, ...) to include only positive contributions
            left_downward = max(0, max_downward_path(node.left))
            right_downward = max(0, max_downward_path(node.right))
            
            # Maximum path sum through the current node (left -> node -> right)
            path_through = node.val + left_downward + right_downward
            
            # Update the global maximum if the path through this node is larger
            self.global_max = max(self.global_max, path_through)
            
            # Return the maximum downward path starting from this node
            # Either left or right subtree can be included, whichever is larger
            return node.val + max(left_downward, right_downward)
        
        # Start the recursion from the root
        max_downward_path(root)
        
        # Return the global maximum path sum
        return self.global_max
