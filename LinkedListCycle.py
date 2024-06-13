# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # using Floyd's Tortoise and Hare algorithm
        # increasing slow by 1, fast by 2
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:  # this means there is a cycle if fast and slow meet
                return True
        return False


l = ListNode([1, 2])
c = Solution()

print(c.hasCycle(l))
