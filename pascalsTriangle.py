from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(numRows - 1):
            temp = [0] + res[-1] + [0]
            row = []
            for j in range(len(res[-1]) + 1):
                row.append(temp[j] + temp[j + 1])
            res.append(row)
        return res


sol = Solution()
a = 5
b = 7
c = 10
print("Pascal Triangle with", a, "rows:", sol.generate(a))
print("Pascal Triangle with", b, "rows:", sol.generate(b))
print("Pascal Triangle with", c, "rows:", sol.generate(c))

ar = [0] + [1, 2, 3, 4, 5] + [6]
print(ar)
r = [7, 8, 9, 10]
for x in r:
    ar.append(x)
print("New:", ar)

