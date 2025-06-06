from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1


c = Solution()
a1 = [-1, 0, 3, 5, 9, 12]
t1 = 9
t2 = 2
print(c.search(a1, t1))
print(c.search(a1, t2))
