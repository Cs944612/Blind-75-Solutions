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
        
        # Step 1: Build the frequency dictionary for t.
        freq_t = {}
        for char in t:
            freq_t[char] = freq_t.get(char,0) + 1

        required_chars = len(freq_t)        # unique chars to match  

        # Step 2: Initialize the sliding window pointers and other variables.
        left, right = 0, 0
        formed = 0              # to count how many characters meet the desired freqency
        window_counts = {}
        # (window length, left, right)
        best_window = (float("inf"), None, None)
        
        # Step 3: Start sliding the window.
        while right < len(s):
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1

            # check if the current character meets the desired frequency 
            if char in freq_t and window_counts[char] == freq_t[char]:
                formed += 1

            # Step 4: Contract the window if it's valid.
            while left <= right and formed == required_chars:
                # Update the smallest window if a smaller window is found.
                if right - left + 1 < best_window[0]:
                    best_window = (right - left + 1, left, right)
                # prepare to move left pointer: remove the char at left 
                char = s[left]
                window_counts[char] -= 1
                if char in freq_t and window_counts[char] < freq_t[char]:
                    formed -= 1
                left += 1

            # Move the right pointer to expand the window.
            right += 1

        # Step 5: Return the smallest valid window or an empty string if not found.
        if best_window[0] == float("inf"):
            return ""
        else:
            # return the substring of s that corresponds to the best window
            return s[best_window[1]:best_window[2] + 1]

# Time complexity: O(n + m), where n is the length of s and m is the length of t.
# Space complexity: O(n + m), where n is the length of s and m is the length of t.

if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    print(Solution().minWindow(s, t))  