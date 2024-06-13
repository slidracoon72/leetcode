from typing import List


# Solved using Decision Tree, Recursion, Depth First Search
# Neetcode: https://www.youtube.com/watch?v=GBKI9VSKdGg
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        # Depth First Search function to traverse through decision tree
        # i = candidate value, cur = current list of elements, total = total of cur
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return

            # going through left branch of tree (recursively)
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])

            # going through right branch of tree (recursively)
            # For right tree, we exclude the already used candidate value in left tree
            cur.pop()
            dfs(i + 1, cur, total)

        # calling the dfs function
        dfs(0, [], 0)
        return res


c = Solution()
l = [2, 3, 6, 7]
t = 7
print(c.combinationSum(l, t))
