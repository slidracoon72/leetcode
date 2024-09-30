from typing import List


class Solution:
    # My Solution
    # Using Sliding Window
    # Passes 1964 / 2028 testcases
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        window = 50
        for x in dictionary:
            window = min(window, len(x))

        exists = set()
        word_set = set(dictionary)

        for l in range(len(s) - window + 1):
            r = l + window - 1
            while r < len(s):
                if s[l:r + 1] in word_set:
                    for i in range(l, r + 1):
                        exists.add(i)
                r += 1

        count = 0
        for i in range(len(s)):
            if i not in exists:
                count += 1

        return count

    # Neetcode: https://www.youtube.com/watch?v=ONstwO1cD7c
    # Using Dynamic Programming With Memoization / Caching
    # Time: O(n^3), Space: O(n^2)
    def minExtraChar1(self, s: str, dictionary: List[str]) -> int:
        # Convert the dictionary list into a set for faster lookup
        words = set(dictionary)

        # Dictionary for caching results of overlapping sub-problems in DFS
        dp = {}

        # Depth-first search (DFS) function to calculate the minimum extra characters from index 'i' onwards
        def dfs(i):
            # Base case: If we've processed all characters in 's', no extra characters are needed
            if i == len(s):
                return 0

            # If we've already computed the result for this index, return it from dp (memoization)
            if i in dp:
                return dp[i]

            # Case 1: Skip the current character and move to the next character
            # The '1' accounts for the skipped character, and 'dfs(i + 1)' calculates for the rest of the string
            res = 1 + dfs(i + 1)

            # Case 2: Try to match substrings starting from 'i' and ending at each 'j'
            # If a substring 's[i:j+1]' exists in the dictionary, we recursively calculate the result for the rest of the string (dfs(j + 1))
            for j in range(i, len(s)):
                if s[i:j + 1] in words:
                    # Choose the minimum between skipping or finding a valid word match
                    res = min(res, dfs(j + 1))

            # Cache the result for index 'i' to avoid recalculating in future calls
            dp[i] = res

            # Return the result for the current index
            return res

        # Start the DFS from index 0 and return the result
        return dfs(0)


c = Solution()
s = "kevlplxozaizdhxoimmraiakbak"
dictionary = ["yv", "bmab", "hv", "bnsll", "mra", "jjqf", "g", "aiyzi", "ip", "pfctr", "flr", "ybbcl", "biu", "ke",
              "lpl", "iak",
              "pirua", "ilhqd", "zdhx", "fux", "xaw", "pdfvt", "xf", "t", "wq", "r", "cgmud", "aokas", "xv", "jf",
              "cyys", "wcaz",
              "rvegf", "ysg", "xo", "uwb", "lw", "okgk", "vbmi", "v", "mvo", "fxyx", "ad", "e"]
print(c.minExtraChar(s, dictionary))
