"""
Merge K Sorted Linked Lists
Problem: LeetCode 121 - Merge k Sorted Lists
Difficulty: Hard

Problem statement:
You are given an array of k linked lists lists, where each list is sorted in ascending order.

Return the sorted linked list that is the result of merging all of the individual linked lists.

Example 1:
Input: lists = [[1,2,4],[1,3,5],[3,6]]
Output: [1,1,2,3,3,4,5,6]

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []

Constraints:
0 <= lists.length <= 1000
0 <= lists[i].length <= 100
-1000 <= lists[i][j] <= 1000
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Filter out empty lists
        lists = [lst for lst in lists if lst]
        
        # If no lists provided, return None
        if not lists:
            return None
        
        # If the list is 1, return as it is
        if len(lists) == 1:
            return lists[0]
        
        # Using divide & conquer, merge lists in pairs
        while len(lists) > 1:
            merged_lists = []
            
            # Merge and process the lists
            for i in range(0, len(lists), 2):
                l1 = lists[i]  # List 1
                l2 = lists[i + 1] if i + 1 < len(lists) else None  # Handle odd number of lists
                merged_lists.append(self.mergeTwoLists(l1, l2))
            
            lists = merged_lists  # Update the lists with new merged lists
        
        return lists[0]  # The last remaining list
    
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)  # Dummy node
        curr = dummy  # Current pointer to build the merged list
        
        # Merge both lists by selecting the smallest node
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next  # Move to the next node
        
        # Attach the remaining nodes from the list
        curr.next = l1 if l1 else l2
        
        return dummy.next
