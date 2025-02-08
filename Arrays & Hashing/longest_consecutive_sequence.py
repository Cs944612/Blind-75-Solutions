"""
Longest Consecutive Sequence
Problem: LeetCode 128 -Longest Consecutive Sequence
Difficulty: Hard

Problem Statement:
Given an array of integers nums, return the length of the longest consecutive sequence
of elements that can be formed.
A consecutive sequence is a sequence of elements in which each element is exactly
1 greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [2,20,4,10,3,4,5]
Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].

Example 2:
Input: nums = [0,3,2,5,4,6,1,1]
Output: 7
Explanation: The longest consecutive sequence is [0, 1, 2, 3, 4, 5, 6].

Constraints:
0 <= nums.length <= 1000
-10^9 <= nums[i] <= 10^9
"""
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # create a set
        num_set = set(nums)
        result = 0      # initialize the result & length

        # iterate through the set
        for num in nums:
            # check if the number is the first number in the sequence
            if (num - 1) is not num_set:
                length = 0
                while (num + length) in num_set:
                    length += 1
                # update the result
                result = max(length, result)
        return result
    
# Time Complexity: O(n)
# Space Complexity: O(n)

if __name__ == "__main__":
    # Example usage
    nums = [2,20,4,10,3,4,5]
    print(Solution().longestConsecutive(nums)) 