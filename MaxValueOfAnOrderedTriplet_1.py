from typing import List


class Solution:
    # Brute Force Approach
    # Time: O(n^3), Space: O(1)
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    res = max(res, (nums[i] - nums[j]) * nums[k])

        return max(res, 0)

    # Greedy + Prefix Suffix Array
    # Time: O(n), Space: O(n)
    def maximumTripletValue1(self, nums: List[int]) -> int:
        n = len(nums)
        left_max, right_max = [0] * n, [0] * n

        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], nums[i - 1])  # prefix array
            right_max[n - 1 - i] = max(right_max[n - i], nums[n - i])  # suffix array

        res = 0
        for j in range(1, n - 1):
            res = max(res, (left_max[j] - nums[j]) * right_max[j])

        return res


c = Solution()
nums = [12, 6, 1, 2, 7]
print(c.maximumTripletValue(nums))
print(c.maximumTripletValue1(nums))
