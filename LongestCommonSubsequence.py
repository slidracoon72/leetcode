# Dynamic Programming (2D)
# Neetcode: https://www.youtube.com/watch?v=Ua0GhsJSlWM
# Time: O(m * n), Space: O(m * n)
class Solution:
    # Bottom-Up Approach
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Initialize the 2D list (dp) with zeros

        # (Option-1) List Comprehension
        # dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        # (Option-2) Normal for-loop
        l1 = len(text1)
        l2 = len(text2)
        dp = []
        # We loop until l1+1 as we need to add an extra row and column of 0's
        for i in range(l1 + 1):
            row = []
            for j in range(l2 + 1):
                row.append(0)
            dp.append(row)

        # Using 2D-DP Bottom-Up Approach (Reverse Loop)
        for i in range(l1 - 1, -1, -1):
            for j in range(l2 - 1, -1, -1):
                if text1[i] == text2[j]:
                    # If same characters, add one and diagonal cell value
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    # If different, choose max between bottom cell and right cell
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        return dp[0][0]

    # Top-Down Approach
    def longestCommonSubsequence1(self, text1: str, text2: str) -> int:
        # Get the lengths of both strings
        l1, l2 = len(text1), len(text2)

        # Create a 2D DP array with dimensions (l1+1) x (l2+1) initialized to 0
        dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]

        # Fill the DP array
        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    # Characters match, take diagonal value and add 1
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # Characters don't match, take the maximum of left and top value
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # The length of the longest common subsequence is in dp[l1][l2]
        return dp[l1][l2]


c = Solution()
text1 = "abcde"
text2 = "ace"
print(c.longestCommonSubsequence(text1, text2))
print(c.longestCommonSubsequence1(text1, text2))
