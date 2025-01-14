class Solution:
    # Time: O(32) == O(1), Space: O(1)
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n % 2
            # res += n & 1 -> also correct
            n = n >> 1
        return res


c = Solution()
n = 13
print(c.hammingWeight(n))
