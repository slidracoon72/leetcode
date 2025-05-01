import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if x < y:
                heapq.heappush(stones, -(y - x))

        return -stones[0] if stones else 0


c = Solution()
stones = [2, 7, 4, 1, 8, 1]
print(c.lastStoneWeight(stones))
