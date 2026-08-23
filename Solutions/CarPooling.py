from typing import List


# Line Sweep / Difference Array Question
# Solving using a Sorted Events Approach
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # Map each location to the net change in passengers at that point
        # (positive when passengers get in, negative when they get out)

        # 1. Initialize an empty list to hold (location, change) events
        events = []

        # 2. Add a pickup event and a dropoff event for each trip
        for numPassengers, start, end in trips:
            events.append((start, numPassengers))  # passengers get in at 'start'
            events.append((end, -numPassengers))  # passengers get out at 'end'

        # Sort events by location; if a pickup and dropoff happen at the
        # same location, process the dropoff first (sorting by change
        # ascending naturally puts negative deltas before positive ones)
        events.sort()

        # currPassengers = passengers currently in the car as we sweep east
        currPassengers = 0

        # Sweep through every event in order of location
        for location, change in events:
            # apply the pickup/dropoff at this location
            currPassengers += change

            # if at any point we exceed capacity, it's impossible
            if currPassengers > capacity:
                return False

        # never exceeded capacity at any point along the route
        return True


trips = [[2, 1, 5], [3, 3, 7]]
capacity = 4
c = Solution()
print(c.carPooling(trips, capacity))
