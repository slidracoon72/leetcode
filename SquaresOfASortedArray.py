import heapq
from typing import List


class Solution:
    # Using Two-Pointers
    # Time: O(n), Space: O(1)
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        pos = n - 1

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[pos] = nums[left] ** 2
                left += 1
            else:
                result[pos] = nums[right] ** 2
                right -= 1
            pos -= 1

        return result

    # Using Min-Heap (less efficient)
    def sortedSquares(self, nums: List[int]) -> List[int]:
        heap = []
        for n in nums:
            heapq.heappush(heap, n * n)

        result = []
        while heap:
            result.append(heapq.heappop(heap))

        return result
