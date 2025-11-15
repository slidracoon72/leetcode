class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        empty = numBottles
        while empty >= numExchange:
            ans += 1
            empty -= numExchange - 1
            numExchange += 1
        return ans


c = Solution()
numBottles = 13
numExchange = 6
print(c.maxBottlesDrunk(numBottles, numExchange))
