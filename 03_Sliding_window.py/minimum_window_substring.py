"""
Minimum Window Substring
Problem: LeetCode 76 - Minimum Window Substring
Difficulty: Hard

problem statement:
Given two strings s and t, return the shortest substring of s such that every character in t, 
including duplicates, is present in the substring. If such a substring does not exist, 
return an empty string "".
You may assume that the correct output is always unique.

Example 1:

Input: s = "OUZODYXAZV", t = "XYZ"
Output: "YXAZ"
Explanation: "YXAZ" is the shortest substring that includes "X", "Y", and "Z" from string t.

Example 2:
Input: s = "xyz", t = "xyz"
Output: "xyz"

Example 3:
Input: s = "x", t = "xy"
Output: ""

Constraints:
1 <= s.length <= 1000
1 <= t.length <= 1000
s and t consist of uppercase and lowercase English letters.
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        # Build a frequency dictionary for characters in t.
        target_freq = {}
        for char in t:
            target_freq[char] = target_freq.get(char, 0) + 1

        required_unique_chars = len(target_freq)  # Number of unique characters required in window

        # Initialize window pointers and tracking variables.
        left = 0
        right = 0
        num_chars_matched = 0                # How many characters currently meet the target frequency
        current_window_counts = {}
        # (window_length, window_left, window_right)
        min_window = (float("inf"), None, None)
        
        # Expand the right pointer to explore the string.
        while right < len(s):
            curr_char = s[right]
            current_window_counts[curr_char] = current_window_counts.get(curr_char, 0) + 1

            # Check if current character fulfills the required frequency.
            if curr_char in target_freq and current_window_counts[curr_char] == target_freq[curr_char]:
                num_chars_matched += 1

            # Once we have a valid window, try to contract from the left.
            while left <= right and num_chars_matched == required_unique_chars:
                window_length = right - left + 1
                if window_length < min_window[0]:
                    min_window = (window_length, left, right)
                
                # Remove the leftmost character and move left pointer.
                left_char = s[left]
                current_window_counts[left_char] -= 1
                if left_char in target_freq and current_window_counts[left_char] < target_freq[left_char]:
                    num_chars_matched -= 1
                left += 1

            right += 1

        # Return the smallest valid window found, or an empty string if no such window exists.
        if min_window[0] == float("inf"):
            return ""
        else:
            return s[min_window[1]:min_window[2] + 1]

if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    print(Solution().minWindow(s, t))