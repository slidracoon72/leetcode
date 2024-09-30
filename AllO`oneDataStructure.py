from collections import defaultdict


# LC - Hard

# Actual Solution is with a Doubly Linked List

# Solved using HashMap
# Time: O(1) for all methods
# Space: O(N) when N is the number of keys
class AllOne:

    def __init__(self):
        self.d = defaultdict(int)

    def inc(self, key: str) -> None:
        self.d[key] += 1

    def dec(self, key: str) -> None:
        self.d[key] -= 1
        if self.d[key] == 0:
            self.d.pop(key)

    def getMaxKey(self) -> str:
        if self.d:
            max_key = max(self.d, key=self.d.get)
            return max_key if max_key else ""
        return ""

    def getMinKey(self) -> str:
        if self.d:
            min_key = min(self.d, key=self.d.get)
            return min_key if min_key else ""
        return ""

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
