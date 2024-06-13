class Solution:

    # BRUTE FORCE -> Time: O(n^2)
    def maxArea_bf(self, height) -> int:
        res = 0

        for l in range(len(height)):
            for r in range(l + 1, len(height)):  # keeping right pointer ahead of left pointer
                area = (r - l) * min(height[l], height[r])
                res = max(res, area)

        return res

    # Optimal Solution -> Time: O(n), Using Two Pointers
    def maxArea(self, height) -> int:
        res = 0
        l, r = 0, len(height) - 1

        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)

            # update pointers
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return res


c = Solution()
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(c.maxArea(height))
