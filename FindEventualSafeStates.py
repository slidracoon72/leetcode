from typing import List


class Solution:
    # Solved using DFS - Recursive
    # Neetcode: https://www.youtube.com/watch?v=wciKkM3g3wQ&ab_channel=NeetCodeIO
    # Time: O(E + V), Space: O(V)
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)  # Number of nodes in the graph
        safe = {}  # Dictionary to memoize whether a node is safe or not

        # Helper function to perform DFS and determine if a node is safe
        def dfs(i) -> bool:
            if i in safe:  # If the safety of node `i` is already determined, return it
                return safe[i]

            safe[i] = False  # Mark the node as unsafe initially (to detect cycles)
            for nei in graph[i]:  # Traverse all neighbors of node `i`
                # If any neighbor is unsafe, the current node cannot be safe
                if not dfs(nei):
                    return False

            safe[i] = True  # If all neighbors are safe, mark the current node as safe
            return safe[i]

        res = []  # List to store all safe nodes
        for i in range(n):  # Iterate through all nodes in the graph
            if dfs(i):  # If the node is determined to be safe
                res.append(i)

        return res  # Return the list of safe nodes


c = Solution()
graph = [[1, 2], [2, 3], [5], [0], [5], [], []]
print(c.eventualSafeNodes(graph))
