from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for x in nums:
            if x != val:
                nums[i] = x
                i += 1
        return i


c = Solution()
nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
print(c.removeElement(nums, val))
