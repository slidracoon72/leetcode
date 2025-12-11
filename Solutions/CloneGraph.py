from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# Neetcode Solution: https://www.youtube.com/watch?v=mQeF6bN8hMk
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Dictionary to map original nodes to their corresponding clones
        oldToNew = {}

        # Depth-first search function to clone the graph
        def dfs(node):
            # If the node has already been cloned, return its clone
            if node in oldToNew:
                return oldToNew[node]
            # Create a new node with the same value as the original node
            copy = Node(node.val)
            # Add the original node and its clone to the mapping dictionary
            oldToNew[node] = copy
            # Recursively clone the neighbors of the original node
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        # If the input node is None, return None
        return dfs(node) if node else None
