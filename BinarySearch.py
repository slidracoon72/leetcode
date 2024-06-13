from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            # m = l + ((r-l) // 2) this avoids overflow
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1


c = Solution()
a1 = [-1, 0, 3, 5, 9, 12]
t1 = 9
t2 = 2
print(c.search(a1, t1))
print(c.search(a1, t2))
