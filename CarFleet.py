from typing import List


class Solution:
    # Using Stack
    # Time: O(nlogn), Space: O(n)
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair up positions and speeds of each car
        pair = [(p, s) for p, s in zip(position, speed)]

        # Sort cars by starting position in descending order (farthest from target first)
        pair.sort(reverse=True)

        stack = []  # Stack to track arrival times (i.e., fleets)

        for p, s in pair:  # Iterate over cars from farthest to closest to target
            # Calculate time it takes for this car to reach the target
            time = (target - p) / s
            stack.append(time)

            # If the current car would arrive earlier or at the same time as the one in front,
            # it merges into the same fleet, so we pop it (only keep leading fleet)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        # The number of fleets is the number of unique times left in the stack
        return len(stack)


c = Solution()
target = 10
position = [4, 1, 0, 7]
speed = [2, 2, 1, 1]
print(c.carFleet(target, position, speed))
