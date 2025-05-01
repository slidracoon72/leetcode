from collections import defaultdict
from typing import List


class Solution:
    # Brute Force
    # Time: O(n^2), Space: O(n)
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        distinct = set(nums)
        res = 0
        for i in range(n):
            cur = set()
            for j in range(i, n):
                cur.add(nums[j])
                if cur == distinct:
                    res += 1
        return res

    # Sliding Window
    # Time: O(n), Space: O(n)
    def countCompleteSubarrays1(self, nums: List[int]) -> int:
        totalDistinct = len(set(nums))  # Total number of distinct elements in nums
        countMap = defaultdict(int)
        res = 0

        # Sliding window
        left = 0
        for right in range(len(nums)):
            countMap[nums[right]] += 1

            # Shrink window from the left while we have all distinct elements
            while len(countMap) == totalDistinct:
                res += len(nums) - right  # Add all valid sub-arrays starting at left
                countMap[nums[left]] -= 1
                if countMap[nums[left]] == 0:
                    del countMap[nums[left]]
                left += 1

        return res


c = Solution()
nums = [1, 3, 1, 2, 2]
print(c.countCompleteSubarrays1(nums))
