from typing import List


class Solution:
    # Solved using Prefix-Sum
    # Time: O(n), Space: O(n)
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)
        pre_sum = [0] * (n + 1)

        for i, num in enumerate(nums):
            pre_sum[i + 1] = pre_sum[i] + num

        splits = 0
        for i in range(n - 1):
            cur = pre_sum[i + 1]
            remaining = total_sum - cur
            if cur >= remaining:
                splits += 1

        return splits

    # Similar Approach - Prefix array not required
    # Time: O(n), Space: O(1)
    def waysToSplitArray1(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        prefix_sum = 0
        splits = 0

        for i in range(len(nums) - 1):
            prefix_sum += nums[i]
            remaining_sum = total_sum - prefix_sum
            if prefix_sum >= remaining_sum:
                splits += 1

        return splits


c = Solution()
nums = [10, 4, -8, 7]
print(c.waysToSplitArray(nums))
print(c.waysToSplitArray1(nums))
