from collections import Counter
from typing import List


# Neetcode: https://www.youtube.com/watch?v=XPPs2Wj2YSk
class Solution:
    # Two-pointer solution using sorting
    # Time: O(nlogn)
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        res = 0

        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:
                res += 1 + (nums[i - 1] - nums[i])
                nums[i] = nums[i - 1] + 1

        return res

    # Counting Sort solution
    # Time: O(N + max(nums))
    def minIncrementForUnique1(self, nums: List[int]) -> int:
        count = Counter(nums)
        print(count)
        res = 0

        for i in range(len(nums) + max(nums)):
            if count[i] > 1:
                extra = count[i] - 1
                count[i + 1] += extra
                res += extra

        return res


c = Solution()
nums = [3, 2, 1, 2, 1, 7]
print(c.minIncrementForUnique(nums))
nums = [3, 2, 1, 2, 1, 7]
print(c.minIncrementForUnique1(nums))
