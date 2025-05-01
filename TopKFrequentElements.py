import collections
import heapq
from typing import List


# Time Complexity : O(n * log(n))
# Space Complexity : O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = collections.Counter(nums)
        s = dict(sorted(c.items(), key=lambda item: item[1], reverse=True))
        l = []
        for c in s:
            l.append(c)
        return l[:k]

    # Similar, but a bit optimized
    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        c = collections.Counter(nums)
        c = dict(sorted(c.items(), key=lambda item: item[1], reverse=True))
        result = list(c.keys())[:k]
        return result

    # Using Min-Heap
    # Time: O(nlogk), Space: O(n + k)
    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

    # Using Max-Heap
    def topKFrequent3(self, nums: List[int], k: int) -> List[int]:
        c = collections.Counter(nums)  # Count frequencies: O(n) time

        # Use a max-heap (simulated via negative counts)
        max_heap = []
        for num, count in c.items():
            # Push tuples of (-count, num) to simulate a max-heap
            heapq.heappush(max_heap, (-count, num))  # O(n log n) time

        # Extract the top k elements
        res = []
        for _ in range(k):
            # Pop the smallest tuple (which has the most negative count = highest frequency)
            res.append(heapq.heappop(max_heap)[1])  # O(k log n) time

        return res


c = Solution()
nums = [1, 1, 1, 2, 2, 2, 2, 3]
k = 2
print(c.topKFrequent(nums, k))
