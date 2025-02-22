"""
Reorder Linked List
Proble: LeetCode 143 - Reorder List
Difficulty: Medium

Problem statement:
You are given the head of a singly linked-list.

The positions of a linked list of length = 7 for example, can intially be represented as:
[0, 1, 2, 3, 4, 5, 6]

Reorder the nodes of the linked list to be in the following order:
[0, 6, 1, 5, 2, 4, 3]

Notice that in the general case for a list of length = n the nodes are 
reordered to be in the following order: [0, n-1, 1, n-2, 2, n-3, ...]

You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.

Example 1:
Input: head = [2,4,6,8]
Output: [2,8,4,6]

Example 2:
Input: head = [2,4,6,8,10]
Output: [2,10,4,8,6]

Constraints:
1 <= Length of the list <= 1000.
1 <= Node.val <= 1000
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next or not head.next.next:
            return      # no need to reorder if the list is 0, 1, 2

        # find the middle using Floyd's tortoise & hare alogorithm
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next        # move one step 
            fast = fast.next.next   # move two step 

        # Reverse the second half of the list
        prev, curr = None, slow.next    # previous, current
        slow.next = None                # split the list into two halves
        while curr:
            next_node = curr.next
            curr.next = prev        # reverse the pointer
            prev = curr
            curr = next_node
        second_half = prev      # head of the second half (reversed)

        # merge the two half alternatively
        first, second = head, second_half

        while second:
            tmp1, tmp2 = first.next, second.next    # save next nodes
            first.next = second     # insert node from second half
            second.next = tmp1      # link back to the first half
            first, second = tmp1, tmp2  # move pointers
