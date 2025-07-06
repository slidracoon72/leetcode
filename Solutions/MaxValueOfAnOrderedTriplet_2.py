from typing import List


class Solution:
    # Time: O(n), Space: O(n)
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        left_max, right_max = [0] * n, [0] * n

        # fill prefix and suffix array
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], nums[i - 1])
            right_max[n - 1 - i] = max(right_max[n - i], nums[n - i])

        res = 0
        for j in range(1, n - 1):
            temp = (left_max[j] - nums[j]) * right_max[j]
            res = max(res, temp)

        return res


c = Solution()
nums = [12, 6, 1, 2, 7]
print(c.maximumTripletValue(nums))
