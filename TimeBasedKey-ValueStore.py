class TimeMap:

    def __init__(self):
        # Initialize a dictionary to store key -> list of [value, timestamp] pairs
        self.keyStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # If the key doesn't exist, initialize an empty list
        if key not in self.keyStore:
            self.keyStore[key] = []
        # Append the (value, timestamp) pair to the list for this key
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # Retrieve the list of (value, timestamp) pairs for the given key
        # If the key doesn't exist, return an empty list
        res, values = "", self.keyStore.get(key, [])

        # Binary search to find the latest timestamp <= given timestamp
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                # Found a valid timestamp, store the value and move right to check for newer timestamps
                res = values[m][0]
                l = m + 1
            else:
                # Current timestamp is too large, move left
                r = m - 1

        return res


timeMap = TimeMap()
timeMap.set("foo", "bar", 1)
print(timeMap.get("foo", 1))
print(timeMap.get("foo", 3))
timeMap.set("foo", "bar2", 4)
print(timeMap.get("foo", 4))
print(timeMap.get("foo", 5))
