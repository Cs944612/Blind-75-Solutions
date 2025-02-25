"""
Serialize and Deserialize Binary Tree
Problem: LeetCode 297 - Serialize and Deserialize Binary Tree
Difficulty: Hard

Probelem statement:
Implement an algorithm to serialize and deserialize a binary tree.

Serialization is the process of converting an in-memory structure into a
sequence of bits so that it can be stored or sent across a network to be 
reconstructed later in another computer environment.

You just need to ensure that a binary tree can be serialized to a string and 
this string can be deserialized to the original tree structure. There is no additional 
restriction on how your serialization/deserialization algorithm should work.

Note: The input/output format in the examples is the same as how NeetCode serializes a 
binary tree. You do not necessarily need to follow this format.

Example 1:
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

Example 2:
Input: root = []
Output: []

Constraints:
0 <= The number of nodes in the tree <= 1000.
-1000 <= Node.val <= 1000
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "null"
        # Preorder: root, left, right
        return f"{root.val},{self.serialize(root.left)},{self.serialize(root.right)}"
    
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        # Split the string into a list of values
        values = data.split(",")
        self.index = 0  # Track position in the list
        
        def dfs():
            if self.index >= len(values):
                return None
            val = values[self.index]
            self.index += 1
            
            if val == "null":
                return None
            
            # Create node and recursively build subtrees
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()
