from collections import defaultdict
from typing import List


class Solution:
    # Indegree & Outdegree
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming = defaultdict(int)
        outgoing = defaultdict(int)

        for src, dst in trust:
            outgoing[src] += 1
            incoming[dst] += 1

        for i in range(1, n + 1):
            if outgoing[i] == 0 and incoming[i] == n - 1:
                return i

        return -1

    # Optimal
    def findJudge1(self, n: int, trust: List[List[int]]) -> int:
        delta = defaultdict(int)

        for src, dst in trust:
            delta[src] -= 1
            delta[dst] += 1

        for i in range(1, n + 1):
            if delta[i] == n - 1:
                return i

        return -1


c = Solution()
n = 4
trust = [[1, 3], [4, 3], [2, 3]]
print(c.findJudge1(n, trust))
