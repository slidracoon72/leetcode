import heapq
from typing import List


class Solution:
    # Two-Heap problem to efficiently manage available and used chairs
    # Neetcode: https://www.youtube.com/watch?v=LqhxcaCctCc
    # Time complexity: O(nlogn) due to sorting and heap operations
    # Space complexity: O(n) for storing times and chairs
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        # Convert times into a list of tuples (arrival, leaving, index)
        # 'index' is the friend number, which is important to find targetFriend's chair
        times = [(t[0], t[1], i) for i, t in enumerate(times)]
        # Sort the times list based on the arrival times
        times.sort()

        # A min-heap to track the available chair numbers (initially all chairs are available)
        available_chairs = [i for i in range(len(times))]
        # A min-heap to track chairs currently in use, storing tuples (leaving_time, chair_number)
        used_chairs = []

        # Iterate through each friend's arrival and leaving times
        for a, l, i in times:
            # Free up chairs for friends who have already left by the current arrival time
            while used_chairs and used_chairs[0][0] <= a:
                # Remove the chair used by the friend who is leaving
                leaving, chair = heapq.heappop(used_chairs)
                # Add the now-available chair back to the available chairs heap
                heapq.heappush(available_chairs, chair)

            # Assign the smallest available chair to the arriving friend
            chair = heapq.heappop(available_chairs)
            # Push the chair into the used_chairs heap with its corresponding leaving time
            heapq.heappush(used_chairs, (l, chair))

            # If this is the targetFriend, return the chair they sat on
            if i == targetFriend:
                return chair
