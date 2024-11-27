from collections import defaultdict
from typing import List


# Sliding Window
# Time: O(n), Space: O(n)
class Solution:
    # Most Optimal
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prev_idx = {}  # num -> prev index of num
        cur_sum = 0

        l = 0
        for r in range(len(nums)):
            cur_sum += nums[r]
            i = prev_idx.get(nums[r], -1)

            while l <= i or r - l + 1 > k:
                cur_sum -= nums[l]
                l += 1

            if r - l + 1 == k:
                res = max(res, cur_sum)

            prev_idx[nums[r]] = r

        return res

    # Using Hash Map
    def maximumSubarraySum1(self, nums: List[int], k: int) -> int:
        res = 0
        count = defaultdict(int)
        cur_sum = 0
        l = 0

        for r in range(len(nums)):
            cur_sum += nums[r]
            count[nums[r]] += 1

            if r - l + 1 > k:
                cur_sum -= nums[l]
                count[nums[l]] -= 1
                if count[nums[l]] == 0:
                    count.pop(nums[l])
                l += 1

            if r - l + 1 == k and len(count) == k:
                res = max(res, cur_sum)

        return res

    # Using Hash Set - Fastest on LC
    def maximumSubarraySum2(self, nums: List[int], k: int) -> int:
        res = 0
        cur_sum = 0
        l = 0
        num_set = set()

        for r in range(len(nums)):
            while nums[r] in num_set:
                # Shrink the window from the left if duplicate found
                num_set.remove(nums[l])
                cur_sum -= nums[l]
                l += 1

            num_set.add(nums[r])
            cur_sum += nums[r]

            # Check if the window size matches k
            if r - l + 1 == k:
                res = max(res, cur_sum)
                # Shrink the window to maintain size k
                num_set.remove(nums[l])
                cur_sum -= nums[l]
                l += 1

        return res


c = Solution()
nums = [1, 5, 4, 2, 9, 9, 9]
k = 3
print(c.maximumSubarraySum(nums, k))
