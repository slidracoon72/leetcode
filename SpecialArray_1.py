from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if not nums:
            return False
        if len(nums) == 1:
            return True

        for i in range(len(nums) - 1):
            # (odd + odd) and (even + even) = even
            if (nums[i] + nums[i + 1]) % 2 == 0:
                return False  # same parity
        return True  # alternating parity


c = Solution()
nums = [4, 3, 1, 6]
print(c.isArraySpecial(nums))
