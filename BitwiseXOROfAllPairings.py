from typing import List


class Solution:
    # Brute Force - Gives TLE
    # Time: O(m * n), Space: O(1)
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        for n1 in nums1:
            for n2 in nums2:
                res ^= (n1 ^ n2)

        return res

    # Neetcode: https://www.youtube.com/watch?v=H9zVwDf6Frk&ab_channel=NeetCodeIO
    # Time: O(m + n), Space: O(1)
    # If both nums1 and nums2 have even lengths, the XOR of all pairs will always be 0.
    # If one of them has an odd length, the result will be the XOR of all elements from the other array.
    # If both have odd lengths, the result will be the XOR of all elements from both arrays.
    def xorAllNums1(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0

        if len(nums1) % 2 == 1:
            for n in nums2:
                res ^= n

        if len(nums2) % 2 == 1:
            for n in nums1:
                res ^= n

        return res


c = Solution()
nums1 = [2, 1, 3]
nums2 = [10, 2, 5, 0]
print(c.xorAllNums1(nums1, nums2))
