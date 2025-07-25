from math import gcd
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Time: O(N), Space: O(1)
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = head, head.next
        while cur:
            g = ListNode(gcd(prev.val, cur.val), cur)
            prev.next = g
            prev, cur = cur, cur.next
        return head

    def insertGreatestCommonDivisors1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head

        while cur.next:
            g = gcd(cur.val, cur.next.val)
            new = ListNode(g, cur.next)
            cur.next = new
            cur = cur.next.next

        return head
