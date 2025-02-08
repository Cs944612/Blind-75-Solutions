"""
Group Anagrams
Problem: LeetCode 49 - Group Anagrams
Difficulty: Medium

Problem Statement:
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:
Input: strs = ["act","pots","tops","cat","stop","hat"]
Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

Example 2:
Input: strs = ["x"]
Output: [["x"]]

Example 3:
Input: strs = [""]
Output: [[""]]

Constraints:
1 <= strs.length <= 1000.
0 <= strs[i].length <= 100
strs[i] is made up of lowercase English letters.
"""
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        # create a dictionary to store the anagrams
        anagrams = defaultdict(list) 
        # iterate over each string in the input list
        for word in strs:
            # count the frequency of each character in the string and use it as a key in the dictionary
            count = [0] * 26 # since there are 26 lowercase English letters (a-z)
            for char in word:
                count[ord(char) - ord('a')] += 1 # ord() returns the ASCII value of the character
            anagrams[tuple(count)].append(word)

        return anagrams.values()


# Time Complexity: O(n * k) where n is the number of strings in the input list and k is the length of the longest string
# Space Complexity: O(n * k) where n is the number of strings in the input list and k is the length of the longest string

if __name__ == "__main__":
    # Example usage
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams(strs))
