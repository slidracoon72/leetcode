from typing import List


class Solution:
    # Getting TLE
    # 702 / 718 testcases passed
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        def helper(x, y):
            res = 0
            x, y = str(x), str(y)
            l = min(len(x), len(y))
            i = 0
            while i < l:
                if x[i] == y[i]:
                    res += 1
                    i += 1
                else:
                    break
            return res

        res = 0
        for x in arr1:
            for y in arr2:
                res = max(res, helper(x, y))
        return res

    # Using Hash Set
    # Passes All Test Cases
    # Time: O(m*n), Space: O(m*n)
    def longestCommonPrefix1(self, arr1: List[int], arr2: List[int]) -> int:
        # Put all the possible prefixes of each element in arr1 into a HashSet.
        pre = set()
        for x in arr1:
            x = str(x)
            for i in range(len(x)):
                pre.add(x[:i + 1])

        # For all the possible prefixes of each element in arr2, check if it exists in the HashSet.
        res = 0
        for x in arr2:
            x = str(x)
            for i in range(len(x)):
                if x[:i + 1] in pre:
                    res = max(res, i + 1)
        return res


c = Solution()
arr1 = [1, 10, 100]
arr2 = [1000]
print(c.longestCommonPrefix1(arr1, arr2))
