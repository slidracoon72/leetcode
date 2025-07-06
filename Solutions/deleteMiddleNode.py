import math
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def deleteMiddleTwoPointer(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = slow = fast = ListNode(-math.inf)
        dummy.next = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next

        return dummy.next

    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        length = 0
        temp = head

        while temp:
            length += 1
            temp = temp.next
        mid = length // 2

        if mid == 0:
            return head.next

        count = 0
        temp = head
        while temp and temp.next:
            count += 1
            if count == mid:
                temp.next = temp.next.next
            temp = temp.next

        return head
