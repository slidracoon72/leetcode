from typing import List


class Solution:
    # Time: O(n), Space: O(1)
    def check(self, nums: List[int]) -> bool:
        count = 0
        n = len(nums)

        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:  # Check if rotation break occurs
                count += 1
                if count > 1:  # More than one break means it's not a rotated sorted array
                    return False

        return True


c = Solution()
nums = [3, 4, 5, 1, 2]
print(c.check(nums))
