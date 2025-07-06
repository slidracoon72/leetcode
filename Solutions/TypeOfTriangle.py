from typing import List


class Solution:
    # Time: O(nlogn) = O(1) (as n = 3), Space: O(n)
    def triangleType(self, nums: List[int]) -> str:
        n = len(set(nums))  # O(n) space
        if n == 1:
            return "equilateral"
        else:
            nums.sort()
            if nums[0] + nums[1] > nums[2]:
                if n == 2:
                    return "isosceles"
                elif n == 3:
                    return "scalene"

        return "none"

    # Slightly optimized
    # Time: O(nlogn) = O(1) (as n = 3), Space: O(1)
    def triangleType1(self, nums: List[int]) -> str:
        nums.sort()
        if nums[0] + nums[1] <= nums[2]:
            return "none"
        elif nums[0] == nums[2]:
            return "equilateral"
        elif nums[0] == nums[1] or nums[1] == nums[2]:
            return "isosceles"
        else:
            return "scalene"


c = Solution()
nums = [8, 4, 2]
nums1 = [3, 4, 5]
print(c.triangleType(nums))
print(c.triangleType1(nums1))
