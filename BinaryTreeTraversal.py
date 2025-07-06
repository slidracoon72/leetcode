from typing import Optional, List


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTreeTraversal:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result = []
        result += self.inorderTraversal(root.left)
        result.append(root.val)
        result += self.inorderTraversal(root.right)
        return result

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result = []
        result.append(root.val)
        result += self.preorderTraversal(root.left)
        result += self.preorderTraversal(root.right)
        return result

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result = []
        result += self.postorderTraversal(root.left)
        result += self.postorderTraversal(root.right)
        result.append(root.val)
        return result

    # Alternate - but similar DFS solutions
    def inorderTraversal1(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            res.append(node.val)
            inorder(node.right)

        inorder(root)
        return res

    def preorderTraversal1(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def preorder(node):
            if not node:
                return

            res.append(node.val)
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return res

    def postorderTraversal1(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def postorder(node):
            if not node:
                return

            postorder(node.left)
            postorder(node.right)
            res.append(node.val)

        postorder(root)
        return res


# Example usage:
# Constructing the BST:    2
#                         / \
#                        1   3
bst = TreeNode(2)
bst.left = TreeNode(1)
bst.right = TreeNode(3)

# Initialize the BST class
bst_traversal = BinaryTreeTraversal()

# Inorder traversal
print("Inorder traversal:", bst_traversal.inorderTraversal(bst))  # Output: [1, 2, 3]

# Preorder traversal
print("Preorder traversal:", bst_traversal.preorderTraversal(bst))  # Output: [2, 1, 3]

# Postorder traversal
print("Postorder traversal:", bst_traversal.postorderTraversal(bst))  # Output: [1, 3, 2]
