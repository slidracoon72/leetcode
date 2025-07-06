import heapq
import math
from typing import List


class Solution:
    # Solved using Max-Heap
    # Time: O(nlogn + klogn), Space: O(n)
    def pickGifts(self, gifts: List[int], k: int) -> int:
        maxHeap = [-1 * gift for gift in gifts]
        heapq.heapify(maxHeap)

        for _ in range(k):
            max_pile = -1 * heapq.heappop(maxHeap)
            heapq.heappush(maxHeap, -1 * math.floor(math.sqrt(max_pile)))

        # return -1 * sum(maxHeap) -> also works
        res = 0
        while maxHeap:
            res += -1 * heapq.heappop(maxHeap)

        return res


c = Solution()
gifts = [25, 64, 9, 4, 100]
k = 4
print(c.pickGifts(gifts, k))
