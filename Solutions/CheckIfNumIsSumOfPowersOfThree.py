# LC-1780: Check if Number is a Sum of Powers of Three
class Solution:
    # Solved using Recursive Backtracking
    # Time: O(n), Space: O(log n) due to recursion depth
    def checkPowersOfThree(self, n: int) -> bool:
        # Helper function to recursively explore sums of powers of 3
        # i: current exponent (0 for 3^0, 1 for 3^1, etc.)
        # cur: current sum of selected powers
        def backtrack(i, cur):
            # Base case: if current sum equals target, we found a valid combination
            if cur == n:
                return True
            # Base case: if current sum exceeds target or power exceeds n, stop this path
            if cur > n or 3 ** i > n:
                return False

            # Choice 1: Include the current power of 3 (3^i) in the sum
            if backtrack(i + 1, cur + 3 ** i):
                return True
            # Choice 2: Skip the current power of 3, keep sum unchanged
            if backtrack(i + 1, cur):
                return True

            # If neither choice works, this path fails
            return False

        # Start backtracking from exponent 0 with sum 0
        return backtrack(0, 0)

    # Solved using Greedy Approach
    # Time: O(log n), Space: O(1)
    def checkPowersOfThree1(self, n: int) -> bool:
        # Find the largest power of 3 less than or equal to n
        i = 0
        while 3 ** i <= n:
            i += 1
        i -= 1  # Backtrack to the largest valid power (3^i <= n)

        # Greedily subtract the largest possible powers of 3
        while i >= 0:
            power = 3 ** i  # Calculate current power of 3
            if power <= n:  # If current power fits, subtract it from n
                n -= power

            if power <= n:  # If power still fits after subtraction, n is overshot (duplicate powers needed)
                return False  # Return False since we can only use each power once

            i -= 1  # Move to the next smaller power

        # If n becomes 0, it means n is a sum of distinct powers of 3
        return n == 0


c = Solution()
print(c.checkPowersOfThree(12))
print(c.checkPowersOfThree(91))
print(c.checkPowersOfThree(21))
print("---------")
print(c.checkPowersOfThree1(12))
print(c.checkPowersOfThree1(91))
print(c.checkPowersOfThree1(21))
