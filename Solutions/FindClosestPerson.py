class Solution:
    # Time: O(1), Space: O(1)
    def findClosest(self, x: int, y: int, z: int) -> int:
        dx = abs(x - z)
        dy = abs(y - z)
        if dx < dy:
            return 1
        elif dx > dy:
            return 2
        else:
            return 0


c = Solution()
print(c.findClosest(x=2, y=7, z=4))
print(c.findClosest(x=2, y=5, z=6))
print(c.findClosest(x=1, y=5, z=3))
