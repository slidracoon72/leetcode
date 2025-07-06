from typing import List


class Solution:
    # Using Sliding Window
    # Time: O(n), Space: O(1)
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0

        for i in range(n - 2):
            if nums[i] == 0:
                nums[i] = 1
                nums[i + 1] = not nums[i + 1] # flip
                nums[i + 2] = not nums[i + 2] # flip
                count += 1

        # check if last two elements are 1, since prior are forced
        if nums[n - 2] == 0 or nums[n - 1] == 0:
            return -1

        return count

    # Similar as above, but slower
    def minOperations1(self, nums: List[int]) -> int:
        res = 0
        i = 0
        while i < len(nums) - 2:
            if not nums[i]:
                for j in range(i, i + 3):
                    nums[j] = not nums[j]
                res += 1
            i += 1

        if all(x == 1 for x in nums):
            return res
        return -1


c = Solution()
nums = [0, 1, 1, 1, 0, 0]
print(c.minOperations(nums))
print(c.minOperations1(nums))
nums = [0, 1, 1, 1, 0, 0]
print(c.minOperations1(nums))
