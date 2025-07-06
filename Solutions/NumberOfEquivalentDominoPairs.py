from collections import defaultdict
from typing import List


class Solution:
    # Brute Force - Gives TLE
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        n = len(dominoes)
        res = 0
        for i in range(n - 1):
            a, b = dominoes[i]
            for j in range(i + 1, n):
                c, d = dominoes[j]
                if (a == c and b == d) or (a == d and b == c):
                    res += 1

        return res

    # Optimal - Make every pair a number with smaller number in ten's place and larger in one's place
    # Time: O(n), Space: O(n)
    def numEquivDominoPairs1(self, dominoes: List[List[int]]) -> int:
        # Dictionary to count occurrences of each normalized domino
        num = defaultdict(int)
        res = 0

        # Iterate through each domino
        for x, y in dominoes:
            # Normalize the domino so [a, b] and [b, a] are considered the same
            val = x * 10 + y if x <= y else y * 10 + x

            # For each previous occurrence of this domino, we can form a new pair
            res += num[val]

            # Increment the count for this normalized domino
            num[val] += 1

        # Return the total number of equivalent domino pairs
        return res


c = Solution()
dominoes = [[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]
print(c.numEquivDominoPairs1(dominoes))
