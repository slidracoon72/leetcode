from typing import List


# Graph - DFS
# Time: O(n^2) (as we traverse the nxn matrix)
# Space: O(n) (as we have a 'seen' set of length n)
class Solution:

    # With Adjacency List (Recursion DFS)
    def findCircleNum(self, isConnected: List[List[int]]):
        # Get the number of rows and columns in the matrix
        rows, cols = len(isConnected), len(isConnected[0])
        # Initialize an adjacency list to represent the graph
        adjacent = {}
        # Initialize a set to keep track of visited cities
        seen = set()
        # Initialize the province counter
        province = 0

        # Construct the adjacency list from the isConnected matrix
        for i in range(rows):
            for j in range(cols):
                if isConnected[i][j] == 1:
                    if i not in adjacent:
                        adjacent[i] = [j]
                    else:
                        adjacent[i].append(j)

        # Define a depth-first search (DFS) function to traverse the graph
        def dfs(city) -> int:
            # If the city has already been visited, return 0 (no new province found)
            if city in seen:
                return 0
            else:
                # Mark the city as visited
                seen.add(city)

            # Get the neighboring cities
            neighbours = adjacent[city]
            # Recursively visit all the neighbors
            for n in neighbours:
                dfs(n)

            # Return 1 to indicate a new province has been found
            return 1

        # Iterate over each city in the adjacency list
        for key in adjacent:
            # For each city, perform DFS to find all connected cities
            # Increment the province count for each DFS call that returns 1
            province += dfs(key)

        # Return the total number of provinces
        return province

    # With Stack (without Adjacency List) (Iterative DFS)
    def findCircleNum1(self, isConnected: List[List[int]]) -> int:
        # Get the number of cities
        n = len(isConnected)
        # Initialize a set to keep track of visited cities
        seen = set()
        # Initialize the province counter
        province = 0

        # Define an iterative depth-first search (DFS) function
        def dfs(start: int):
            # Initialize a stack with the starting city
            stack = [start]
            # Process the stack until it's empty
            while stack:
                city = stack.pop()
                # If the city has not been visited
                if city not in seen:
                    # Mark the city as visited
                    seen.add(city)
                    # Add all directly connected cities to the stack
                    for neighbor in range(n):
                        if isConnected[city][neighbor] == 1 and neighbor not in seen:
                            stack.append(neighbor)

        # Iterate over each city
        for city in range(n):
            # If the city has not been visited, it means we found a new province
            if city not in seen:
                # Perform DFS from this city
                dfs(city)
                # Increment the province counter
                province += 1

        # Return the total number of provinces
        return province


c = Solution()
isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(c.findCircleNum1(isConnected))
