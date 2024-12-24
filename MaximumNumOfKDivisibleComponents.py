# LC - Hard

from collections import defaultdict
from typing import List


class Solution:
    # Neetcode: https://www.youtube.com/watch?v=xlgOaIK-inc&ab_channel=NeetCodeIO
    # Time: O(n), Space: O(n)
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        # Create an adjacency list to represent the tree
        adj = defaultdict(list)

        # Build the adjacency list from the edges
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        # Variable to store the count of valid components
        res = 0

        # Depth-First Search (DFS) to calculate subtree sums and count valid components
        def dfs(cur, parent):
            # Start with the value of the current node
            total = values[cur]

            # Traverse all the child nodes of the current node
            for child in adj[cur]:
                # Skip the parent node to avoid revisiting
                if child != parent:
                    # Add the subtree sum of the child to the total
                    total += dfs(child, cur)

            # If the total sum of the current subtree is divisible by k, it forms a valid component
            if total % k == 0:
                nonlocal res  # Access the outer variable `res`
                res += 1

            # Return the total sum of the subtree rooted at the current node
            return total

        # Start DFS traversal from the root node (0), with no parent (-1)
        dfs(0, -1)

        # Return the total number of valid components found
        return res


c = Solution()
n = 7
edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]
values = [3, 0, 6, 1, 5, 2, 1]
k = 3
print(c.maxKDivisibleComponents(n, edges, values, k))
