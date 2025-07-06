from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# LC-3217: Delete Nodes From Linked List Present in Array
class Solution:
    # Time complexity: O(m+n) where m is the length of the linked list and n is the size of nums.
    # Space complexity: O(n) due to storing nums in a set for O(1) lookups.
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        # Convert nums to a set for faster O(1) lookups.
        nums = set(nums)

        # Create a dummy node to handle edge cases like removing the head node.
        dummy = ListNode(0, head)

        # Initialize pointers. 'prev' starts at the dummy node,
        # and 'cur' starts at the first actual node (head of the list).
        prev = dummy
        cur = dummy.next  # cur = head (this simplifies the code to avoid handling special cases)

        # Iterate through the linked list.
        while cur:
            # If the current node's value is in nums (should be removed):
            if cur.val in nums:
                # Remove the current node by pointing 'prev' to 'cur.next'
                prev.next = cur.next
            else:
                # Otherwise, move 'prev' to the current node.
                prev = prev.next
            # Move to the next node in the list.
            cur = cur.next

        # Return the head of the modified list, which is 'dummy.next' (skipping the dummy node).
        return dummy.next
        # Returning 'head' would also be correct if no nodes were removed.
