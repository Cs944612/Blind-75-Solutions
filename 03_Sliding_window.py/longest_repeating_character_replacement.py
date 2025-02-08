"""
Longest Repeating Character Replacement
Problem: LeetCode 424 - Longest Repeating Character Replacement
Difficulty: Medium

problem statement:
You are given a string s consisting of only uppercase english characters and an integer k. 
You can choose up to k characters of the string and replace them with any other uppercase English character.

After performing at most k replacements, return the length of the longest substring 
which contains only one distinct character.

Example 1:
Input: s = "XYYX", k = 2
Output: 4
Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.

Example 2:
Input: s = "AAABABB", k = 1
Output: 5

Constraints:
1 <= s.length <= 1000
0 <= k <= s.length
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        left = 0
        max_freq = 0
        freq = defaultdict(int)
        max_length = 0

        for right in range(len(s)):
            # update the frequency of the current character
            current_char = s[right]
            freq[current_char] += 1
            max_freq = max(max_freq, freq[current_char]) 

            # if the number of replacements needed is greater than k then move the left pointer to the right
            while (right - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1

            # update the max_length
            max_length = max(max_length, (right -left + 1))

        return max_length
    
# Time Complexity: O(n)
# Space Complexity: O(1) since the size of the frequency dictionary is fixed at 26

if __name__ == "__main__":
    s = "XYYX"
    k = 2
    sol = Solution()
    print(sol.characterReplacement(s, k)) 

    s = "AAABABB"
    k = 1
    sol = Solution()
    print(sol.characterReplacement(s, k))



            