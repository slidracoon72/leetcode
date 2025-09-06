class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while n > 1:
            n /= 4
        return n == 1


c = Solution()
print(c.isPowerOfFour(16))
print(c.isPowerOfFour(5))
print(c.isPowerOfFour(1))
