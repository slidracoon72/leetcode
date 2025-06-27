from typing import List


class Solution:
    # Time: O(N), Space: O(1)
    # Neetcode: https://www.youtube.com/watch?v=bNvIQI2wAjk
    def productExceptSelf(self, nums):
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res

    def productExceptSelf1(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        pref = [0] * n
        suff = [0] * n

        pref[0] = suff[n - 1] = 1
        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]
        for i in range(n - 2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]
        for i in range(n):
            res[i] = pref[i] * suff[i]
        return res

    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [1] * (n + 1)
        suff = [1] * (n + 1)
        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]
        for i in range(n - 2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]

        res = []
        for i in range(1, n + 1):
            res.append(pref[i - 1] * suff[i - 1])
        return res


c = Solution()
nums1 = [1, 2, 3, 4]
nums2 = [-1, 1, 0, -3, 3]
print(c.productExceptSelf1(nums1))
print(c.productExceptSelf1(nums2))
