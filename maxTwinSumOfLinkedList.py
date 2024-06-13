# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Function to reverse a linked list
        def reverse_linked_list(head):
            prev = None
            curr = head
            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev

        # Function to find the midpoint of the linked list
        def find_mid(head):
            slow = fast = head
            while fast.next and fast.next.next:
                slow = slow.next  # Move slow by one step each time
                fast = fast.next.next  # Move fast by two steps each time
            return slow

        # Find the midpoint of the linked list
        mid = find_mid(head)

        # Break the linked list into two halves
        l1 = head
        l2 = mid

        # Reverse the second half of the linked list if it exists
        if l2:
            l2 = reverse_linked_list(l2)

        max_sum = float('-inf')  # Initialize max_sum to negative infinity

        # Iterate until one of l1 or l2 becomes None
        while l1 and l2:
            max_sum = max(max_sum, l1.val + l2.val)
            l1 = l1.next
            l2 = l2.next

        return max_sum


c = Solution()
# Test cases
# Example 1
head1 = ListNode(5)
head1.next = ListNode(4)
head1.next.next = ListNode(2)
head1.next.next.next = ListNode(1)
print(c.pairSum(head1))  # Output: 6

# Example 2
head2 = ListNode(4)
head2.next = ListNode(2)
head2.next.next = ListNode(2)
head2.next.next.next = ListNode(3)
print(c.pairSum(head2))  # Output: 7

# Example 3
head3 = ListNode(1)
head3.next = ListNode(100000)
print(c.pairSum(head3))  # Output: 100001
