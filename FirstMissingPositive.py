# LC - Hard

class Solution:
    # Time: O(nlogn), Space: O(1)
    def firstMissingPositive(self, nums: list[int]) -> int:
        nums.sort()
        missing = 1

        for num in nums:
            if num > 0 and missing == num:
                missing += 1

        return missing


c = Solution()
nums = [1, 2, 0]
print(c.firstMissingPositive(nums))
