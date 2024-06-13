from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        print(len(set(nums)))
        x = 1
        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1]:
                nums[x] = nums[i + 1]
                x += 1
        return x


c = Solution()
a = [0, 1, 5, 5, 5, 5, 6, 7, 7, 7, 9]
print(c.removeDuplicates(a))
s = set(a)
print(s, len(s))
