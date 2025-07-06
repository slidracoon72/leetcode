import heapq
from typing import List

# Time: O(nlogn), Space: O(n)
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        res = 0

        while len(nums) >= 2:
            x, y = heapq.heappop(nums), heapq.heappop(nums)
            if x >= k:
                return res

            temp = min(x, y) * 2 + max(x, y)
            heapq.heappush(nums, temp)
            res += 1

        return res

    # Similar as above
    def minOperations1(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        res = 0
        while nums[0] < k:
            x, y = heapq.heappop(nums), heapq.heappop(nums)
            heapq.heappush(nums, x * 2 + y)
            res += 1

        return res


c = Solution()
nums = [1, 1, 2, 4, 9]
k = 20
print(c.minOperations(nums, k))
nums = [1, 1, 2, 4, 9]
print(c.minOperations1(nums, k))
