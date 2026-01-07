from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        size = 0
        while cur:
            size += 1
            cur = cur.next

        if size == 1:
            return head

        middle = size // 2

        cur = head
        i = 0
        while cur:
            if i + 1 == middle:
                return cur.next
            i += 1
            cur = cur.next

    def middleNode1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
