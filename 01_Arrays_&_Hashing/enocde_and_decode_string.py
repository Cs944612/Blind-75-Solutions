"""
Encode and Decode Strings
Problem: LeetCode 271 - Encode and Decode Strings
difficulty level: Medium

Problem statement:
Design an algorithm to encode a list of strings to a single string.
The encoded string is then decoded back to the original list of strings.
Please implement encode and decode

Example 1:
Input: ["neet","code","love","you"]
Output:["neet","code","love","you"]

Example 2:
Input: ["we","say",":","yes"]
Output: ["we","say",":","yes"]

Constraints:
0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters.
"""
from typing import List
class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "/" + s # encoding logic (size of the string + "/" + string)
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded, i = [], 0
        while i < len(s):
            delimiter = s.find("/", i)  # Find the delimiter
            size = int(s[i:delimiter])  # Get the size of the string
            start_pos = delimiter + 1  
            end_pos = start_pos + size  
            decoded.append(s[start_pos:end_pos])
            i = end_pos  # Move the index to the end of the current string
        return decoded

# Time complexity: O(n)
# Space complexity: O(n)

if __name__ == "__main__":
    # Test cases
    test = Solution()
    strs = ["neet","code","love","you"]
    print(f"Input value: {strs}")
    encoded = test.encode(strs)
    print(f"After Encoding: {encoded}")
    decoded = test.decode(encoded)
    print(f"After Decoding: {decoded}")
    
