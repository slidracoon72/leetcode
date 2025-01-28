from collections import defaultdict
from typing import List


# Neetcode: https://www.youtube.com/watch?v=wYoZMBenHYY
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[
        bool]:
        # Create an adjacency list to store the direct prerequisites for each course
        adj = defaultdict(list)
        for pre, crs in prerequisites:
            adj[crs].append(pre)

        # A dictionary to map each course to the set of all its prerequisites (direct and indirect)
        prereqMap = {}

        # Depth-First Search (DFS) to compute all prerequisites for a given course
        def dfs(crs):
            # If the course's prerequisites are not already computed, calculate them
            if crs not in prereqMap:
                prereqMap[crs] = set()  # Initialize the set of prerequisites for this course
                # Recursively gather prerequisites for each prerequisite course
                for prereq in adj[crs]:
                    prereqMap[crs] |= dfs(prereq)  # Union of prerequisites
                # Add the course itself as a prerequisite (indirectly)
                prereqMap[crs].add(crs)
            return prereqMap[crs]

        # Compute prerequisites for all courses (populate prereqMap)
        for crs in range(numCourses):
            dfs(crs)

        # Evaluate the queries by checking if the first course in the query is a prerequisite of the second course
        res = []
        for u, v in queries:
            res.append(u in prereqMap[v])  # Check if `u` is in the set of prerequisites for course `v`
        return res


c = Solution()
numCourses = 3
prerequisites = [[1, 2], [1, 0], [2, 0]]  # List of direct prerequisites
queries = [[1, 0], [1, 2]]  # List of queries to check
print(c.checkIfPrerequisite(numCourses, prerequisites, queries))
