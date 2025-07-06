from math import sqrt


# Neetcode: https://www.youtube.com/watch?v=B0UrG_X2faA
class Solution:
    # Using Hash-Set
    # Time: O(sqrt(c)), Space: O(sqrt(c))
    def judgeSquareSum(self, c: int) -> bool:
        # To store values of b^2
        squareroot = set()

        for i in range(int(sqrt(c)) + 1):
            squareroot.add(i * i)

        a = 0
        while a * a <= c:
            # check: b^2 = c - a^2
            target = c - a * a
            if target in squareroot:
                return True
            a += 1

        return False

    # Using Two-Pointers
    # Time: O(sqrt(c)), Space: O(1)
    def judgeSquareSum1(self, c: int) -> bool:
        left, right = 0, int(sqrt(c))
        while left <= right:
            total = (left * left) + (right * right)
            if total > c:
                right -= 1
            elif total < c:
                left += 1
            else:
                return True
        return False
