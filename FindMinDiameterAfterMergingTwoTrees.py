# LC - Hard

import heapq
from collections import defaultdict
from math import ceil
from typing import List


# Neetcode: https://www.youtube.com/watch?v=tK1TLnhmXzw&ab_channel=NeetCodeIO
# Time: O(n+m), Space: O(n+m)
class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        m = len(edges1) + 1  # Number of nodes in the first tree
        n = len(edges2) + 1  # Number of nodes in the second tree

        # Helper function to build an adjacency list from edges
        def build_adj(edges):
            adj = defaultdict(list)  # Using defaultdict for convenience
            for n1, n2 in edges:
                adj[n1].append(n2)  # Add n2 to the adjacency list of n1
                adj[n2].append(n1)  # Add n1 to the adjacency list of n2
            return adj

        adj1 = build_adj(edges1)  # Build adjacency list for the first tree
        adj2 = build_adj(edges2)  # Build adjacency list for the second tree

        # Recursive function to calculate the diameter of a tree
        # Returns [diameter, max_leaf_path]
        def get_diameter(cur, par, adj):
            max_d = 0  # Maximum diameter found so far
            max_child_paths = [0, 0]  # Stores the two longest paths from children to leaves

            for nei in adj[cur]:  # Iterate through the neighbors of the current node
                if nei == par:  # Skip the parent node to avoid backtracking
                    continue

                # Recurse into the child node
                nei_d, nei_max_leaf_path = get_diameter(nei, cur, adj)
                max_d = max(max_d, nei_d)  # Update the maximum diameter

                # Update the two longest paths to leaves
                heapq.heappush(max_child_paths, nei_max_leaf_path)
                heapq.heappop(max_child_paths)  # Maintain only the top two values

            # Update the diameter to include paths through the current node
            max_d = max(max_d, sum(max_child_paths))
            return [max_d, 1 + max(max_child_paths)]  # Diameter and longest path to leaf

        # Calculate the diameter of both trees
        d1, _ = get_diameter(0, -1, adj1)  # Diameter of the first tree
        d2, _ = get_diameter(0, -1, adj2)  # Diameter of the second tree

        # Return the minimum possible diameter of the merged tree
        # Formula accounts for merging the two trees and their respective diameters
        return max(d1, d2, 1 + ceil(d1 / 2) + ceil(d2 / 2))


c = Solution()
edges1 = [[0, 1], [0, 2], [0, 3], [2, 4], [2, 5], [3, 6], [2, 7]]
edges2 = [[0, 1], [0, 2], [0, 3], [2, 4], [2, 5], [3, 6], [2, 7]]
print(c.minimumDiameterAfterMerge(edges1, edges2))
