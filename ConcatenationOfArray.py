from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for _ in range(2):
            for n in nums:
                ans.append(n)
        return ans


c = Solution()
nums = [1, 3, 2, 1]
print(c.getConcatenation(nums))
