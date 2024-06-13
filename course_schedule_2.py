from typing import List


# Topological Sorting
# Neetcode: https://www.youtube.com/watch?v=Akt3glAwyfY&t=919s
# Time: O(V+E)
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Create a dictionary to represent prerequisites for each course
        preMap = {c: [] for c in range(numCourses)}

        # Populate the preMap dictionary with prerequisites
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        output = []  # List to store the topological order
        visit, cycle = set(), set()  # Sets to track visited courses and detect cycles

        def dfs(crs):
            """
            Depth-first search to perform topological sorting.
            """
            if crs in cycle:  # If the course is in the cycle set, there's a cycle
                return False
            if crs in visit:  # If the course has already been visited, skip it
                return True

            cycle.add(crs)  # Add the course to the cycle set to track the current path
            for pre in preMap[crs]:  # Explore prerequisites
                if not dfs(pre):  # Recursive call to dfs
                    return False
            cycle.remove(crs)  # Remove the course from the cycle set after exploring its prerequisites

            visit.add(crs)  # Mark the course as visited
            output.append(crs)  # Add the course to the output list
            return True

        # Perform DFS for each course
        for c in range(numCourses):
            if not dfs(c):  # If a cycle is detected, return an empty list
                return []
        return output  # Return the topological order
