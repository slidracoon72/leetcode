# LC - Hard


from typing import List
from collections import deque


class Solution:
    # Techdose: https://www.youtube.com/watch?v=LDiCiart4Yw&ab_channel=Techdose
    # Solved using Multi-Source BFS
    # Time: O(n), Space: O(n); where n = len(status)
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]],
                   initialBoxes: List[int]) -> int:
        # Intuition: We need to maximize candies collected by opening boxes. Start with initial boxes,
        # collect candies, use keys to unlock other boxes, and access contained boxes. Some boxes may
        # be locked initially, so we track them until unlocked. Use BFS to process boxes systematically.

        # Initialize queue with initial boxes
        queue = deque(initialBoxes)
        # Set to track locked boxes we can't open yet
        closed = set()
        # Total candies collected
        total_candies = 0

        # Process boxes using BFS
        while queue:
            # Get current box
            curr_box = queue.popleft()

            # If box is locked, add to closed set and skip
            if status[curr_box] == 0:
                closed.add(curr_box)
                continue

            # Box is unlocked: collect its candies
            total_candies += candies[curr_box]

            # Use keys to unlock other boxes
            for box_to_unlock in keys[curr_box]:
                status[box_to_unlock] = 1  # Mark box as unlocked
                # If this box was in closed set, it's now accessible
                if box_to_unlock in closed:
                    queue.append(box_to_unlock)
                    closed.remove(box_to_unlock)

            # Add contained boxes to queue
            for contained_box in containedBoxes[curr_box]:
                queue.append(contained_box)

        # Return total candies collected
        return total_candies


c = Solution()
status = [1, 0, 1, 0]
candies = [7, 5, 4, 100]
keys = [[], [], [1], []]
containedBoxes = [[1, 2], [3], [], []]
initialBoxes = [0]
print(c.maxCandies(status, candies, keys, containedBoxes, initialBoxes))
