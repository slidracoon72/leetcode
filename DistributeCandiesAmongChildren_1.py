class Solution:
    # Brute-Force solution
    # Time: O(N^3), Space: O(N)
    def distributeCandies(self, n: int, limit: int) -> int:
        res = 0
        for i in range(limit + 1):
            for j in range(limit + 1):
                for k in range(limit + 1):
                    if i + j + k == n:
                        res += 1
        return res


c = Solution()
print(c.distributeCandies(5, 2))
print(c.distributeCandies(3, 3))
