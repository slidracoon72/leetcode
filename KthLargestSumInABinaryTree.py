import heapq
from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        level_sums = []
        q = deque()
        q.append(root)

        while q:
            qLen = len(q)
            res = 0
            for _ in range(qLen):
                node = q.popleft()
                if node:
                    res += node.val
                    q.append(node.left)
                    q.append(node.right)
            if res:
                level_sums.append(res)

        if len(level_sums) < k:
            return -1
        else:
            level_sums.sort()
            return level_sums[-k]

    # Using Min-Heap to store only top k values
    # Slightly efficient
    def kthLargestLevelSum1(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1

        min_heap = []
        q = deque([root])

        while q:
            level_sum = 0
            for _ in range(len(q)):
                node = q.popleft()
                level_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            # Maintain a heap of size k
            heapq.heappush(min_heap, level_sum)
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # Check if we have at least k sums
        return min_heap[0] if len(min_heap) == k else -1
