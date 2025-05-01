import math


class Solution:
    # Neetcode: https://www.youtube.com/watch?v=y_XVeVUpdP4&ab_channel=NeetCodeIO
    # Time: O(logn), Space: O(1)
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7  # Use modulo to avoid large numbers (as required by the problem)

        # Similar to Pow(x,n).py
        # Helper function to compute (x^n) % MOD using binary exponentiation
        def pow(x, n):
            if n == 0:
                return 1  # Base case: any number to the power 0 is 1

            res = 1
            while n > 1:
                if n % 2:
                    res = (res * x) % MOD  # If n is odd, include x in the result
                n = n // 2  # Halve the exponent
                x = (x ** 2) % MOD  # Square the base each time

            return (res * x) % MOD  # Final multiplication to complete the exponentiation

        # Calculate number of even positions (0-based even indices)
        even = math.ceil(n / 2)
        # Calculate number of odd positions (0-based odd indices)
        odd = math.floor(n / 2)

        # Even positions can take 5 values: {0, 2, 4, 6, 8}
        # Odd positions can take 4 values: {2, 3, 5, 7}
        # Total combinations = (5^even) * (4^odd)
        return (pow(5, even) * pow(4, odd)) % MOD


c = Solution()
print(c.countGoodNumbers(1))
print(c.countGoodNumbers(4))
print(c.countGoodNumbers(50))
