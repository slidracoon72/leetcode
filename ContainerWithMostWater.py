from typing import List


class Solution:
    # Brute Force -> Time: O(n^2)
    def maxArea_bf(self, height) -> int:
        res = 0

        for l in range(len(height)):
            for r in range(l + 1, len(height)):  # keeping right pointer ahead of left pointer
                area = (r - l) * min(height[l], height[r])
                res = max(res, area)

        return res

    # Using Two Pointers
    # Optimal Solution -> Time: O(n)
    def maxArea(self, height: List[int]) -> int:
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

    # Similar as above
    def maxArea1(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n - 1
        res = 0
        while l < r:
            h = min(height[l], height[r])
            w = r - l
            water = h * w
            res = max(res, water)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return res


c = Solution()
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(c.maxArea(height))
