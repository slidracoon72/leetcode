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
            return

        # calculating size of LL
        size = 0
        if head:
            current_node = head
            while current_node:
                size += 1
                current_node = current_node.next

        # calculate index to remove node from
        index = size - n

        # code for removing node
        current_node = head
        position = 0

        # if first element to be removed, change head
        if position == index:
            head = head.next
        else:
            # traverse to the element one before the element to be removed
            while current_node != None and position + 1 != index:
                position = position + 1
                current_node = current_node.next

            if current_node != None:
                current_node.next = current_node.next.next

        return head