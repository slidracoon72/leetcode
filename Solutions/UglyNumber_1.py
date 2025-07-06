class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        prime_factors = [2, 3, 5]

        for p in prime_factors:
            while n % p == 0:
                n = n // p
        return n == 1


c = Solution()
print(c.isUgly(6))
print(c.isUgly(7))
print(c.isUgly(9))
