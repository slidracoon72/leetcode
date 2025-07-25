from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Using an array
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        res = []
        cur = head

        # Traverse the linked list and collect the binary digits as strings
        while cur:
            res.append(str(cur.val))  # Convert binary digit to string and append
            cur = cur.next

        # Join all binary digits to form the binary number string
        res = "".join(res)

        # Convert binary string to decimal integer using base 2
        return int(res, 2)

    # Using Bit Manipulation - More space efficient
    def getDecimalValue1(self, head: Optional[ListNode]) -> int:
        result = 0
        current = head

        # Traverse the list and compute the decimal value directly
        while current:
            # Shift result left by 1 bit and add current node's value
            result = (result << 1) | current.val
            current = current.next

        return result
