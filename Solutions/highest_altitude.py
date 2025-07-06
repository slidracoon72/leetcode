class Solution:
    def largestAltitude(self, gain) -> int:
        maxAltitude = 0
        currentAltitude = 0

        for g in gain:
            currentAltitude += g
            maxAltitude = max(maxAltitude, currentAltitude)

        return maxAltitude

    # My Solution
    def largestAltitude1(self, gain) -> int:
        a = [0]
        a.append(gain[0])

        for i in range(1, len(gain)):
            x = a[-1] + gain[i]
            a.append(x)

        return max(a)


c = Solution()
gain = [-4, -3, -2, -1, 4, 3, 2]
gain1 = [-5, 1, 5, 0, -7]
print(c.largestAltitude(gain1))
print(c.largestAltitude1(gain1))
