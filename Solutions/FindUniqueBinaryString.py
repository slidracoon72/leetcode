from typing import List


# Recursive - Backtracking
# Time: O(n^2), Space: O(n^2)
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res = ""
        n = len(nums)
        numbers = set(nums)

        # Backtracking function
        def buildNumber(curr):
            nonlocal res
            if len(curr) == n:  # if number is generated
                if curr not in numbers:
                    res = curr
                    return True
                return False

            # Try '0'
            curr += "0"
            if buildNumber(curr):
                return True
            curr = curr[:-1]  # reset

            # Try '1'
            curr += "1"
            if buildNumber(curr):
                return True
            curr = curr[:-1] # reset

            return False

        buildNumber("")
        return res

    # Similar as above - Cleaner syntax
    def findDifferentBinaryString1(self, nums: List[str]) -> str:
        res = ""
        n = len(nums)
        numbers = set(nums)

        def backtrack(curr):
            nonlocal res
            if len(curr) == n:
                if curr not in numbers:
                    res = curr
                    return True
                return False

            # Try adding '0' and '1'
            return backtrack(curr + "0") or backtrack(curr + "1")

        backtrack("")
        return res


c = Solution()
nums = ["000", "011", "001"]
print(c.findDifferentBinaryString(nums))
