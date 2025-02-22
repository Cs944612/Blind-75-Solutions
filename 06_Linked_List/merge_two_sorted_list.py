"""
Merge Two Sorted Linked Lists
Problem: LeetCode 21 - Merge Two Sorted Lists
Difficulty: easy

Problem statement:
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted linked list and return 
the head of the new sorted linked list.

The new list should be made up of nodes from list1 and list2.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,5]
Output: [1,1,2,3,4,5]

Example 2:
Input: list1 = [], list2 = [1,2]
Output: [1,2]

Example 3:
Input: list1 = [], list2 = []
Output: []
 
Constraints:
0 <= The length of the each list <= 100.
-100 <= Node.val <= 100
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # create a dummy node to simplify the list handling
        dummy = ListNode(-1)
        current = dummy     # Pointer to track the merged list 

        # traverse both the list
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next      # move list1 forward
            else:
                current.next = list2
                list2 = list2.next      # move list2 forward
            current = current.next      # move merged list pointer

        # attach the remaining 
        current.next = list1 if list1 else list2

        return dummy.next           # return the merged list (skip the dummy node)
