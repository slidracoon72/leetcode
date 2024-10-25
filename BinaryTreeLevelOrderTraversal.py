import collections
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Solving using Breadth First Search (BFS)
# Time Complexity: O(N)
# Neetcode: https://www.youtube.com/watch?v=6ZnyEApgFYg
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque()  # BFS uses a queue data structure
        q.append(root)

        while q:
            qLen = len(q)
            level = []  # to append elements of a particular level
            for _ in range(qLen):
                node = q.popleft()  # pop left value in a queue
                if node:
                    level.append(node.val)
                    # add children to queue
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)

        return res
