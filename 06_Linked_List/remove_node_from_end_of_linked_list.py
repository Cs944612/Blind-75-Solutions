"""
Remove Node From End of Linked List
Problem: LeetCode 19 - Remove Nth Node From End of List
Difficulty: Medium

Problem statement:
You are given the beginning of a linked list head, and an integer n.

Remove the nth node from the end of the list and return the beginning of the list.

Example 1:
Input: head = [1,2,3,4], n = 2
Output: [1,2,4]

Example 2:
Input: head = [5], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 2
Output: [2]

Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # create a dummy node 
        dummy = ListNode(0)
        dummy.next = head

        # initialize two pointers
        slow, fast = dummy, dummy

        # move pointers n steps ahead 
        for _ in range(n):
            fast = fast.next

        # move both pointers until fast reaches the end
        while fast.next:
            slow = slow.next
            fast = fast.next

        # remove the nth node from the list
        slow.next = slow.next.next

        # return the changes list (skip the dummy)
        return dummy.next 
