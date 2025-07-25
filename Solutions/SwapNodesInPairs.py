from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Linked List
    # Time: O(n), Space: O(1)
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node pointing to head to handle edge cases (like swapping the first pair)
        dummy = ListNode(0, head)
        prev, cur = dummy, head

        # Traverse the list while there are at least two nodes to swap
        while cur and cur.next:
            temp = cur.next.next  # Store the next pair's start
            second = cur.next  # The second node of the current pair

            # Perform the swap
            second.next = cur  # second → first
            cur.next = temp  # first → next pair
            prev.next = second  # link previous node to the new first (second)

            # Move pointers forward for next swap
            prev = cur
            cur = temp

        # Return the new head (which is dummy.next)
        return dummy.next
