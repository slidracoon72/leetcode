from typing import Counter, List


class Solution:
    # Time: O(n), Space: O(n)
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c = Counter(nums)
        max_freq = max(c.values())

        res = 0
        for key, freq in c.items():
            if freq == max_freq:
                res += 1

        return res * max_freq


c = Solution()
nums = [1, 2, 2, 3, 1, 4]
nums1 = [1, 2, 3, 4, 5]
print(c.maxFrequencyElements(nums))
print(c.maxFrequencyElements(nums1))
