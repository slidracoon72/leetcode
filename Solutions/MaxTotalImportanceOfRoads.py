from collections import defaultdict
from typing import List


class Solution:
    # Time: O(n*logn)
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        # Create a dictionary to store the degree of each city
        degree = [0] * n
        for c1, c2 in roads:
            degree[c1] += 1
            degree[c2] += 1

        # Sort the cities based on their degrees in descending order
        # range(n) gives list = [0...n-1]
        sorted_cities = sorted(range(n), key=lambda x: degree[x], reverse=True)

        # Assign the highest value to the city with the highest degree
        values = [0] * n
        for i in range(n):
            values[sorted_cities[i]] = n - i

        # Calculate the total importance
        res = 0
        for c1, c2 in roads:
            res += values[c1] + values[c2]

        return res

    # Some test cases fail as number of cities not considered
    def maximumImportance1(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        for c1, c2 in roads:
            adj[c1].append(c2)
            adj[c2].append(c1)

        sorted_adj = dict(sorted(adj.items(), key=lambda x: len(x[1])))  # x is (key,value), x[1] is value

        points = defaultdict(int)
        i = 1
        for k in sorted_adj:
            points[k] = i
            i += 1

        res = 0
        for c1, c2 in roads:
            res += points[c1] + points[c2]

        return res


c = Solution()
n = 5
# roads = [[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]]
roads = [[0, 3], [2, 4], [1, 3]]
print(c.maximumImportance(n, roads))
