"""
Valid Palindrome
Problem: LeetCode 128 -Longest Consecutive Sequence
Difficulty: Easy

Problem Statement:
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. 
It is also case-insensitive and ignores all non-alphanumeric characters.

Example 1:
Input: s = "Was it a car or a cat I saw?"
Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

Example 2:
Input: s = "tab a cat"
Output: false
Explanation: "tabacat" is not a palindrome.

Constraints:
1 <= s.length <= 1000
s is made up of only printable ASCII characters.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while right > left and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            # move the pointers towards the center
            left += 1
            right -= 1
        return True
    
# Time Complexity: O(n)
# Space Complexity: O(1)

if __name__ == "__main__":
    # Example usage
    s = "Was it a car or a cat I saw?"
    print(Solution().isPalindrome(s)) 
    