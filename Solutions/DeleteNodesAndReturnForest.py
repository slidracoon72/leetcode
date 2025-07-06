from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Neetcode: https://www.youtube.com/watch?v=UhKu0q1yXHY
# Deleting a node: Update child ptr or return null
# Can delete all in O(n)
# res=set, if delete node, remove from res and add children to result
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        # Convert to_delete list to a set for O(1) lookup time.
        delete_set = set(to_delete)
        # Initialize result_set with the root node.
        result_set = {root}

        def dfs(node):
            if not node:
                return None  # Base case: If the node is None, return None.

            res = node
            # Check if the current node needs to be deleted.
            if node.val in delete_set:
                res = None  # Mark the node for deletion by setting res to None.
                result_set.discard(node)  # Remove the node from the result set.

                # If the node has a left child, add it to the result set.
                if node.left:
                    result_set.add(node.left)
                # If the node has a right child, add it to the result set.
                if node.right:
                    result_set.add(node.right)

            # Recursively process the left and right children.
            # Update the left child of the current node.
            node.left = dfs(node.left)
            # Update the right child of the current node.
            node.right = dfs(node.right)

            return res  # Return the current node if it is not deleted, otherwise None.

        # Start the DFS from the root node.
        dfs(root)
        # Convert the result set to a list and return it.
        return list(result_set)

