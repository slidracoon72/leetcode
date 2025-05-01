# DO AGAIN
class Solution:
    # Using Dynamic Programming
    def numDecodings(self, s: str) -> int:
        n = len(s)

        # Initialize an array to store the number of ways to decode up to index i
        dp = [0] * (n + 1)

        # Base case: an empty string has one way to decode
        dp[0] = 1

        # Check each character in the string
        for i in range(1, n + 1):
            # Check if the current character is not '0'
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]

            # Check if the previous two characters form a valid decoding
            if i > 1 and '10' <= s[i - 2:i] <= '26':
                dp[i] += dp[i - 2]

        return dp[n]

    # Using Recursion
    def numDecodings1(self, s: str) -> int:

        def dfs(i):
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0

            res = dfs(i + 1)
            if i < len(s) - 1:
                if (s[i] == '1' or
                        (s[i] == '2' and s[i + 1] < '7')):
                    res += dfs(i + 2)

            return res

        return dfs(0)
