class Solution:
    # DFS - Backtracking
    # Neetcode: https://www.youtube.com/watch?v=fLjeVALxzjg
    # Time: O(2^n), Space: O(n)
    def maxUniqueSplit(self, s: str) -> int:
        def dfs(i, cur_set):
            # Base case: if we have processed the entire string, return 0 (no more splits possible)
            if i == len(s):
                return 0

            res = 0  # Initialize result to track the maximum number of unique splits

            # Loop to check every substring starting at index 'i'
            for j in range(i, len(s)):
                substr = s[i:j + 1]  # Get the current substring

                # Skip if the substring is already in the set (not unique)
                if substr in cur_set:
                    continue

                # Add the substring to the set and recursively check further splits
                cur_set.add(substr)
                # Recursively call dfs for the next index and update the result with the maximum unique splits
                res = max(res, 1 + dfs(j + 1, cur_set))
                # Backtrack: remove the substring to explore other options
                cur_set.remove(substr)

            return res

        # Start DFS with an empty set and initial index 0
        return dfs(0, set())
