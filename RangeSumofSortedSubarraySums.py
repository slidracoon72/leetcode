from typing import List


class Solution:
    # My Solution - Bit Inefficient
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        res = []
        MOD = 10 ** 9 + 7
        for i in range(n):
            cur_sum = 0
            for j in range(i, n):
                res.append(sum(nums[i:j + 1]) % MOD)
        res = sorted(res)
        return sum(res[left - 1:right]) % MOD

    # Neetcode: https://www.youtube.com/watch?v=7XTGlO6b16A
    # TIme: O(n^2 * logn), Space: O(n^2)
    def rangeSum1(self, nums: List[int], n: int, left: int, right: int) -> int:
        res = []
        MOD = 10 ** 9 + 7
        for i in range(n):
            cur_sum = 0
            for j in range(i, n):
                cur_sum = (cur_sum + nums[j]) % MOD
                res.append(cur_sum)
        res.sort()
        ans = 0
        for i in range(left - 1, right):
            ans = (ans + res[i]) % MOD
        return ans


c = Solution()
nums = [1, 2, 3, 4]
n = 4
left = 1
right = 10
print(c.rangeSum(nums, n, left, right))
