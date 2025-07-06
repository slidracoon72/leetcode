from typing import List


class Solution:
    # Brute Force
    # Time: O(n^2), Space: O(1)
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)

        res = -1
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    res = max(res, nums[j] - nums[i])

        return res

    # Optimal - Similar to BestTimeToBuyAndSellStock.py
    # Time: O(n), Space: O(1)
    def maximumDifference1(self, nums: List[int]) -> int:
        n = len(nums)

        res = -1
        prev = nums[0]
        for i in range(1, n):
            if prev < nums[i]:
                res = max(res, nums[i] - prev)
            else:
                prev = nums[i]

        return res


c = Solution()
nums = [7, 1, 5, 4]
print(c.maximumDifference(nums))
print(c.maximumDifference1(nums))
