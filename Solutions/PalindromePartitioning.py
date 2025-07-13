from typing import List


class Solution:

    def partition(self, s: str) -> List[List[str]]:
        # 'res' stores all the possible palindrome partitions
        # 'part' is the current list of substrings in the ongoing partition
        res, part = [], []

        # Depth-first search function to explore all partitions
        def dfs(i):
            # If we have reached the end of the string, store the current partition
            if i >= len(s):
                res.append(part.copy())
                return

            # Try all possible substrings starting from index i
            for j in range(i, len(s)):
                # Check if the substring s[i:j+1] is a palindrome
                if self.isPali(s, i, j):
                    # If it is, add it to the current partition
                    part.append(s[i: j + 1])
                    # Recurse on the remaining substring
                    dfs(j + 1)
                    # Backtrack to explore other partitions
                    part.pop()

        # Start the DFS from index 0
        dfs(0)
        return res

    # Helper function to check if a substring s[l:r+1] is a palindrome
    def isPali(self, s, l, r):
        # Use two pointers to compare characters from both ends
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True


c = Solution()
s = "aab"
print(c.partition(s))
