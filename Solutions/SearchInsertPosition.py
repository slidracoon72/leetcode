from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        res = len(nums)
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res


c = Solution()
a = [1, 3, 5, 6]
t1, t2, t3 = 5, 2, 7

# print(c.search_insert(a,t1))
# print(c.search_insert(a,t2))
print(c.searchInsert(a,t3))

