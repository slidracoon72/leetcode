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

    # Neetcode: https://www.youtube.com/watch?v=yz48myznqQY
    # Using Bitwise &
    def minBitFlips1(self, start: int, goal: int) -> int:
        res = 0

        while start or goal:
            if (start & 1) != (goal & 1):
                res += 1
            start = start // 2
            goal = goal // 2

        return res

    # Using Bitwise Right Shift
    def minBitFlips1(self, start: int, goal: int) -> int:
        res = 0

        while start or goal:
            if (start % 2) != (goal % 2):
                res += 1
            start = start >> 1
            goal = goal >> 1

        return res

    # Using Bitwise XOR
    #  10 -> 1010
    #  7  -> 0111
    # XOR -> 1101
    # Now count number of 1's after XOR to get flips to change
    def minBitFlips2(self, start: int, goal: int) -> int:
        res = 0

        n = start ^ goal

        while n:
            res += n & 1
            n = n >> 1

        return res


c = Solution()
start = 10
goal = 7
print(c.minBitFlips(start, goal))
