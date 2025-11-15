from typing import List


class Solution:
    # Greedy Approach - 23 / 46 testcases passed
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        res = 0
        n = len(triangle)
        i, prev = 0, 0

        while i < n:
            cur = triangle[i]
            temp1, temp2 = 1001, 1001
            if prev < len(cur):
                temp1 = cur[prev]
            if prev + 1 < len(cur):
                temp2 = cur[prev + 1]

            if temp1 < temp2:
                res += temp1
            else:
                res += temp2
                prev += 1
            i += 1

        return res

    # Dynamic Programming - Bottom Up
    # Solution - https://leetcode.com/problems/triangle/solutions/7221386/bottom-up-dynamic-programming-in-place-beats-100/?https://leetcode.com/problems/triangle/solutions/7221386/bottom-up-dynamic-programming-in-place-beats-100/?envType=daily-question&envId=2025-09-25https://leetcode.com/problems/triangle/solutions/7221386/bottom-up-dynamic-programming-in-place-beats-100/?envType=daily-question&envId=2025-09-25https://leetcode.com/problems/triangle/solutions/7221386/bottom-up-dynamic-programming-in-place-beats-100/?envType=daily-question&envId=2025-09-25https://leetcode.com/problems/triangle/solutions/7221386/bottom-up-dynamic-programming-in-place-beats-100/?envType=daily-question&envId=2025-09-25=daily-question&envId=2025-09-25

    def minimumTotal1(self, triangle: List[List[int]]) -> int:
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        return triangle[0][0]


c = Solution()
triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
print(c.minimumTotal1(triangle))