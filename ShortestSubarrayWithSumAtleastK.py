# LC - Hard
import heapq
from typing import List


class Solution:
    # Time: O(nlogn), Space: O(n)
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        res = float("inf")
        cur_sum = 0
        minHeap = []  # (prefix_sum, end_index)

        for r in range(len(nums)):
            cur_sum += nums[r]

            if cur_sum >= k:
                res = min(res, r + 1)

            # Find the min window ending at r
            while minHeap and cur_sum - minHeap[0][0] >= k:
                pre_sum, end_idx = heapq.heappop(minHeap)
                res = min(res, r - end_idx)
            heapq.heappush(minHeap, (cur_sum, r))

        return res if res != float("inf") else -1

    # Brute Force
    # Time: O(n^2) - TLE
    def shortestSubarray1(self, nums: List[int], k: int) -> int:
        res = float('inf')
        flag = False
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                sub_sum = sum(nums[i:j + 1])
                if sub_sum >= k:
                    res = min(res, j - i + 1)
                    flag = True

        return res if flag else -1
