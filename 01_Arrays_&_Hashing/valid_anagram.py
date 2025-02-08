# Valid Anagram
# Problem: LeetCode 242 - Valid Anagram 
# Difficulty: Easy

# Problem statement:
# Given two strings s and t, return true if the two strings are anagrams of each other,
# otherwise return false.

# An anagram is a string that contains the exact same characters as another string,
# but the order of the characters can be different.

# Example 1:
# Input: s = "racecar", t = "carrace"
# Output: true

# Example 2:
# Input: s = "jar", t = "jam"
# Output: false

# Constraints:
# s and t consist of lowercase English letters.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if the length of the two strings are not equal, return False
        if len(s) != len(t):
            return False
        
        # create a dictionary to store the frequency of characters in the first string
        freq = {}

        # update frequency count for s
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        # decrement frequency count for t
        for char in t:
            if char not in freq or freq[char] == 0:
                return False
            freq[char] -= 1
        
        # if all counts are zero, then the strings are anagrams, return true
        return True
    
# Time complexity: O(n) 
# Space complexity: O(n) 

if __name__ == "__main__":
    # Example usage:
    s = "racecar"
    t = "carrace"
    print(Solution().isAnagram(s, t)) 