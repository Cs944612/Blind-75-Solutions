""" 
Contains Duplicate
Problem: LeetCode 217 - Contains Duplicate
difficulty: Easy

problem statement:
Given an integer array nums, return 
true if any value appears more than once in the array,
otherwise return false.

Example 1:
Input: nums = [1, 2, 3, 3]
Output: true

Example 2:
Input: nums = [1, 2, 3, 4]
Output: false
"""

from typing import List

class Soltuion:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create a set to store the unique values
        unique = set()
        # iterate through the list of numbers
        for num in nums:
            # if the number is already in the set, return True
            if num in unique:
                return True
            # add the number to the set
            unique.add(num)
        # return False if no duplicates are found
        return False
        

# Time complexity: O(n)
# Space complexity: O(n)

if __name__ == "__main__":
    # Example usage
    nums = [1, 2, 3, 3]
    print(Soltuion().hasDuplicate(nums))
