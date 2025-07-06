from typing import List


class Solution:
    # Brute Force
    # Time: O(n^2), Space: O(n)
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        res = [0] * len(A)
        seen_A = set()
        seen_B = set()

        for i, (x, y) in enumerate(zip(A, B)):
            seen_A.add(x)
            seen_B.add(y)
            res[i] = len(seen_A & seen_B)

        return res

    # Optimal
    # Time: O(n), Space: O(n)
    def findThePrefixCommonArray1(self, A: List[int], B: List[int]) -> List[int]:
        res = [0] * len(A)
        common = set()
        seen = set()

        for i, (x, y) in enumerate(zip(A, B)):
            if x in seen:
                common.add(x)
            else:
                seen.add(x)

            if y in seen:
                common.add(y)
            else:
                seen.add(y)

            res[i] = len(common)

        return res


c = Solution()
A = [1, 3, 2, 4]
B = [3, 1, 2, 4]
print(c.findThePrefixCommonArray(A, B))
print(c.findThePrefixCommonArray1(A, B))
