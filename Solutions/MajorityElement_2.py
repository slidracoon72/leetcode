from typing import List, Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count = Counter(nums)

        res = []
        for key, val in count.items():
            if val > n // 3:
                res.append(key)

        return res


c = Solution()
nums = [3, 2, 3]
print(c.majorityElement(nums))
