import collections
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # Solved without using level's list
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        q = collections.deque()  # BFS uses a queue data structure
        q.append(root)

        # BFS is not recursive, it is iterative
        while q:
            qLen = len(q)
            for i in range(qLen):
                node = q.popleft()
                if i == qLen - 1:  # If it's the last node at this level
                    res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return res

    # solved using a level's list
    def rightSideView2(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        q = collections.deque()  # BFS uses a queue data structure
        q.append(root)

        while q:
            qLen = len(q)
            level = []
            for _ in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

            if level:
                res.append(level[-1])

        return res
