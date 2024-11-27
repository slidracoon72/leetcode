from typing import List


# The node with no incoming edges is the strongest. If there are multiple such nodes, then there is no champion
class Solution:
    # Time: O(n), Space: O(n)
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        incoming = [0] * n

        for src, dst in edges:
            incoming[dst] += 1

        champion = []
        for i, incoming_count in enumerate(incoming):
            if not incoming_count:
                champion.append(i)

        return champion[0] if len(champion) == 1 else -1


c = Solution()
n = 3
edges = [[0, 1], [1, 2]]
print(c.findChampion(n, edges))
