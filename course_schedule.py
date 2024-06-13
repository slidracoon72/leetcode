from typing import List


# Graph Adjacency List Question
# Solving using DFS
# Neetcode: https://www.youtube.com/watch?v=EgI5nU9etnU
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Map each course with its prerequisites using HashMap

        # 1. Initialize the prerequisites of each course as an empty list
        preMap = {i: [] for i in range(numCourses)}

        # 2. Add each courses' corresponding prerequisite
        for course, pre in prerequisites:
            preMap[course].append(pre)

        # visitSet = all courses visited along the current DFS path
        visitSet = set()

        # Defining DFS function
        def dfs(course):
            # if loop detected in graph(course already visited), return False
            if course in visitSet:
                return False

            # if no prerequisite required
            if not preMap[course]:
                return True

            visitSet.add(course)
            # recursively call DFS on the courses' prerequisites
            for pre in preMap[course]:
                if not dfs(pre): return False
            visitSet.remove(course)

            # remove prerequisite of visited(and doable) course
            preMap[course] = []

            return True

        # call DFS for each node of the graph (i.e, for each course)
        for course in range(numCourses):
            if not dfs(course): return False
        return True


numCourses = 3
prerequisites = [[2, 1], [1, 0]]
c = Solution()
print(c.canFinish(numCourses, prerequisites))
