class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n > 1:
            n /= 2
        return n == 1


c = Solution()
print(c.isPowerOfTwo(1))
print(c.isPowerOfTwo(16))
print(c.isPowerOfTwo(3))
