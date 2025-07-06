import heapq
from typing import List


class Solution:
    # Time: O(n * log k), Space: O(k)
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # Min-heap to store the top k largest elements along with their indices
        heap = []

        # Iterate over nums with both value (num) and index (i)
        for i, num in enumerate(nums):
            # Push (num, index) into the heap
            heapq.heappush(heap, (num, i))
            # If heap size exceeds k, pop the smallest element
            if len(heap) > k:
                heapq.heappop(heap)

        # Sort the heap based on index to preserve the original order in subsequence
        heap.sort(key=lambda x: x[1])

        # Extract only the numbers from the sorted heap to form the subsequence
        return [num for num, i in heap]


c = Solution()
print(c.maxSubsequence(nums=[2, 1, 3, 3], k=2))
