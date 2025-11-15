from typing import List


class Solution:
    # Time :O(n^2), Space: O(n)
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        while len(nums) > 1:
            newNums = []
            for i in range(len(nums) - 1):
                newNums.append((nums[i] + nums[i + 1]) % 10)
            nums = newNums

        return nums[0]


c = Solution()
nums = [1, 2, 3, 4, 5]
print(c.triangularSum(nums))
