from typing import List


class Solution:
    # Time: O(n^2), Space: O(1)
    def countPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] == nums[j] and i * j % k == 0:
                    res += 1
        return res


c = Solution()
nums = [3, 1, 2, 2, 2, 1, 3]
k = 2
print(c.countPairs(nums, k))
