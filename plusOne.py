from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = int(''.join(str(e) for e in digits))
        s += 1
        s = str(s)
        l = []
        for i in s:
            l.append(int(i))

        return l


c = Solution()
a1 = [1, 2, 3]
a2 = [4, 3, 2, 1]
a3 = [9]
print(c.plusOne(a1))
print(c.plusOne(a2))
print(c.plusOne(a3))
