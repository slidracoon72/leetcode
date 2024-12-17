# LC-3264. Final Array State After K Multiplication Operations I
import heapq
from typing import List


class Solution:
    # Solved using Min-Heap
    # Time: O(klogn), Space: O(n)
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        minHeap = [(n, i) for i, n in enumerate(nums)]
        heapq.heapify(minHeap)

        for _ in range(k):
            x, i = heapq.heappop(minHeap)
            nums[i] = x * multiplier
            heapq.heappush(minHeap, (nums[i], i))

        return nums


c = Solution()
nums = [2, 1, 3, 5, 6]
k = 5
multiplier = 2
print(c.getFinalState(nums, k, multiplier))
