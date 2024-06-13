class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s

        res = ""
        for r in range(numRows):
            increment = 2 * (numRows - 1)
            for i in range(r, len(s), increment):
                res += s[i]
                if 0 < r < numRows - 1 and i + increment - 2 * r < len(s):
                    res += s[i + increment - 2 * r]

        return res


c = Solution()
s = "PAYPALISHIRING"
numRows = 4
print(c.convert(s, numRows))
