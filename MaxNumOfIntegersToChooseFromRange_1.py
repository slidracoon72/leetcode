from typing import List


class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned_set = set(banned)  # for O(1) lookup

        res = 0
        cur_sum = 0
        i = 1
        while i < n + 1:
            if i not in banned_set:
                if cur_sum < maxSum:
                    cur_sum += i
                    res += 1

                if cur_sum > maxSum:
                    res -= 1
                    cur_sum -= i
            i += 1

        return res


c = Solution()
banned = [1, 6, 5]
n = 5
maxSum = 6
print(c.maxCount(banned, n, maxSum))
