from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos, neg = 0, 0

        for x in nums:
            if x > 0:
                pos += 1
            elif x < 0:
                neg += 1

        return max(pos, neg)


c = Solution()
nums = [-3, -2, -1, 0, 0, 1, 2]
print(c.maximumCount(nums))
