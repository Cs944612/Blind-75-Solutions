"""
Reverse Linked List
Problem: LeetCode 206 - Reverse Linked List
Difficulty: Easy

Problem Statement:
Given the beginning of a singly linked list head, 
reverse the list, and return the new beginning of the list.

Example 1:
Input: head = [0,1,2,3]
Output: [3,2,1,0]

Example 2:
Input: head = []
Output: []

Constraints:
0 <= The length of the list <= 1000.
-1000 <= Node.val <= 1000
"""

# defination for a singly-linked List
#class ListNode:
#    def __init__(self, val=0, next=None):
#       self.value = value
#       self.next = next

class Solution:
    def reverseList(self, head:Optional[ListNode]) -> Optional[ListNode]:
        # Initialize the pointers
        previous = None
        current = head

        # iterate through the list
        while current:
            next_node = current.next    # store the next node
            current.next = previous     # reverse the previous node's poninter
            previous = current          # move previous forward
            current = next_node         #move current forward

        # previous is now the head of the reversed list
        return previous

