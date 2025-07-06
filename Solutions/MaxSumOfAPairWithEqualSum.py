# LC - 2342: Max Sum of a Pair With Equal Sum of Digits

import heapq
from collections import defaultdict
from typing import List


class Solution:
    # Time: O(nlogn), Space: O(n)
    def maximumSum(self, nums: List[int]) -> int:
        # sum -> num map (max-heap)
        sum_nums = defaultdict(list)

        # Group numbers by their digit sum using a max-heap
        for num in nums:
            n = num
            digit_sum = 0
            while n:
                digit_sum += n % 10
                n = n // 10
            heapq.heappush(sum_nums[digit_sum], -num)

        res = -1

        # Find the maximum sum of two largest numbers in each group
        for heap in sum_nums.values():
            if len(heap) > 1:  # atleast one pair exists
                max1, max2 = -heapq.heappop(heap), -heapq.heappop(heap)
                res = max(res, max1 + max2)

        return res


c = Solution()
nums = [18, 43, 36, 13, 7]
print(c.maximumSum(nums))
