class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start, goal = str(bin(start)[2:]), str(bin(goal)[2:])

        if len(start) > len(goal):
            diff = len(start) - len(goal)
            goal = "0" * diff + goal
        elif len(start) < len(goal):
            diff = len(goal) - len(start)
            start = "0" * diff + start

        res = 0
        for i in range(len(start) - 1, -1, -1):
            if start[i] != goal[i]:
                res += 1
        return res


c = Solution()
start = 10
goal = 7
print(c.minBitFlips(start, goal))
