from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Solved using DFS and Hash-Set
class FindElements:
    # Time: O(n), Space: O(n)
    def __init__(self, root: Optional[TreeNode]):
        self.recovered = set()
        if root:
            root.val = 0
            self.dfs(root)

    def dfs(self, root: Optional[TreeNode]):
        if not root:
            return

        x = root.val
        self.recovered.add(x)

        if root.left:
            root.left.val = 2 * x + 1
            self.dfs(root.left)

        if root.right:
            root.right.val = 2 * x + 2
            self.dfs(root.right)

    # Time: O(1), Space: O(1)
    def find(self, target: int) -> bool:
        return target in self.recovered

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
