class Solution:
    # Time: O(logn), Space: O(1)
    def myPow(self, x: float, n: int) -> float:
        # Base case: any number to the power 0 is 1
        if n == 0:
            return 1
        # Edge case: 0 raised to any positive power is 0
        if x == 0:
            return 0

        # If the exponent is negative, convert to positive and take reciprocal of base
        if n < 0:
            n = -n
            x = 1 / x

        res = 1  # Initialize result

        # Binary exponentiation loop
        while n > 1:
            if n % 2:  # If current exponent is odd
                res = res * x  # Multiply current result with base
            n = n // 2  # Reduce exponent by half
            x = x ** 2  # Square the base

        return res * x  # Final multiplication to account for the remaining power


c = Solution()
print(c.myPow(2.00000, 10))
print(c.myPow(2.10000, 3))
print(c.myPow(2.00000, -2))
