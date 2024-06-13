import collections
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Solved using BFS - Optimized version
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_sum = float('-inf')
        max_level = 1

        q = collections.deque()
        q.append(root)

        cur_level = 1
        while q:
            q_len = len(q)
            level_sum = 0

            for _ in range(q_len):
                node = q.popleft()
                level_sum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if level_sum > max_sum:
                max_sum = level_sum
                max_level = cur_level

            cur_level += 1

        return max_level

    # Solved using BFS - using list to store level values
    def maxLevelSum1(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_sum = float('-inf')
        max_level = 1

        q = collections.deque()
        q.append(root)

        cur_level = 1
        while q:
            qLen = len(q)
            level_members = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level_members.append(node.val)
                    # add children to queue
                    q.append(node.left)
                    q.append(node.right)

            if level_members:
                level_sum = sum(level_members)
                if level_sum > max_sum:
                    max_sum = level_sum
                    max_level = cur_level

            cur_level += 1

        return max_level
