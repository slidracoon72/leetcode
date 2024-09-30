class MyCalendar:

    def __init__(self):
        # Initialize an empty list to store events, each event is represented as a tuple (start, end)
        self.events = []

    def book(self, start: int, end: int) -> bool:
        # Iterate through all the existing events to check for overlaps
        for s, e in self.events:
            # If the new event overlaps with any existing event, return False (event cannot be booked)
            # The condition checks if there is no overlap: 'e <= start' means the existing event ends before the new event starts,
            # 'end <= s' means the new event ends before the existing event starts.
            # If neither condition is true, there is an overlap, so we return False.
            if not (e <= start or end <= s):
            # if e > start and end > s: -> Also correct
                return False

        # If no overlaps, add the new event to the list of events and return True (event is successfully booked)
        self.events.append((start, end))
        return True
