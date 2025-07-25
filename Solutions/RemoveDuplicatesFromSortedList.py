from typing import Optional


# Definition for a singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head  # Start from the head of the list

        # Traverse the list until the end
        while cur and cur.next:
            # If the current node has the same value as the next one, skip the next node
            if cur.val == cur.next.val:
                cur.next = cur.next.next  # Remove the duplicate node
            else:
                cur = cur.next  # Move to the next node if values are different

        # Return the updated head of the list
        return head
