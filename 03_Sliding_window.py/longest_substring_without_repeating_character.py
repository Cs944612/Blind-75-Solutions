"""
Longest Substring Without Repeating Characters
Problem: LeetCode 3 - Longest Substring Without Repeating Characters
Difficulty: Medium

Problem Statement:
Given a string s, find the length of the longest substring without duplicate characters.
A substring is a contiguous sequence of characters within a string.

Example 1:
Input: s = "zxyzxyz"
Output: 3
Explanation: The string "xyz" is the longest without duplicate characters.

Example 2:
Input: s = "xxxx"
Output: 1

Constraints:
0 <= s.length <= 1000
s may consist of printable ASCII characters.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_length = 0
        # set to store unique characters in the current window
        seen = set()

        for right in range(len(s)):
            # if the character at right is already in the set
            while s[right] in seen:
                # remove the character at left from the set
                seen.remove(s[left])
                # move left pointer to the right
                left += 1
            # add the character at right to the set
            seen.add(s[right])
            # update the max length
            max_length = max(max_length, right - left + 1) 
        return max_length

# Time Complexity: O(n)
# Space Complexity: O(n)

if __name__ == "__main__":
    s = "zxyzxyz"
    print(Solution().lengthOfLongestSubstring(s)) 