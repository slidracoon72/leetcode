class Solution:
    def longestOnes(self, nums, k: int) -> int:
        l = max_cons = 0

        for r, num in enumerate(nums):
            k -= 1 - num

            if k < 0:
                k += 1 - nums[l]
                l += 1
            else:
                max_cons = max(max_cons, r - l + 1)

        return max_cons


c = Solution()
nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
k = 3
print(c.longestOnes(nums, k))
