"""
Construct Binary Tree from Preorder and Inorder Traversal
Problem: LeetCode 105 - Construct Binary Tree from Preorder and Inorder Traversal
Difficulty: Medium


Problem statement:
You are given two integer arrays preorder and inorder.

preorder is the preorder traversal of a binary tree
inorder is the inorder traversal of the same tree
Both arrays are of the same size and consist of unique values.
Rebuild the binary tree from the preorder and inorder traversals and return its root.

Example 1:
Input: preorder = [1,2,3,4], inorder = [2,1,3,4]
Output: [1,2,3,null,null,null,4]

Example 2:
Input: preorder = [1], inorder = [1]
Output: [1]

Constraints:
1 <= inorder.length <= 1000.
inorder.length == preorder.length
-1000 <= preorder[i], inorder[i] <= 1000
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Map to store value -> index for inorder traversal
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        # Pointer to track current root in preorder
        self.pre_idx = 0
        
        def build(preorder, inorder_map, in_start, in_end):
            # Base case: if no elements to process
            if in_start > in_end:
                return None
            
            # Get the current root value from preorder
            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)
            self.pre_idx += 1
            
            # Find root's position in inorder
            root_idx = inorder_map[root_val]
            
            # Recursively build left and right subtrees
            root.left = build(preorder, inorder_map, in_start, root_idx - 1)
            root.right = build(preorder, inorder_map, root_idx + 1, in_end)
            
            return root
        
        return build(preorder, inorder_map, 0, len(inorder) - 1)
