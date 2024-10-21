class Solution:
    # Brute Force - Passes all test cases
    # Time: O(2^n)
    def findKthBit(self, n: int, k: int) -> str:
        s = "0"

        def rev_inv(s):
            s = list(s)
            for i in range(len(s)):
                if s[i] == "1":
                    s[i] = "0"
                else:
                    s[i] = "1"
            return "".join(s)[::-1]

        for i in range(1, n):
            s = s + "1" + rev_inv(s)
            if i == k - 1:
                return s[i]

        return s[k - 1]

    # Optimal - Using Recursion
    # Neetcode: https://www.youtube.com/watch?v=h9DOEqeb_ZA
    # Time: O(n), Space: O(n)
    def findKthBit1(self, n: int, k: int) -> str:
        length = 2 ** n - 1

        def helper(length, k):
            if length == 1:
                return "0"

            half = length // 2
            # 15 // 2 = 7, so half is 7 + 1 = 8
            # On left side
            if k <= half:
                return helper(half, k)
            # on right side
            elif k > half + 1:
                res = helper(half, 1 + length - k)
                return "0" if res == "1" else "1"
            else:
                return "1"

        return helper(length, k)


c = Solution()
n = 4
k = 11
print(c.findKthBit(n, k))
