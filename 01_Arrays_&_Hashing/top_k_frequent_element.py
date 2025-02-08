"""
Top K Frequent Elements
Problem: LeetCode 347 - Top K Frequent Elements
Difficulty: Medium

Problem Statement:
Given an integer array nums and an integer k, return the k most frequent elements within the array.
The test cases are generated such that the answer is always unique.
You may return the output in any order.

Example 1:
Input: nums = [1,2,2,3,3,3], k = 2
Output: [2,3]

Example 2:
Input: nums = [7,7], k = 1
Output: [7]

Constraints:
1 <= nums.length <= 10^4.
-1000 <= nums[i] <= 1000
1 <= k <= number of distinct elements in nums.
"""

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Dictionary to store the frequency of each element
        count = {}
        # List of lists to store elements by their frequency
        freq = [[] for _ in range(len(nums) + 1)]

        # Count the frequency for each element
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # Group elements by frequency
        for key, value in count.items():
            freq[value].append(key)

        res = []
        # Iterate backwards over possible frequencies
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

# Time Complexity: O(n)
# Space Complexity: O(n)

# Example usage
if __name__ == "__main__":
    nums = [1, 2, 2, 3, 3, 3]
    k = 2
    print(Solution().topKFrequent(nums, k))