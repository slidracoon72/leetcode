from typing import List


class Solution:
    # Binary Decomposition + Direct Calculation
    # Time: O(q * logn), Space: O(logn)
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10 ** 9 + 7  # Modulo value to prevent integer overflow
        powers = []  # List to store the powers of 2 that make up 'n'
        cur = 1  # Current power of 2 being considered

        # Decompose n into powers of 2 (from least significant to most significant)
        while n > 0:
            if n % 2 == 1:  # If the current bit is set
                powers.append(cur)  # Store the current power of 2
            cur *= 2  # Move to the next power of 2
            n //= 2  # Shift n to the right by 1 bit

        res = []  # Result list to store answers for each query

        # Process each query
        for left, right in queries:
            cur = 1  # Product accumulator for the current query
            # Multiply the powers in the given range and take modulo
            for i in range(left, right + 1):
                cur = (cur * powers[i]) % MOD
            res.append(cur)  # Append the result for this query

        return res  # Return the list of results


c = Solution()
n = 15
queries = [[0, 1], [2, 2], [0, 3]]
print(c.productQueries(n, queries))
