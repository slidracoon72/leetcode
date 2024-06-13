from typing import List


class Solution:
    # Solving using Binary Search | Time: O(log n)
    # Neetcode: https://www.youtube.com/watch?v=U8XENwh8Oy8
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            # left sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # right sorted portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1

    def searchBruteForce(self, nums: List[int], target: int) -> int:
        for i, v in enumerate(nums):
            if v == target:
                return i
        return -1


c = Solution()
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(c.search(nums, target))
