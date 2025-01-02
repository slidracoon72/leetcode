class Solution:
    # Dynamic Programming with DFS and Memoization
    # Time: O(high), Space: O(high)
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10 ** 9 + 7

        # Memoization dictionary to store results for a given length
        dp = {}

        def dfs(length):
            # If the length exceeds the allowed maximum, return 0
            if length > high:
                return 0

            # If the result for the current length is already computed, return it
            if length in dp:
                return dp[length]

            # Start with 1 if the current length is within the valid range
            count = 1 if low <= length <= high else 0

            # Add ways by appending zero '0's or one '1's
            count += dfs(length + zero)  # Add zeros
            count += dfs(length + one)  # Add ones

            # Store the result modulo `mod` for the current length
            dp[length] = count % mod
            return dp[length]

        # Start the DFS with an empty string (length 0)
        return dfs(0)


c = Solution()
low = 3
high = 3
zero = 1
one = 1
print(c.countGoodStrings(low, high, zero, one))
