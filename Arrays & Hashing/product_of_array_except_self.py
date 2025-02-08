"""
Products of Array Except Self
Problem: LeetCode 238 - Product of Array Except Self
Difficulty: Medium

Problem Statement:
Given an integer array nums, return an array output where output[i] is the 
product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in O(n)
O(n) time without using the division operation?

Example 1:
Input: nums = [1,2,4,6]
Output: [48,24,12,8]

Example 2:
Input: nums = [-1,0,1,2,3]
Output: [0,-6,0,0,0]

Constraints:
2 <= nums.length <= 1000
-20 <= nums[i] <= 20
"""
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        # calculate the left product of each element
        left_product = 1
        for num in range(len(nums)):
            result[num] *= left_product  # store the left product of the current element
            left_product *= nums[num]   # update the left product for the next element

        # calculate the right product of each element
        right_product = 1
        for num in range(len(nums) - 1, -1, -1):
            result[num] *= right_product    # store the right product of the current element
            right_product *= nums[num]      # update the right product for the next element
    
        return result

# Time Complexity: O(n) 
# Space Complexity: O(1) since we are using a single list to store the result

if __name__ == "__main__":
    # Example usage
    nums = [1, 2, 4, 6]
    print(Solution().productExceptSelf(nums))
    