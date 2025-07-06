# LC - 3160: Find the Number of Distinct Colors Among the Balls
from collections import defaultdict
from typing import List


class Solution:
    # Brute Force - Time: O(N ^ Q)
    # Gives TLE - Passes 547/551 Testcases
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colors = defaultdict(int)
        res = []

        for b, c in queries:
            colors[b] = c
            seen = set()
            distinct = 0
            for color in colors.values():
                if color not in seen:
                    distinct += 1
                    seen.add(color)
            res.append(distinct)

        return res

    # Two-Hash Map Technique
    # Time Complexity: O(N), as we iterate through the queries once.
    # Space Complexity: O(N), since we use two dictionaries to store ball colors and color frequencies.
    def queryResults1(self, limit: int, queries: List[List[int]]) -> List[int]:
        # Dictionary to keep track of the color assigned to each ball
        ball_color = defaultdict(int)
        # Dictionary to track the frequency of each color
        color_freq = defaultdict(int)

        res = []  # List to store the result after each query

        for ball, color in queries:
            # If the ball is already painted, remove its previous color from the frequency count
            if ball in ball_color:
                prev_color = ball_color[ball]
                color_freq[prev_color] -= 1
                # If the previous color is no longer used, remove it from the dictionary
                if color_freq[prev_color] == 0:
                    del color_freq[prev_color]

            # Paint the ball with the new color
            ball_color[ball] = color
            # Increase the frequency count of the new color
            color_freq[color] += 1

            # Store the count of unique colors currently in use
            res.append(len(color_freq))

        return res


c = Solution()
limit = 4
queries = [[0, 1], [1, 2], [2, 2], [3, 4], [4, 5]]
print(c.queryResults1(limit, queries))
