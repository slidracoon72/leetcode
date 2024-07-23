from collections import Counter
from typing import List


# Time: o(n + nlogn), Space: O(n)
# Neetcode: https://www.youtube.com/watch?v=Evq1SfUbhBg
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        # Sort according to frequency, if same frequency, sort by
        # -ve of the same numbers. eg. 3,4 -> -3 > -4 -> 4,3
        nums.sort(key=lambda x: (count[x], -x))
        return nums

    def frequencySort1(self, nums: List[int]) -> List[int]:
        # Can also do it this way
        count = Counter(nums)

        def custom_sort(n):
            return (count[n], -n)

        nums.sort(key=custom_sort)

        return nums


c = Solution()
nums = [1, 1, 2, 2, 2, 3]
print(c.frequencySort(nums))
print(c.frequencySort1(nums))
