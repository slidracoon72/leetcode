from typing import List


# Neetcode: https://www.youtube.com/watch?v=XEmy13g1Qxc
# Quick Select Solution: Time: O(n) - average case, O(n^2) - worst case
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickSelect(l, r):
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if k < p:
                return quickSelect(l, p - 1)
            elif k > p:
                return quickSelect(p + 1, r)
            else:
                return nums[p]

        return quickSelect(0, len(nums) - 1)


c = Solution()
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(c.findKthLargest(nums, k))
