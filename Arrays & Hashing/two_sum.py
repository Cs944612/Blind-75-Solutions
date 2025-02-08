"""
Two Sum
Problem: LeetCode 1 - Two Sum
Difficulty: Easy

Problem Statement:
Given an array of integers nums and an integer target, return the indices i and j 
such that nums[i] + nums[j] == target and i != j.
You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
Return the answer with the smaller index first.

Example 1:

Input: 
nums = [3,4,5,6], target = 7

Output: [0,1]
Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

Example 2:

Input: nums = [4,5,6], target = 10

Output: [0,2]
Example 3:

Input: nums = [5,5], target = 10

Output: [0,1]
Constraints:

2 <= nums.length <= 1000
-10,000,000 <= nums[i] <= 10,000,000
-10,000,000 <= target <= 10,000,000

"""


from typing import List

class Solution:
    def twoSum(nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store the difference and its index
        num_dict = {}
        # Create a dictionary to store the value and its index
        dict = {}
        # iterate through the list of numbers and their indices
        for i, num in enumerate(nums):
            if (diff :=target - num) in dict:
                return [dict[diff], i]
            dict[num] = i
        else:
            return []

# Time complexity: O(n)
# Space complexity: O(n)

# Example usage:
nums = [2, 7, 11, 15]
target = 9
print(Solution.twoSum(nums, target)) 
