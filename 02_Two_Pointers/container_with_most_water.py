"""
Container With Most Water
Problem: LeetCode 11 - Container With Most Water
Difficulty: Medium

Problem statement:
You are given an integer array heights where heights[i] represents the height of the 
ith bar.You may choose any two bars to form a container. 
Return the maximum amount of water a container can store.

Example 1:
Input: height = [1,7,2,5,4,7,3,6]
Output: 36

Example 2:
Input: height = [2,2,2]
Output: 4

Constraints:
2 <= height.length <= 1000
0 <= height[i] <= 1000
"""

from typing import List
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_area = 0

        while left < right:
            # calculate the area of the container with the current left and right pointers
            current_area = min(heights[left], heights[right]) * (right - left)
            # update the max_area
            max_area = max(max_area, current_area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_area

# Time complexity: O(n) 
# Space complexity: O(1)

if __name__ == "__main__":
    # Example usage
    s = Solution()
    print(s.maxArea([1,7,2,5,4,7,3,6])) 