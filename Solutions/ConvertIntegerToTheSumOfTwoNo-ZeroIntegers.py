from typing import List


class Solution:
    # Time: O(n), Space: O(1)
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for x in range(1, n):
            y = n - x
            if "0" not in str(x) + str(y):
                return [x, y]
        return []

    def getNoZeroIntegers1(self, n: int) -> List[int]:
        a, b = n - 1, 1
        # Nudge a down and b up until both have no '0' digits
        while '0' in str(a) or '0' in str(b):
            a -= 1
            b += 1
        return [a, b]


c = Solution()
print(c.getNoZeroIntegers(2))
print(c.getNoZeroIntegers(11))
print(c.getNoZeroIntegers(10000))
