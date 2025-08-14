class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n > 1:
            n = n / 3
        return n == 1


c = Solution()
print(c.isPowerOfThree(27))
print(c.isPowerOfThree(45))
print(c.isPowerOfThree(0))
print(c.isPowerOfThree(-1))
