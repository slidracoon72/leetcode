# Neetcode: https://www.youtube.com/watch?v=7utL5cTDcnA
# Time: O(n), Space: O(n) where n is the number of total events booked.
class MyCalendarTwo:

    def __init__(self):
        # List to store non-overlapping events
        # This will hold all the events that have been booked successfully so far.
        self.non_overlapping = []

        # List to store overlapping events (but not triple overlapping)
        # This holds the intervals where two events overlap but do not cause a triple booking.
        self.overlapping = []

    def book(self, start: int, end: int) -> bool:
        # First, check if the new event causes a triple booking by comparing it with the already overlapping intervals.
        # If there is any overlap with an event in the 'overlapping' list, it would cause a triple booking, so we return False.
        for s, e in self.overlapping:
            # Check if the new event overlaps with any of the existing double-booked intervals
            if not (e <= start or end <= s):
                return False  # Triple booking detected, so the event cannot be added.

        # Check if the new event overlaps with non-overlapping events.
        # If it overlaps, add the overlap to the 'overlapping' list, as this would be a new double-booked event.
        for s, e in self.non_overlapping:
            # If there is an overlap with a non-overlapping event
            if not (e <= start or end <= s):
                # Add the overlapping interval to the 'overlapping' list.
                self.overlapping.append((max(s, start), min(e, end)))

        # Finally, add the new event to the 'non_overlapping' list as it doesn't cause a triple booking.
        self.non_overlapping.append((start, end))

        return True  # Event added successfully without causing triple booking.
