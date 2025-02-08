"""
3Sum
Problem: LeetCode 15 - 3Sum
Difficulty: Medium

problem statement:
Given an integer array nums, return all the triplets [nums[i], nums[j], 
nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.
The output should not contain any duplicate triplets. 
You may return the output and the triplets in any order.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:
3 <= nums.length <= 1000
-10^5 <= nums[i] <= 10^5
"""
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            # if the current number is greater than 0, then the sum of the three numbers will be greater than 0
            # so we can break the loop
            if nums[i] > 0:
                break
            # if the current number is the same as the previous number, then we skip it
            elif i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    # skip the same number
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return result

# Time Complexity: O(n^2)
# Space Complexity: O(n) for sorting or O(1) if we don't consider the space for the output list

if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]
    s = Solution()
    print(s.threeSum(nums)) 


            