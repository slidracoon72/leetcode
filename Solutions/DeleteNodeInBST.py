class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:  # Node to delete found

            # Node has only one child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            # Node has both left and right children
            # Find the inorder successor (smallest left node in the right subtree)
            successor = self.findSuccessor(root.right)
            # Copy the value of the successor to the current node
            root.val = successor.val
            # Delete the successor node
            root.right = self.deleteNode(root.right, successor.val)

        return root

    def findSuccessor(self, node: TreeNode) -> TreeNode:
        while node.left:
            node = node.left
        return node
