from typing import List


# Neetcode: https://www.youtube.com/watch?v=ZGxqqjljpUI
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        f = [0] + flowerbed + [0]
        for i in range(1, len(f) - 1):
            if f[i - 1] == 0 and f[i] == 0 and f[i + 1] == 0:
                n -= 1
                f[i] = 1
        return n <= 0


c = Solution()
flowerbed = [1, 0, 0, 0, 1]
n = 1
print(c.canPlaceFlowers(flowerbed, n))
