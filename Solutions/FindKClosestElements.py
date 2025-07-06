import heapq
from typing import List


class Solution:
    # Using Heap
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []  # (diff, val)
        for num in arr:
            diff = abs(num - x)
            heapq.heappush(heap, (diff, num))

        res = []
        for _ in range(k):
            _, val = heapq.heappop(heap)
            res.append(val)

        return sorted(res)

    # Using Two-Pointers - More Optimal
    # Time: O(n-k), Space: O(k)
    def findClosestElements1(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1
        while r - l >= k:
            if abs(x - arr[l]) <= abs(x - arr[r]):
                r -= 1
            else:
                l += 1

        return arr[l: r + 1]
        # return arr[l: l + k] -> also correct


c = Solution()
print(c.findClosestElements1(arr=[1, 2, 3, 4, 5], k=4, x=3))
