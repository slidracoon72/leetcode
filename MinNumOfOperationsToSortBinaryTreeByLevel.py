import collections
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Solved using BFS
    # Time: O(nlogn), Space: O(n)
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        # Helper function to count the minimum number of swaps to sort an array
        def count_swaps(nums):
            # Create a map of numbers to their indices
            idx_map = {n: i for i, n in enumerate(nums)}

            # Create a sorted version of the array
            sorted_nums = sorted(nums)

            swaps = 0
            for i in range(len(nums)):
                # If the current number is not in the correct position
                if nums[i] != sorted_nums[i]:
                    swaps += 1  # Increment swap count

                    # Find the correct position of the current number
                    j = idx_map[sorted_nums[i]]

                    # Swap the current number with the correct number
                    nums[i], nums[j] = nums[j], nums[i]

                    # Update the index map to reflect the swap
                    idx_map[nums[i]] = i
                    idx_map[nums[j]] = j

            return swaps

        # Queue for level-order traversal
        q = collections.deque()
        q.append(root)

        res = 0  # To store the total number of swaps

        while q:
            level = []  # To store the values of the current level

            # Process all nodes in the current level
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)  # Add the node's value to the current level

                # Add left and right children to the queue
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            # Add the number of swaps needed to sort this level
            res += count_swaps(level)

        return res
