from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        l, r = 0, len(nums) - 1

        # Binary search to find one of the target positions
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                # Found the target, now find the start and end positions
                s, e = mid, mid
                # Extend s to the left
                while s > 0 and nums[s - 1] == target:
                    s -= 1
                # Extend e to the right
                while e < len(nums) - 1 and nums[e + 1] == target:
                    e += 1
                return [s, e]

        return [-1, -1]


c = Solution()
nums = [5, 7, 7, 8, 8, 10]
target = 8
print(c.searchRange(nums, target))
