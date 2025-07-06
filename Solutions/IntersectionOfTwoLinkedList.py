from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Neetcode: https://www.youtube.com/watch?v=D0X0BONOQhI
# Time: O(m + n), Space: O(1)
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a, b = headA, headB
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a

    # Same code, with easier explanation
    def getIntersectionNode1(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a, b = headA, headB
        # Move pointer until a and b are not same (not yet intersected)
        # If 'a' exists, shift it.
        # Else, assign 'a' as 'headB'
        while a != b:
            if a:
                a = a.next
            else:
                a = headB

            if b:
                b = b.next
            else:
                b = headA
        return a
