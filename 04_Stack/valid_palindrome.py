"""
Valid Parentheses
Problem: LeetCode 76 - Minimum Window Substring
Difficulty: Medium

problem statement:

You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.
The input string s is valid if and only if:
Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.

Example 1:
Input: s = "[]"
Output: true

Example 2:
Input: s = "([{}])"
Output: true

Example 3:
Input: s = "[(])"
Output: false
Explanation: The brackets are not closed in the correct order.

Constraints:
1 <= s.length <= 1000
"""

class Solution:
    def isValid(self, s: str) -> bool:
        # Create a stack to keep track of opening brackets.
        stack = []
        # Create a dictionary to store the mapping of opening and closing brackets.
        parentheses_map = {")": "(", "}": "{", "]": "["}


        # Iterate through the string.
        for char in s:
            # if the character is an opening bracket, push it to the stack.
            if char in parentheses_map.values():
                stack.append(char) 
            # if the character is a closing bracket, check if it matches the top of the stack.
            elif char in parentheses_map:
                # if the stack is empty or the top of the stack does not match the closing bracket, return False.
                if not stack or stack[-1] != parentheses_map[char]:
                    return False
                stack.pop()
            else :
                return False
        
        return not stack
        
# Time Complexity: O(n)
# Space Complexity: O(n)

if __name__ == "__main__":
    solution = Solution()
    s = "([{}])"
    print(solution.isValid(s)) #