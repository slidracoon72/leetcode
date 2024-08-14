from typing import List


# Solved using Decision Tree, Recursion, Depth First Search
# Neetcode: https://www.youtube.com/watch?v=FOyRpNUSFeA
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        # Sort the candidates to avoid duplicate combinations
        candidates.sort()

        # Depth First Search function to traverse through decision tree
        # i = candidate value, cur = current list of elements, total = total of cur
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i == len(candidates) or total > target:
                return

            # Option 1: include candidates[i]
            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])

            # Backtrack
            cur.pop()

            # Option 2: skip candidates[i]
            # Increment 'i' till we find a different value
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, cur, total)

        # calling the dfs function
        dfs(0, [], 0)
        return res


c = Solution()
candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
print(c.combinationSum2(candidates, target))
