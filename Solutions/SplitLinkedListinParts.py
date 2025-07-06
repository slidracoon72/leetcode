from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Neetcode: https://www.youtube.com/watch?v=-OTlqdrxrVI
# Time: O(max(k, len(LinkedList)), Space: O(1)
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # Step 1: Calculate the total length of the linked list
        length = 0
        cur = head
        while cur:  # Traverse the list to count the number of nodes
            length += 1
            cur = cur.next

        # Step 2: Determine the base size of each part and the remainder
        base_len = length // k  # This is the minimum size of each part
        remainder = length % k  # These are the extra nodes that need to be distributed

        # Step 3: Initialize the result list and reset the cur pointer to head
        cur = head
        res = []

        # Step 4: Split the list into k parts
        for i in range(k):
            # Append the current node (which will be the start of the i-th part) to the result list
            res.append(cur)

            # Create a sublist of size `base_len + 1` if there are extra nodes left, otherwise of size `base_len`
            for j in range(base_len - 1 + (1 if remainder > 0 else 0)):
                if not cur:  # If cur becomes None, exit the loop
                    break
                cur = cur.next

            # Step 5: Decrease remainder after distributing an extra node
            remainder -= 1 if remainder > 0 else 0

            # Step 6: Break the link to create the end of the current part and move cur to the next part
            if cur:
                cur.next, cur = None, cur.next  # Break the current list and move to the next node

        # Step 7: Return the result list containing the split parts of the linked list
        return res
