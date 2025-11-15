from typing import List


class Solution:
    # Time: O(n), Space: O(1)
    def sumZero(self, n: int) -> List[int]:
        # Edge case: if n is 0 or 1, only possible valid output is [0]
        if n <= 1:
            return [0]

        res = []
        # If n is odd, include 0 in the result to make total count odd
        if n % 2:
            res = [0]

        i = 1
        # Keep adding pairs of numbers (i and -i) until the list has n elements
        while len(res) < n:
            res.append(i)  # Add positive integer
            if len(res) < n:  # Ensure we don't exceed n
                res.append(-i)  # Add its negative counterpart
            i += 1

        # The list will now contain n unique integers summing to 0
        return res

    # Similar as above
    def sumZero1(self, n: int) -> List[int]:
        # If n is even: just return pairs of numbers (i, -i)
        # If n is odd: include 0, then return pairs
        res = [0] if n % 2 else []

        # Add pairs (i, -i) until we reach n elements
        for i in range(1, n // 2 + 1):
            res.extend([i, -i])

        return res


c = Solution()
print(c.sumZero(5))
print(c.sumZero(3))
print(c.sumZero(1))
