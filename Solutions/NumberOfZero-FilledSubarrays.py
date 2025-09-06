from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        l, r = 0, 0
        while r < n:
            # skip non-zero elements
            while r < n and nums[r] != 0:
                r += 1
                l = r
            # find consecutive zeros
            while r < n and nums[r] == 0:
                r += 1
            k = r - l  # length of zero segment
            res += k * (k + 1) // 2
            l = r
        return res

    # Time: O(n), Space: O(1)
    def zeroFilledSubarray1(self, nums: List[int]) -> int:
        res = 0
        streak = 0
        for num in nums:
            if num == 0:
                streak += 1
                res += streak  # each 0 extends all subarrays ending here
            else:
                streak = 0
        return res


c = Solution()
nums = [1, 3, 0, 0, 2, 0, 0, 4]
print(c.zeroFilledSubarray(nums))
print(c.zeroFilledSubarray1(nums))
