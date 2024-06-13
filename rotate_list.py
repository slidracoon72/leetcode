from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Neetcode: https://www.youtube.com/watch?v=UcGtPs2LE_c
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        # Get length of linked list
        length, tail = 1, head
        while tail.next:
            length += 1
            tail = tail.next

        # If k is greater than length
        k = k % length  # (eg. 6 % 5 = 1, thus 6 rotations ~ 1 rotation)
        # no rotations required (as 5 rotations ~ 0 rotation; if k=length=5)
        if k == 0:
            return head

        # Move to pivot and rotate
        cur = head
        for i in range(length - k - 1):
            cur = cur.next
        newHead = cur.next
        cur.next = None
        tail.next = head

        return newHead
