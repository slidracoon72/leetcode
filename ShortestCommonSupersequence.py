# LC - Hard

# Similar to LongestCommonSubsequence.py
# Dynamic Programming (2D)
# Bottom - Up Solution
# Neetcode: https://www.youtube.com/watch?v=JkjQNJSxXN0&ab_channel=NeetCodeIO
# Time: O(n * m * (n + m)), Space: O(n * (n + m))
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)

        # Instead of creating a full (n+1) x (m+1) DP table, we optimize by storing only two rows at a time.
        # 'prev' stores the results of the previous row in the DP table.
        prev = [str2[i:] for i in range(m)]  # Initialize with suffixes of str2
        prev.append("")  # Base case: empty string when i = n

        # Process rows from bottom to top
        for i in reversed(range(n)):
            curr = [""] * m  # Initialize current row storage
            curr.append(str1[i:])  # Base case: suffix of str1 when j = m

            # Process columns from right to left
            for j in reversed(range(m)):
                if str1[i] == str2[j]:
                    # If characters match, take the diagonal result
                    curr[j] = str1[i] + prev[j + 1]
                else:
                    # If characters don't match, consider two choices:
                    bottom = str1[i] + prev[j]  # Include str1[i], move down
                    right = str2[j] + curr[j + 1]  # Include str2[j], move right

                    # Choose the smaller string lexicographically
                    if len(bottom) < len(right):
                        curr[j] = bottom
                    else:
                        curr[j] = right

            prev = curr  # Update previous row for next iteration

        return curr[0]  # The result is stored in the top-left cell


c = Solution()
str1 = "abac"
str2 = "cab"
print(c.shortestCommonSupersequence(str1, str2))
