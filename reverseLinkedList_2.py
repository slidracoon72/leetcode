from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Neetcode: https://www.youtube.com/watch?v=RF_M9tX4Eag
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        # 1) Reach node at position left
        leftPrev, cur = dummy, head
        for i in range(left - 1):
            leftPrev, cur = cur, cur.next

        # 2) Now, cur = 'left', leftPrev = 'node before left'
        # Reverse from left to right
        prev = None
        for i in range(right - left + 1):
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        # 3) Update pointers
        leftPrev.next.next = cur  # cur is node after 'right'
        leftPrev.next = prev  # prev is node at 'right'

        # Exclude dummy point, thus return next of dummy
        return dummy.next
