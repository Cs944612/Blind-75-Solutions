"""
Binary Tree Level Order Traversal
Problem: LeetCode 102 - Binary Tree Level Order Traversal
Difficulty: Medium

Problem statement:
Given a binary tree root, return the level order traversal of it as a nested list, 
where each sublist contains the values of nodes at a particular level in the tree, from left to right.

Example 1:
Input: root = [1,2,3,4,5,6,7]
Output: [[1],[2,3],[4,5,6,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

Constraints:
0 <= The number of nodes in both trees <= 1000.
-1000 <= Node.val <= 1000
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # initialize the result list
        result = []

        # if empty tree
        if not root:
            return result

        # use queue for BFS (Breadth First Search)
        queue = deque([root])
        
        # process each level
        while queue:
            # get the number of nodes at current level
            level_size = len(queue)
            # Empty list to store values of the current level\
            curr_level = []

            # process all nodes at current level
            for _ in range(level_size): 
                # Deque the front node 
                node = queue.popleft()
                # add its value to the current level list
                curr_level.append(node.val)
                # if its children exits enqueue 
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # add the current list to the result
            result.append(curr_level)

        return result
