from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # if linked list (LL) empty, return
        if head is None:
            return None

        # calculating size of LL
        size = 0
        current_node = head
        while current_node:
            size += 1
            current_node = current_node.next

        # calculate index to remove node from
        index = size - n
        # if first element to be removed, change head
        if index == 0:
            return head.next

        # code for removing node
        current_node = head
        position = 0
        # traverse to the element one before the element to be removed
        while current_node and position + 1 != index:
            position = position + 1
            current_node = current_node.next

        if current_node:
            current_node.next = current_node.next.next

        return head

    # Similar as above - Optimized
    def removeNthFromEnd1(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        N = 0
        cur = head
        while cur:
            N += 1
            cur = cur.next

        removeIndex = N - n
        if removeIndex == 0:
            return head.next

        cur = head
        for i in range(N - 1):
            if (i + 1) == removeIndex:
                cur.next = cur.next.next
                break
            cur = cur.next
        return head
