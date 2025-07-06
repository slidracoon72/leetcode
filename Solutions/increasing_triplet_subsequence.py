from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        first = second = float('inf')

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True

        return False


c = Solution()
nums = [20, 100, 10, 12, 5, 13]
print(c.increasingTriplet(nums))
