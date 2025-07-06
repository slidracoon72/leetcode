from typing import List


# Graph - DFS (Iterative)
# Time: O(N+E), where N = number of rooms, E = total number of keys across all rooms
# Space: O(N), due to visited set
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # A set to keep track of visited rooms
        visited = set()

        # Initialize a stack with room 0, since we already have the key for room 0
        stack = [0]

        # Loop until there are no more rooms to visit
        while stack:
            # Take the last room from the stack (LIFO order)
            room = stack.pop()

            # Mark this room as visited
            visited.add(room)

            # Iterate through all keys found in the current room
            for key in rooms[room]:
                # If the room corresponding to this key has not been visited
                if key not in visited:
                    # Add the room to the stack to visit it later
                    stack.append(key)

        # After visiting all possible rooms, check if we've visited all the rooms
        return len(visited) == len(rooms)


c = Solution()
# rooms = [[1], [2], [3], []]
rooms = [[1, 3], [3, 0, 1], [2], [0]]
print(c.canVisitAllRooms(rooms))
