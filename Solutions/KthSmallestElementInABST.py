import collections
import heapq
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Solved using Inorder-Traversal as it gives sorted output
    # Time: O(n), Space: O(n)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorderTraversal(root):
            if root is None:
                return []
            result = []
            result += inorderTraversal(root.left)
            result.append(root.val)
            result += inorderTraversal(root.right)
            return result

        return inorderTraversal(root)[k - 1]

    # Solved using Max-Heap
    # Time: O(nlogk), Space: O(n)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Max-heap (using negative values since Python only has min-heap by default)
        heap = []

        # Queue for level-order traversal (BFS)
        q = collections.deque()
        q.append(root)

        while q:
            node = q.popleft()

            # Push negative of node value to simulate max-heap
            heapq.heappush(heap, -node.val)

            # Maintain heap size of at most k
            if len(heap) > k:
                heapq.heappop(heap)  # Remove the largest among k+1 smallest values

            # Continue BFS traversal
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        # The k-th smallest is the largest value in the heap (invert sign back)
        return -heap[0]
