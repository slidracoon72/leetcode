class Solution:
    # Similar to LongestCommonSubsequence.py
    # Bottom-Up Approach
    def longestPalindromeSubseq(self, s: str) -> int:
        # The longest palindromic subsequence of s is exactly the longest
        # common subsequence between s and its reverse — so we can reuse
        # the LCS(text1, text2) approach directly with text2 = reverse(s).
        rev = s[::-1]

        # Initialize the 2D list (dp) with zeros

        # (Option-1) List Comprehension
        # dp = [[0 for j in range(len(rev) + 1)] for i in range(len(s) + 1)]

        # (Option-2) Normal for-loop
        l1 = len(s)
        l2 = len(rev)
        dp = []
        # We loop until (l1 + 1) as we need to add an extra row and column of 0's
        for i in range(l1 + 1):
            row = []
            for j in range(l2 + 1):
                row.append(0)
            dp.append(row)

        # Using 2D-DP Bottom-Up Approach (Reverse Loop)
        for i in range(l1 - 1, -1, -1):
            for j in range(l2 - 1, -1, -1):
                if s[i] == rev[j]:
                    # If same characters, add one and diagonal cell value
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    # If different, choose max between bottom cell and right cell
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        return dp[0][0]
