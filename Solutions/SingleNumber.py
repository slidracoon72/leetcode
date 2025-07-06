from typing import List


class Solution:
    # Using XOR - Bit Manipulation
    # XOR cancels out same numbers
    # Time: O(n), Space: O(n)
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res ^= n
        return res

    # Using HashMap
    # Time: O(n), Space: O(n)
    def singleNumber1(self, nums: List[int]) -> int:
        d = dict()
        for i in nums:
            if i in d:
                d.pop(i)
            else:
                d[i] = 1

        return next(iter(d))


v = Solution()

l1 = [2, 2, 1]  # 1
l2 = [4, 1, 2, 1, 2]  # 4
print(v.singleNumber(l1))
print(v.singleNumber(l2))
